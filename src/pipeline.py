#!/usr/bin/env python3
# pipeline.py

import asyncio
import json
from pathlib import Path
from typing import Any

import aiofiles
import tiktoken
import typer
from bs4 import BeautifulSoup, NavigableString, Tag
from loguru import logger
from rich.console import Console

from translator import translate, translate_glossary_terms

console = Console()
app = typer.Typer(
    help="Contract Translation Pipeline - Translates legal documents using Google's Generative AI",
    add_completion=False,
)

# ------------
# Logging configuration
# ------------
logger.add('translation_pipeline.log', rotation='500 MB', level='INFO', format='{time} - {level} - {message}')


# ------------
# Token Management
# ------------
def tokenize_text(text: str, encoder_name: str = 'cl100k_base') -> list[int]:
    """Encodes text to token IDs using tiktoken."""
    encoder = tiktoken.get_encoding(encoder_name)
    return encoder.encode(text)


def detokenize_text(token_ids: list[int], encoder_name: str = 'cl100k_base') -> str:
    """Decodes token IDs back to text."""
    encoder = tiktoken.get_encoding(encoder_name)
    return encoder.decode(token_ids)


def chunk_text_by_tokens(
    text: str, max_tokens: int, overlap_tokens: int = 50, encoder_name: str = 'cl100k_base'
) -> list[tuple[str, int, int]]:
    """
    Splits text into chunks with token overlap for context preservation.
    Returns: List of (text_chunk, start_pos, end_pos) tuples.
    """
    token_ids = tokenize_text(text, encoder_name)
    chunks: list[tuple[str, int, int]] = []

    start_idx = 0
    while start_idx < len(token_ids):
        # Calculate end index with overlap
        end_idx = min(start_idx + max_tokens, len(token_ids))
        chunk_tokens = token_ids[start_idx:end_idx]

        # Get text and positions
        chunk_text = detokenize_text(chunk_tokens, encoder_name)
        text_start = len(detokenize_text(token_ids[:start_idx]))
        text_end = text_start + len(chunk_text)

        chunks.append((chunk_text, text_start, text_end))

        # Move to next chunk accounting for overlap
        start_idx = end_idx - overlap_tokens if end_idx < len(token_ids) else end_idx

    return chunks


# ------------
# Glossary Management
# ------------
async def process_glossary_terms(terms_file: Path | None, origin_language: str, target_language: str, model: str) -> list[dict[str, str]]:
    """
    Process and translate glossary terms from a JSON file.
    Expected format: [{"term": "term1", "context": "context1"}, ...]
    """
    if not terms_file or not terms_file.exists():
        logger.info("No glossary file provided or file doesn't exist")
        return []

    try:
        async with aiofiles.open(terms_file, encoding='utf-8') as f:
            content = await f.read()
            raw_terms = json.loads(content)

        # Transform terms into the expected format
        formatted_terms = [
            {'word': term['term'], 'context_before': term.get('context', ''), 'context_after': term.get('additional_context', '')}
            for term in raw_terms
        ]

        translated_terms = await translate_glossary_terms(
            terms=formatted_terms, origin_language=origin_language, target_language=target_language, model=model
        )

        logger.info(f'Processed {len(translated_terms)} glossary terms')
        return translated_terms

    except Exception as e:
        logger.error(f'Error processing glossary terms: {e}')
        return []


# ------------
# HTML Processing
# ------------
def extract_text_from_html(html_content: str) -> tuple[str, dict[int, tuple[str, str]]]:
    """
    Extracts text while preserving HTML tag positions and context.
    Returns: (plain_text, tag_positions)
    """
    soup = BeautifulSoup(html_content, 'lxml')
    text = ''
    tag_positions: dict[int, tuple[str, str]] = {}

    def process_node(node, current_pos: int) -> int:
        nonlocal text
        if isinstance(node, NavigableString):
            text += str(node)
            return current_pos + len(str(node))
        if isinstance(node, Tag):
            tag_positions[current_pos] = (str(node.name), 'open')
            for child in node.children:
                current_pos = process_node(child, current_pos)
            tag_positions[current_pos] = (str(node.name), 'close')
            return current_pos
        return current_pos

    process_node(soup, 0)
    return text, tag_positions


def reinsert_html_tags(translated_text: str, tag_positions: dict[int, tuple[str, str]]) -> str:
    """Reinserts HTML tags into translated text while maintaining structure."""
    result = ''
    current_pos = 0

    sorted_positions = sorted(tag_positions.items())

    for pos, (tag_name, tag_type) in sorted_positions:
        if pos > current_pos:
            result += translated_text[current_pos:pos]

        result += f'<{"" if tag_type == "close" else ""}{tag_name}>'
        current_pos = pos

    if current_pos < len(translated_text):
        result += translated_text[current_pos:]

    return result


# ------------
# Core Translation Functions
# ------------
async def process_segment(
    segment_text: tuple[str, int, int],
    original_html: str,
    model: str,
    origin_language: str,
    target_language: str,
    glossary: list[dict[str, str]] | None = None,
    context_window: int = 2000,
    log_path: Path | None = None,
) -> str:
    """Process single segment with surrounding context and glossary application."""
    try:
        text, start, end = segment_text

        # Extract context
        prefix = original_html[max(0, start - context_window) : start]
        suffix = original_html[end : min(len(original_html), end + context_window)]

        translated_text = await translate(
            text_to_be_translated=text,
            context_before=prefix,
            context_after=suffix,
            origin_language=origin_language,
            target_language=target_language,
            model=model,
        )

        if log_path:
            async with aiofiles.open(log_path, 'a') as f:
                await f.write(f'Segment translation:\nOriginal: {text}\nTranslated: {translated_text}\n\n')

        # Apply glossary terms if available
        if glossary:
            for term in glossary:
                if term.get('translation'):
                    translated_text = translated_text.replace(term['word'], term['translation'])

        return translated_text
    except Exception as e:
        logger.error(f'Segment processing error: {e}')
        return text


