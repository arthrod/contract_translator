"""
Translation modules providing context-aware translation capabilities:
1. translate: For single-chunk translation with context
2. translate_glossary_terms: For consistent term translation with context
"""

import asyncio
import os

import loguru
from dotenv import load_dotenv
from google import genai
from google.genai import types

logger = loguru.logger


load_dotenv()


async def translate(
    text_to_be_translated: str,
    context_before: str | None = None,
    context_after: str | None = None,
    origin_language: str | None = None,
    target_language: str | None = None,
    model: str = 'gemini-2.0-flash',
    max_retries: int = 100,
    concurrent_attempts: int = 1,
) -> str:
    """
    Translate text using Gemini API with context awareness and robust error handling.

    Args:
        text_to_be_translated: Text to translate
        context_before: Text appearing before the translation target
        context_after: Text appearing after the translation target
        origin_language: Source language (auto-detect if None)
        target_language: Target language (defaults to English if None)
        model: Gemini model to use (default: gemini-2.0-flash)
        max_retries: Maximum retry attempts per task
        concurrent_attempts: Number of concurrent translation attempts

    Returns:
        Translated text string

    Raises:
        RuntimeError: If all translation attempts fail
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError('GEMINI_API_KEY environment variable is required')

    client = genai.Client(api_key=api_key)

    async def single_translation_attempt() -> str | None:
        retry_count = 0

        while retry_count < max_retries:
            try:
                prompt = f"""
                Translate the following text from {origin_language or 'auto-detect'} to {target_language or 'English'}.
                The text to translate is wrapped in XML-style tags. Context is provided for accuracy but should not be translated.

                {f'<context_before>{context_before}</context_before>' if context_before else ''}
                <text_to_translate>{text_to_be_translated}</text_to_translate>
                {f'<context_after>{context_after}</context_after>' if context_after else ''}

                Requirements:
                - Translate ONLY the text between <text_to_translate> tags
                - Use surrounding context to ensure accurate meaning and tone
                - Preserve all formatting and special characters
                - Maintain document style and formality level
                - Return only the translated text
                """

                logger.info(f'\n=== Translation Attempt {retry_count + 1} ===')
                logger.info(f'Input Text: {text_to_be_translated}')
                logger.info(f'Context Before: {context_before}')
                logger.info(f'Context After: {context_after}')
                logger.info(f'Source Language: {origin_language}')
                logger.info(f'Target Language: {target_language}')
                logger.info(f'Full Prompt:\n{prompt}')

                response = await client.aio.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                # Log full API response
                logger.info('=== API Response ===')
                logger.info(f'Response object: {response}')
                logger.info(f'Candidates: {response.candidates}')
                if response.candidates:
                    logger.info(f'First candidate: {response.candidates[0]}')
                    if response.candidates[0].content:
                        logger.info(f'Content: {response.candidates[0].content}')
                        logger.info(f'Parts: {response.candidates[0].content.parts}')
                logger.info('=' * 80)

                if not response.candidates or not response.candidates[0].content:
                    logger.warning(f'Empty response on attempt {retry_count + 1}')
                    retry_count += 1
                    await asyncio.sleep(0.1 * retry_count)
                    continue

                result = response.candidates[0].content.parts[0].text
                logger.info('=== Translation Result ===')
                logger.info('Original:')
                logger.info(text_to_be_translated)
                logger.info('\nTranslated:')
                logger.info(result)
                logger.info('=' * 80)
                return result

            except Exception as e:
                logger.warning(f'Translation attempt {retry_count + 1} failed: {e}')
                retry_count += 1
                await asyncio.sleep(0.1 * retry_count)

        return None

    if concurrent_attempts > 1:
        tasks = [asyncio.create_task(single_translation_attempt()) for _ in range(concurrent_attempts)]

        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        for task in pending:
            task.cancel()

        for completed_task in done:
            try:
                result = completed_task.result()
                if result:
                    return result
            except Exception as e:
                logger.warning(f'Task failed: {e}')
                continue
    else:
        result = await single_translation_attempt()
        if result:
            return result

    raise RuntimeError('All translation attempts failed')


async def translate_glossary_terms(
    terms: list[dict[str, str]],
    origin_language: str | None = None,
    target_language: str | None = None,
    model: str = 'gemini-2.0-flash',
    max_retries: int = 100,
) -> list[dict[str, str]]:
    """
    Translate a list of glossary terms with context awareness.

    Args:
        terms: List of dictionaries, each containing:
            {
                "word": str,              # Required
                "context_before": str,     # Optional
                "context_after": str      # Optional
            }
        api_key: Google AI API key for authentication
        target_language: Target language (defaults to English if None)
        model: Gemini model to use (default: gemini-2.0-flash)
        max_retries: Maximum retry attempts per task
        concurrent_attempts: Number of concurrent translation attempts

    Returns:
        List of dictionaries containing:
        [
            {
                "term": str,
                "translation": str,
                "context_notes": str,
                "alternative_translations": [
                    {
                        "translation": str,
                        "usage_context": str
                    }
                ]
            }
        ]

    Raises:
        ValueError: If no valid terms are provided
        RuntimeError: If all translation attempts fail
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError('GEMINI_API_KEY environment variable is required')

    client = genai.Client(api_key=api_key)
    retry_count = 0

    while retry_count < max_retries:
        try:
            formatted_terms = []
            for term in terms:
                if not isinstance(term, dict) or 'word' not in term:
                    logger.warning(f'Invalid term format: {term}')
                    continue

                formatted_terms.append(
                    {'word': term['word'], 'context_before': term.get('context_before'), 'context_after': term.get('context_after')}
                )

            if not formatted_terms:
                raise ValueError('No valid terms provided')

            prompt = f"""
            These are common terms of an agreement, which
            can be definitions or not. They will used to make 
            sure our translation is accurate and consistent. 
            The original language is {origin_language or 'American English'}. Translate the following terms to {
                target_language or 'Brazilian Portuguese'
            }, maintaining consistency
            and considering provided context. Each term is marked with XML-style tags.

            Terms to translate:

            {
                chr(10).join(
                    f'''
            Term {i + 1}:
            {f'<context_before>{term["context_before"]}</context_before>' if term.get('context_before') else ''}
            <word_to_translate>{term['word']}</word_to_translate>
            {f'<context_after>{term["context_after"]}</context_after>' if term.get('context_after') else ''}
            '''
                    for i, term in enumerate(formatted_terms)
                )
            }

            Requirements:
            - Provide primary translation for each term
            - Consider context for accuracy
            - Note any context-specific usage guidance
            - Suggest alternatives only if context indicates multiple valid translations
            - Return a structured response for each term
            """

            response = await client.aio.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    response_mime_type='application/json',
                    response_schema={
                        'type': 'OBJECT',
                        'properties': {
                            'translations': {
                                'type': 'ARRAY',
                                'items': {
                                    'type': 'OBJECT',
                                    'properties': {
                                        'term': {'type': 'STRING'},
                                        'translation': {'type': 'STRING'},
                                        'context_notes': {'type': 'STRING'},
                                        'alternative_translations': {
                                            'type': 'ARRAY',
                                            'items': {
                                                'type': 'OBJECT',
                                                'properties': {'translation': {'type': 'STRING'}, 'usage_context': {'type': 'STRING'}},
                                            },
                                        },
                                    },
                                    'required': ['term', 'translation'],
                                },
                            }
                        },
                        'required': ['translations'],
                    },
                ),
            )

            # Log full API response
            logger.info('=== API Response ===')
            logger.info(f'Response object: {response}')
            logger.info(f'Candidates: {response.candidates}')
            if response.candidates:
                logger.info(f'First candidate: {response.candidates[0]}')
                if response.candidates[0].content:
                    logger.info(f'Content: {response.candidates[0].content}')
                    logger.info(f'Parsed: {response.parsed}')
            logger.info('=' * 80)

            if not response.candidates or not response.candidates[0].content:
                logger.warning(f'Empty response on attempt {retry_count + 1}')
                retry_count += 1
                await asyncio.sleep(0.1 * retry_count)
                continue

            return response.parsed['translations']

        except Exception as e:
            logger.warning(f'Translation attempt {retry_count + 1} failed: {e}')
            retry_count += 1
            await asyncio.sleep(0.1 * retry_count)

    raise RuntimeError('All translation attempts failed')
