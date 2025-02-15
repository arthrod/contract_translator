"""
Comprehensive real-world tests for translator.py
WARNING: Requires GEMINI_API_KEY environment variable
         These make REAL API calls - run with caution
"""

import asyncio

# Configure logging
import os

import pytest
from loguru import logger

from src.translator import translate, translate_glossary_terms

# Configure logger to write to both console and file
logger.add('translation_test.log', rotation='500 MB', level='INFO')

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')


# --- Core Configuration ---
TEST_TIMEOUT = 30  # Seconds per test case
MAX_CONCURRENT = 3  # Parallel test executions


# --- Test Cases for translate() ---
TRANSLATE_CASES = [
    # (text, context_before, context_after, source_lang, target_lang)
    ('Hello world', None, None, 'en', 'es'),
    ('Important deadline: Friday', 'The contract states', 'must be respected', 'en', 'pt'),
    ('', 'Previous paragraph', 'Next paragraph', 'auto', 'fr'),  # Empty text
    ('12345', None, None, 'en', 'de'),  # Numbers
    (' 2024 Company Name', None, None, 'en', 'ja'),  # Special characters
    ('New line\ntest', 'Header', 'Footer', 'en', 'es'),
    ('<html>Test</html>', None, None, 'en', 'zh'),  # HTML content
    ('Long text ' * 50, 'Context start', 'Context end', 'en', 'it'),  # Bulk text
    ('Technical term: quantum computing', 'In physics:', None, 'en', 'de'),
    ("Idiom: 'Break a leg'", None, 'used in theater', 'en', 'es'),
    ('term', 'This legal', 'is binding', 'en', 'es'),  # Context changes meaning
    ('right', 'You have the', 'to remain silent', 'en', 'pt'),  # Legal context
    ('present', 'I hereby', 'the evidence', 'en', 'fr'),  # Formal context
    ('fine', 'You will be charged a', 'of $500', 'en', 'de'),  # Financial context
    ('party', 'The first', 'agrees to terms', 'en', 'it'),  # Legal party
    ('execution', 'Contract', 'date', 'en', 'es'),  # Legal execution
    ('subject', 'Email', 'line', 'en', 'pt'),  # Email context
    ('address', 'Please', 'the concerns', 'en', 'fr'),  # Verb vs noun
    ('close', 'Please', 'the account', 'en', 'de'),  # Action context
    ('interest', 'Bank', 'rate', 'en', 'it'),  # Financial context
    (
        """CONFIDENTIALITY AND NON-DISCLOSURE AGREEMENT

    THIS CONFIDENTIALITY AND NON-DISCLOSURE AGREEMENT (the "Agreement") is entered into as of [DATE] by and between [COMPANY NAME], a corporation organized and existing under the laws of [STATE/COUNTRY], with its principal place of business at [ADDRESS] ("Disclosing Party"), and [RECIPIENT NAME], with its principal place of business at [ADDRESS] ("Receiving Party").

    WHEREAS, the Disclosing Party possesses certain confidential and proprietary information relating to its business, operations, products, services, and intellectual property; and

    WHEREAS, the Receiving Party desires to receive and the Disclosing Party is willing to disclose such confidential information for the purpose of [SPECIFY PURPOSE].

    NOW, THEREFORE, in consideration of the mutual covenants and agreements contained herein, and other good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, the parties agree as follows:""",
        'IMPORTANT LEGAL DOCUMENT',
        'The following sections detail the terms of confidentiality.',
        'en',
        'pt-br',
    ),
    (
        """1. DEFINITION OF CONFIDENTIAL INFORMATION
    "Confidential Information" means any and all non-public, confidential, or proprietary information disclosed by the Disclosing Party to the Receiving Party, whether orally, visually, in writing, electronically, or in any other form or medium, including but not limited to:
    (a) trade secrets, know-how, processes, procedures, methodologies, techniques, and protocols;
    (b) business strategies, plans, and forecasts;
    (c) customer lists, pricing data, and market analyses;
    (d) research and development information, technical specifications, and product designs;
    (e) financial information, budgets, and projections;
    (f) employee, contractor, and supplier information; and
    (g) any other information that should reasonably be recognized as confidential information of the Disclosing Party.""",
        'This section defines what constitutes confidential information under this agreement.',
        'The next section covers the obligations of the receiving party.',
        'en',
        'pt-br',
    ),
    (
        """2. OBLIGATIONS OF RECEIVING PARTY
    The Receiving Party agrees to:
    (a) maintain the confidentiality of all Confidential Information;
    (b) use the Confidential Information solely for the Purpose;
    (c) not disclose any Confidential Information to any third party without prior written consent;
    (d) limit access to Confidential Information to employees, agents, or representatives who have a need to know;
    (e) inform all persons having access to Confidential Information of its confidential nature;
    (f) protect Confidential Information with at least the same degree of care used to protect its own confidential information;
    (g) notify the Disclosing Party immediately upon discovery of any unauthorized use or disclosure; and
    (h) return or destroy all Confidential Information upon request or termination of this Agreement.""",
        'Previous section defined confidential information.',
        'The next section covers exceptions to confidentiality.',
        'en',
        'pt-br',
    ),
    (
        """3. TERM AND TERMINATION
    This Agreement shall commence on the Effective Date and shall remain in effect for a period of [NUMBER] years thereafter, unless terminated earlier by mutual written agreement of the parties. Notwithstanding such termination, all obligations of the Receiving Party with respect to the use and disclosure of Confidential Information shall survive and continue for a period of [NUMBER] years after termination or expiration of this Agreement.

    4. REMEDIES
    The Receiving Party acknowledges that any breach of this Agreement may cause irreparable harm to the Disclosing Party for which monetary damages would be inadequate. Accordingly, the Disclosing Party shall be entitled to seek injunctive or other equitable relief to prevent or curtail any breach of this Agreement, without the necessity of posting a bond or other security.""",
        'The previous sections covered confidentiality obligations.',
        'The final section will cover governing law.',
        'en',
        'pt-br',
    ),
    (
        """5. GOVERNING LAW AND JURISDICTION
    This Agreement shall be governed by and construed in accordance with the laws of [STATE/COUNTRY], without regard to its conflicts of law principles. Any dispute arising out of or relating to this Agreement shall be subject to the exclusive jurisdiction of the courts of [STATE/COUNTRY], and the parties hereby consent to the personal jurisdiction of such courts.

    IN WITNESS WHEREOF, the parties have executed this Confidentiality and Non-Disclosure Agreement as of the date first above written.

    [COMPANY NAME]
    By: ____________________
    Name: __________________
    Title: ___________________

    [RECIPIENT NAME]
    By: ____________________
    Name: __________________
    Title: ___________________""",
        'This is the final section of the agreement.',
        'Signatures will follow below.',
        'en',
        'pt-br',
    ),
    # Additional complex legal clauses
    (
        """FORCE MAJEURE CLAUSE
    Neither party shall be liable for any failure to perform its obligations under this Agreement if such failure results from circumstances beyond its reasonable control, including but not limited to acts of God, war, civil unrest, labor disputes, government actions, pandemics, epidemics, natural disasters, fire, flood, or other catastrophes. The affected party shall promptly notify the other party of the force majeure event and its expected duration. If the force majeure event continues for more than [NUMBER] days, either party may terminate this Agreement upon written notice to the other party.""",
        'Standard contract clause for unforeseen circumstances.',
        'This clause protects both parties from extraordinary events.',
        'en',
        'pt-br',
    ),
    (
        """INTELLECTUAL PROPERTY RIGHTS
    All rights, title, and interest in and to any Confidential Information, including all intellectual property rights therein, shall remain the exclusive property of the Disclosing Party. Nothing in this Agreement shall be construed as granting any rights, license, or authorization to the Receiving Party with respect to the Confidential Information, except for the limited purpose set forth in this Agreement. The Receiving Party shall not reverse engineer, decompile, or disassemble any products, prototypes, software, or other tangible objects embodying the Confidential Information.""",
        'This section protects intellectual property.',
        'Following sections cover additional protections.',
        'en',
        'pt-br',
    ),
]


