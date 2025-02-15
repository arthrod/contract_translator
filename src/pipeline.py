#!/usr/bin/env python3
# pipeline.py

import asyncio
import json
import re
from dataclasses import dataclass
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


@dataclass
class ProcessedTerm:
    word: str
    context_before: str
    context_after: str
    translation: str | None = None


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
    Expected format: [{"term": "term1", "context": "context1", "additional_context": "extra1"}, ...]
    """
    if not terms_file or not terms_file.exists():
        logger.info("No glossary file provided or file doesn't exist")
        return []

    try:
        async with aiofiles.open(terms_file, encoding='utf-8') as f:
            content = await f.read()
            raw_terms = json.loads(content)

        # Validate and format terms
        formatted_terms = []
        for term in raw_terms:
            if not isinstance(term, dict) or 'term' not in term:
                logger.warning(f'Skipping invalid glossary entry: {term}')
                continue
            formatted_terms.append(
                ProcessedTerm(
                    word=term['term'],
                    context_before=term.get('context', ''),
                    context_after=term.get('additional_context', ''),
                )
            )

        # Translate terms
        translated_terms = await translate_glossary_terms(
            terms=[
                {'word': term.word, 'context_before': term.context_before, 'context_after': term.context_after} for term in formatted_terms
            ],
            origin_language=origin_language,
            target_language=target_language,
            model=model,
        )

        # Update translations
        for term, translated in zip(formatted_terms, translated_terms):
            if isinstance(translated, dict) and 'translation' in translated:
                term.translation = translated['translation']
            else:
                logger.warning(f'Failed to get translation for term: {term.word}')

        logger.info(f'Processed {len(formatted_terms)} glossary terms')
        return formatted_terms

    except Exception as e:
        logger.error(f'Error processing glossary terms: {e}')
        return []


# ------------
# HTML Processing
# ------------
def extract_text_from_html(html_content: str) -> tuple[str, dict[int, tuple[str, dict[str, str]]]]:
    """
    Enhanced text extraction that preserves HTML structure and attributes.

    Returns:
        tuple containing:
        - Plain text with tags removed
        - Dictionary mapping positions to (tag_name, attributes) tuples
    """
    soup = BeautifulSoup(html_content, 'lxml')
    text = ''
    tag_positions: dict[int, tuple[str, dict[str, str]]] = {}

    def process_node(node, current_pos: int) -> int:
        nonlocal text
        if isinstance(node, NavigableString):
            # Skip ```html markers
            content = str(node)
            if '```html' not in content:
                text += content
                return current_pos + len(content)
            return current_pos

        if isinstance(node, Tag):
            # Store tag with all attributes
            attrs = dict(node.attrs) if node.attrs else {}
            tag_positions[current_pos] = (str(node.name), {'type': 'open', 'attrs': attrs})

            for child in node.children:
                current_pos = process_node(child, current_pos)

            # Store closing tag
            tag_positions[current_pos] = (str(node.name), {'type': 'close'})

        return current_pos

    process_node(soup, 0)
    return text, tag_positions


def reinsert_html_tags(translated_text: str, tag_positions: dict[int, tuple[str, dict[str, str]]]) -> str:
    """
    Reinserts HTML tags with enhanced position tracking and attribute preservation.
    """
    result = []
    current_pos = 0
    text_length = len(translated_text)

    # Sort positions to ensure proper tag ordering
    sorted_positions = sorted(tag_positions.items())

    for pos, (tag_name, tag_info) in sorted_positions:
        # Add text content before tag
        if pos > current_pos and current_pos < text_length:
            result.append(translated_text[current_pos:pos])

        # Construct tag with attributes
        if tag_info['type'] == 'close':
            result.append(f'</{tag_name}>')
        else:
            attrs = tag_info.get('attrs', {})
            attr_str = ' '.join(f'{k}="{v}"' for k, v in attrs.items())
            result.append(f'<{tag_name}{" " + attr_str if attr_str else ""}>')

        current_pos = pos

    # Add remaining text
    if current_pos < text_length:
        result.append(translated_text[current_pos:])

    return ''.join(result)


def clean_translated_html(html_content: str) -> str:
    """
    Cleans translated HTML by removing ```html markers and fixing common issues.
    """
    # Remove ```html markers
    cleaned = re.sub(r'```html\n?', '', html_content)
    cleaned = re.sub(r'\n?```', '', cleaned)

    # Fix common translation artifacts
    cleaned = re.sub(r'&lt;', '<', cleaned)
    cleaned = re.sub(r'&gt;', '>', cleaned)

    # Normalize whitespace around tags
    cleaned = re.sub(r'\s+(?=</)', '', cleaned)  # Remove space before closing tags
    cleaned = re.sub(r'>\s+', '> ', cleaned)  # Normalize space after tags
    cleaned = re.sub(r'\s+<', ' <', cleaned)  # Normalize space before tags

    return cleaned.strip()