async def process_single_contract(
    contract_data: dict,
    model: str,
    origin_language: str,
    target_language: str,
    tokenizer: Any,
    log_path: Path,
    glossary: list[dict[str, str]] | None = None,
    max_chunk_tokens: int = 1000,
    overlap_tokens: int = 50,
) -> dict:
    """Process a single contract with enhanced chunking and HTML preservation."""
    try:
        original_html = contract_data['contracts']

        # Extract text and tag positions
        plain_text, tag_positions = extract_text_from_html(original_html)

        # Chunk the text while preserving token context
        chunks = chunk_text_by_tokens(plain_text, max_tokens=max_chunk_tokens, overlap_tokens=overlap_tokens)

        # Translate chunks
        translated_chunks = []
        for chunk in chunks:
            translated_chunk = await process_segment(
                segment_text=chunk,
                original_html=original_html,
                model=model,
                origin_language=origin_language,
                target_language=target_language,
                glossary=glossary,
                log_path=log_path,
            )
            translated_chunks.append(translated_chunk)

        # Combine translated chunks and reinsert HTML
        combined_translation = ''.join(translated_chunks)
        translated_html = reinsert_html_tags(combined_translation, tag_positions)

        # Update contract data
        contract_data['contratos'] = translated_html
        return contract_data

    except Exception as e:
        logger.error(f'Error processing contract: {e!s}')
        return contract_data


async def process_contracts_pipeline(
    input_jsonl_path: str,
    output_jsonl_path: str,
    model: str,
    origin_language: str,
    target_language: str,
    glossary_path: str | None = None,
) -> None:
    """Main pipeline function with glossary support."""
    try:
        # Initialize tokenizer
        tokenizer = tiktoken.get_encoding('cl100k_base')

        # Create output directory
        output_path = Path(output_jsonl_path).parent
        output_path.mkdir(parents=True, exist_ok=True)

        # Setup logging
        log_path = output_path / 'translation_log.txt'

        # Process glossary if provided
        glossary = None
        if glossary_path:
            glossary = await process_glossary_terms(Path(glossary_path), origin_language, target_language, model)

        # Read and process contracts
        async with aiofiles.open(input_jsonl_path, encoding='utf-8') as fin:
            lines = [json.loads(line) for line in await fin.readlines() if line.strip()]

        # Process each contract
        for contract in lines:
            try:
                result = await process_single_contract(
                    contract_data=contract,
                    model=model,
                    origin_language=origin_language,
                    target_language=target_language,
                    tokenizer=tokenizer,
                    log_path=log_path,
                    glossary=glossary,
                )

                # Save result
                async with aiofiles.open(output_jsonl_path, 'a', encoding='utf-8') as fout:
                    await fout.write(json.dumps(result, ensure_ascii=False) + '\n')

                await asyncio.sleep(0.1)  # Rate limiting

            except Exception as e:
                logger.error(f'Contract processing error: {e!s}')
                error_result = {'contracts': contract.get('contracts', ''), 'error': str(e)}
                async with aiofiles.open(output_jsonl_path, 'a', encoding='utf-8') as fout:
                    await fout.write(json.dumps(error_result, ensure_ascii=False) + '\n')

    except Exception as e:
        logger.error(f'Pipeline error: {e!s}')
        raise


# ------------
# CLI Interface
# ------------
@app.command()
def main(
    input_file: Path = typer.Option(
        'input.jsonl',
        '--input',
        '-i',
        help='Input JSONL file containing contracts to translate',
    ),
    output_file: Path = typer.Option(
        'output.jsonl',
        '--output',
        '-o',
        help='Output JSONL file for translated contracts',
    ),
    origin_language: str = typer.Option(
        'American English',
        '--origin-lang',
        '-ol',
        help='Origin language code',
    ),
    target_language: str = typer.Option(
        'Brazilian Portuguese',
        '--target-lang',
        '-tl',
        help='Target language code',
    ),
    model: str = typer.Option(
        'gemini-2.0-flash',
        '--model',
        '-m',
        help='Google Generative AI model to use',
    ),
    glossary_file: Path | None = typer.Option(
        None,
        '--glossary',
        '-g',
        help='Optional JSON file containing glossary terms',
    ),
):
    """Translate contracts from JSONL using Google's Generative AI with optional glossary support."""
    try:
        if not input_file.exists():
            console.print(f'[red]Error: Input file {input_file} does not exist[/]')
            raise typer.Exit(1)

        asyncio.run(
            process_contracts_pipeline(
                input_jsonl_path=str(input_file),
                output_jsonl_path=str(output_file),
                model=model,
                origin_language=origin_language,
                target_language=target_language,
                glossary_path=str(glossary_file) if glossary_file else None,
            )
        )

        console.print('\n[green]✨ Translation completed successfully![/]')

    except Exception as e:
        console.print(f'\n[red]Error: {e!s}[/]')
        raise typer.Exit(1)


if __name__ == '__main__':
    app()