# --- Test Cases for translate_glossary_terms() ---
GLOSSARY_CASES = [
    [
        {'word': 'Force Majeure', 'context_before': 'In case of', 'context_after': 'events'},
        {'word': 'Lump sum', 'context_after': 'payment terms'},
    ],
    [{'word': 'Confidentiality', 'context_before': 'Article 5:'}, {'word': 'Arbitration', 'context_after': 'clause'}],
    [{'word': '', 'context_before': 'Amount:'}],  # Currency symbol
    [{'word': 'COVID-19', 'context_after': 'pandemic related'}],  # Modern term
    [{'word': 'Party A'}, {'word': 'Party B'}, {'word': 'Effective Date'}],  # Multiple simple terms
    [{'word': ' ' * 10}],  # Whitespace term
    [{'word': '1.2.3', 'context_before': 'Version'}],  # Version number
    [{'word': 'Herr', 'context_before': 'German title'}, {'word': 'Sehr geehrte', 'context_after': 'letter opening'}],  # Non-English source
    [{'word': '🤝', 'context_before': 'Agreement symbol'}],  # Emoji
    [{'word': 'Lorem ipsum', 'context_after': 'placeholder text'}],  # Placeholder
]


# --- Test Implementation ---
class TestRealWorldTranslations:
    """Test suite making real API calls to Gemini"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize('text,ctx_before,ctx_after,src_lang,tgt_lang', TRANSLATE_CASES)
    async def test_translate_variations(self, text, ctx_before, ctx_after, src_lang, tgt_lang):
        """Test translate() with diverse real-world scenarios, running each test 5 times"""
        results = []

        # Log test case details
        logger.info('\n' + '=' * 80)
        logger.info('Starting new test case')
        logger.info('Text to translate:')
        logger.info(text)  # Log full text
        logger.info(f'\nContext before: {ctx_before}')
        logger.info(f'Context after: {ctx_after}')
        logger.info(f'Source language: {src_lang}')
        logger.info(f'Target language: {tgt_lang}')
        logger.info('=' * 80 + '\n')

        for i in range(5):  # Run each test 5 times
            try:
                logger.info(f'\n=== Test Run {i + 1} ===')
                result = await asyncio.wait_for(
                    translate(
                        text_to_be_translated=text,
                        context_before=ctx_before,
                        context_after=ctx_after,
                        origin_language=src_lang,
                        target_language=tgt_lang,
                        concurrent_attempts=MAX_CONCURRENT,
                    ),
                    timeout=TEST_TIMEOUT,
                )
                await asyncio.sleep(0.1)
                assert result and isinstance(result, str)
                logger.info(f'Run {i + 1} - Translation successful')
                logger.info('\nOriginal text:')
                logger.info(text)
                logger.info('\nTranslated text:')
                logger.info(result)
                logger.info('=' * 80)
                results.append(result)

            except Exception as e:
                logger.error(f'Run {i + 1} - Translation failed: {e!s}')
                results.append(None)

            await asyncio.sleep(0.5)  # Small delay between runs

        # Log summary of all runs
        logger.info('\n=== Summary of all runs ===')
        logger.info('Original text:')
        logger.info(text)
        logger.info(f'\nContext Before: {ctx_before}')
        logger.info(f'Context After: {ctx_after}')
        for i, result in enumerate(results, 1):
            logger.info(f'\nRun {i} Result:')
            if result:
                logger.info(result)
            else:
                logger.info('Failed')
        logger.info('=' * 80)

    @pytest.mark.asyncio
    @pytest.mark.parametrize('terms', GLOSSARY_CASES)
    async def test_glossary_translations(self, terms):
        """Test glossary term translation with varied inputs"""
        try:
            results = await asyncio.wait_for(
                translate_glossary_terms(
                    terms=terms,
                    target_language='es',  # Standardizing for consistency
                    max_retries=2,
                ),
                timeout=TEST_TIMEOUT,
            )
            await asyncio.sleep(0.1)
            # Validate response structure
            assert isinstance(results, list), 'Results must be list'
            for item in results:
                assert 'term' in item, 'Missing original term'
                assert 'translation' in item, 'Missing translation'
                assert item['translation'].strip() != '', 'Empty translation'

            logger.info(f'Translated {len(terms)} terms successfully')

        except Exception as e:
            logger.error(f'Glossary test failed: {e!s}')
            if 'API_KEY' in str(e):
                pytest.fail('Missing GEMINI_API_KEY environment variable')
            elif 'quota' in str(e).lower():
                pytest.skip('API quota exceeded')
            elif 'unavailable' in str(e).lower():
                pytest.skip('API service unavailable')


if __name__ == '__main__':
    # For direct execution without pytest
    async def main():
        tester = TestRealWorldTranslations()
        for case in TRANSLATE_CASES:
            await tester.test_translate_variations(*case)
        for terms in GLOSSARY_CASES:
            await tester.test_glossary_translations(terms)

    asyncio.run(main())