# ------------
# Core Translation Functions
# ------------
async def process_segment(
    segment_text: tuple[str, int, int],
    original_html: str,
    model: str,
    origin_language: str,
    target_language: str,
    glossary: list[ProcessedTerm] | None = None,
    context_window: int = 2000,
    log_path: Path | None = None,
) -> str:
    """Process single segment with surrounding context and glossary application."""
    try:
        text, start, end = segment_text

        # Don't process empty segments
        if not text.strip():
            return text

        # Extract context with proper text content
        prefix = original_html[max(0, start - context_window) : start].strip()
        suffix = original_html[end : min(len(original_html), end + context_window)].strip()

        # Prepare glossary context for translation
        glossary_context = None
        if glossary:
            glossary_context = [
                {'term': term.word, 'translation': term.translation, 'context': f'{term.context_before} {term.context_after}'.strip()}
                for term in glossary
                if term.translation
            ]

        # Only attempt translation if we have actual text to translate
        if text.strip():
            translated_text = await translate(
                text_to_be_translated=text.strip(),
                context_before=prefix if prefix else None,
                context_after=suffix if suffix else None,
                origin_language=origin_language,
                target_language=target_language,
                model=model,
                glossary_terms=glossary_context,
            )

            if log_path:
                async with aiofiles.open(log_path, 'a') as f:
                    await f.write(f'Segment translation:\nOriginal: {text}\nTranslated: {translated_text}\n\n')

            # Apply glossary terms with context awareness
            if glossary:
                translated_text = apply_glossary_terms(translated_text, glossary)

            return translated_text

        return text

    except Exception as e:
        logger.error(f'Segment processing error: {e}')
        return text


def apply_glossary_terms(text: str, glossary: list[ProcessedTerm]) -> str:
    """Apply translated glossary terms to the text with context awareness."""
    if not glossary:
        return text

    processed_text = text
    for term in glossary:
        if term.translation:
            # Create a context-aware replacement using regex
            if term.context_before and term.context_after:
                pattern = re.compile(
                    rf'(?<!\w){re.escape(term.context_before)}\s*?{re.escape(term.word)}\s*?{re.escape(term.context_after)}(?!\w)',
                    re.IGNORECASE,
                )
                processed_text = pattern.sub(f'{term.context_before} {term.translation} {term.context_after}', processed_text)

            else:
                pattern = re.compile(rf'(?<!\w){re.escape(term.word)}(?!\w)', re.IGNORECASE)
                processed_text = pattern.sub(term.translation, processed_text)

    return processed_text


async def process_contracts_pipeline(
    input_jsonl_path: str,
    output_jsonl_path: str,
    model: str,
    origin_language: str,
    target_language: str,
    glossary_path: str | None = None,
) -> None:
    """Main pipeline function with glossary support and enhanced contract preservation."""
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
                # Validate contract has content to translate
                if not contract.get('contracts', '').strip():
                    logger.warning(f'Empty contract found, skipping: {contract}')
                    continue

                # Store original contract structure
                original_contract = contract.copy()

                result = await process_single_contract(
                    contract_data=contract,
                    model=model,
                    origin_language=origin_language,
                    target_language=target_language,
                    tokenizer=tokenizer,
                    log_path=log_path,
                    glossary=glossary,
                )

                # Preserve original structure while adding translation
                full_result = original_contract.copy()
                full_result['contratos'] = result.get('contratos', '')

                # Save result
                async with aiofiles.open(output_jsonl_path, 'a', encoding='utf-8') as fout:
                    await fout.write(json.dumps(full_result, ensure_ascii=False) + '\n')

                await asyncio.sleep(0.1)  # Rate limiting

            except Exception as e:
                logger.error(f'Contract processing error: {e!s}')
                error_result = original_contract.copy()
                error_result['error'] = str(e)
                async with aiofiles.open(output_jsonl_path, 'a', encoding='utf-8') as fout:
                    await fout.write(json.dumps(error_result, ensure_ascii=False) + '\n')

    except Exception as e:
        logger.error(f'Pipeline error: {e!s}')
        raise


async def process_single_contract(
    contract_data: dict,
    model: str,
    origin_language: str,
    target_language: str,
    tokenizer: Any,
    log_path: Path,
    glossary: list[ProcessedTerm] | None = None,
    max_chunk_tokens: int = 1000,
    overlap_tokens: int = 50,
) -> dict:
    """Enhanced contract processing with improved HTML handling."""
    try:
        original_html = contract_data['contracts']

        # Validate content
        if not original_html or not original_html.strip():
            logger.warning('Empty contract content, returning original')
            return contract_data

        # Extract text and tag positions with enhanced tracking
        plain_text, tag_positions = extract_text_from_html(original_html)

        # Chunk text while preserving structure
        chunks = chunk_text_by_tokens(plain_text, max_tokens=max_chunk_tokens, overlap_tokens=overlap_tokens)

        # Translate non-empty chunks
        translated_chunks = []
        for chunk in chunks:
            if chunk[0].strip():
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
            else:
                translated_chunks.append(chunk[0])

        # Combine translations and reinsert HTML
        combined_translation = ''.join(translated_chunks)
        translated_html = reinsert_html_tags(combined_translation, tag_positions)

        # Clean and normalize the translated HTML
        cleaned_html = clean_translated_html(translated_html)

        # Create result maintaining original structure
        result = contract_data.copy()
        result['contratos'] = cleaned_html
        return result

    except Exception as e:
        logger.error(f'Error processing contract: {e!s}')
        return contract_data


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
