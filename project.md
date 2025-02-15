Below is a fully worked-out Python implementation demonstrating how to build a modular pipeline for translating legal contracts from English to Brazilian Portuguese (pt-BR) using Google’s Gemini LLM in a majority vote approach. It also shows how to extract frequently used legal terms with LexNLP, let a user review those terms, enforce consistent translations of those terms, and finally output translated contracts in JSONL.

Important Note:

Google’s Gemini API is not publicly available at the time of writing. The GeminiTranslator class below includes placeholder logic showing how you would structure calls to a hypothetical Gemini API. Replace with your actual calls to Vertex AI or other Google endpoints once the API is published.
Some pieces (e.g., user review of terms) are demonstrated in code comments or placeholders. In a real system, you might store the glossary in a file or present it in a simple CLI/GUI for a human to edit.
This code is designed for illustration and may need adjustments (error handling, environment variables, concurrency limits, etc.) for production-scale usage.
Directory/Project Structure
Below is an example project layout. You can store these classes in separate .py files if you prefer. For simplicity, the entire pipeline is in one file here, with distinct classes and sections.

graphql
Copy
legal_translation_pipeline/
├── pipeline.py  # Put the code below here
├── requirements.txt
└── input.jsonl   # Example input

requirements.txt (example):

nginx
Copy
beautifulsoup4
lexnlp
requests
lxml
tqdm
(Add or remove dependencies as needed.)

python
Copy
#!/usr/bin/env python3
# pipeline.py

import json
import os
import re
from collections import Counter, defaultdict
from typing import List, Dict, Tuple

import lexnlp.nlp.en.tokens as lexnlp_tokens
import lexnlp.nlp.en.stopwords as lexnlp_stopwords
from bs4 import BeautifulSoup

# If using concurrency
from concurrent.futures import ThreadPoolExecutor, as_completed

# ------------
# 1) BACKEND: GEMINI TRANSLATOR (Placeholder)
# ------------
class GeminiTranslator:
    """
    A plug-and-play backend class for interacting with Google’s Gemini LLM.
    This is a mock-up to illustrate the usage. Replace the 'translate_text'
    method with real calls to Vertex AI or Gemini once available.
    """

    def __init__(self, project_id: str, location: str, model_id: str, credential_file: str):
        """
        :param project_id: Google Cloud project ID
        :param location: e.g. 'us-central1'
        :param model_id: e.g. 'models/gemini-translator'
        :param credential_file: path to GCP service account or user credentials
        """
        self.project_id = project_id
        self.location = location
        self.model_id = model_id
        self.credential_file = credential_file
        # Normally you'd initialize a Vertex AI client here.
        # e.g. self.client = some_gcp_sdk.Client(...)
        # For now, this is a stub.

    def translate_text(self, text: str, source_lang: str, target_lang: str, temperature: float = 0.2) -> str:
        """
        Hypothetical translation method calling Gemini. 
        In reality, you'd use something like:
          response = self.client.predict(text, source_lang, target_lang, model=self.model_id, temperature=temperature)
        For demonstration, we'll just simulate a 'fake' translation.
        """
        # Here you would do the real request to the Gemini endpoint.
        # For demonstration, let's pretend it returns the text reversed 
        # (or we can do a fake substitution) so we can see it's changing something.
        # Obviously you must replace with actual LLM translation logic.

        # SIMULATED TRANSLATION:
        # (You'd remove this in production and call the actual API.)
        fake_translation = f"[{target_lang} translation of: {text[:50]}...]"
        return fake_translation

    def translate_text_batch(
        self, 
        texts: List[str], 
        source_lang: str, 
        target_lang: str, 
        temperature: float = 0.2
    ) -> List[str]:
        """
        Batch version: translates a list of texts. 
        In a real system, you'd send them in a single request (if the API supports it) 
        or do parallel calls. We'll just map `translate_text` for now.
        """
        # In production, try to do fewer calls by grouping texts 
        # into a single request if the API allows.
        return [self.translate_text(t, source_lang, target_lang, temperature) for t in texts]

# ------------
# 2) LANGUAGE SELECTION
# ------------
class LanguageSelector:
    """
    Manages source/target languages. 
    For demonstration, we only handle English (en) -> Portuguese-BR (pt).
    """

    def __init__(self, source: str = "en", target: str = "pt"):
        """
        :param source: ISO language code for source text
        :param target: ISO language code for target text
        """
        self.source_lang = source
        self.target_lang = target

    def set_language_pair(self, source: str, target: str):
        self.source_lang = source
        self.target_lang = target

    def get_source(self) -> str:
        return self.source_lang

    def get_target(self) -> str:
        return self.target_lang

# ------------
# 3) LEGAL TERM EXTRACTION & REVIEW
# ------------
class LegalTermExtractor:
    """
    Uses LexNLP to extract frequently used terms, ignoring stopwords,
    generating a draft glossary for each contract.
    """

    def __init__(self, top_n_terms: int = 20):
        """
        :param top_n_terms: The max number of terms/phrases to capture
        """
        self.top_n_terms = top_n_terms
        # Load English stopwords from LexNLP
        self.stopwords = set(lexnlp_stopwords.get_stopwords())

    def extract_frequent_terms(self, text: str) -> List[str]:
        """
        Tokenize text, filter out stopwords, punctuation, short tokens,
        and gather the most frequent terms. 
        Return a list of terms in descending frequency order.
        """
        # Basic tokenization with LexNLP
        tokens = list(lexnlp_tokens.get_tokens(text))
        # Lowercase everything
        tokens = [t.lower() for t in tokens]
        # Filter stopwords, punctuation, numeric, short tokens
        # Also ignoring tokens that are purely numeric or single letters
        filtered = []
        for t in tokens:
            if (len(t) > 2) and (t not in self.stopwords) and re.match(r'^[a-z]+$', t):
                filtered.append(t)

        # Count frequency
        freqdist = Counter(filtered)
        # Get most common
        most_common = freqdist.most_common(self.top_n_terms)

        # Return just the terms
        terms = [t[0] for t in most_common]
        return terms

    def user_review_and_approve(self, gemini_translator: GeminiTranslator, lang_selector: LanguageSelector, terms: List[str]) -> Dict[str, str]:
        """
        For each extracted term, get a proposed translation from the LLM
        and let user review. In a non-interactive environment, we can
        assume the translation is accepted or log it for manual editing.

        :return: A dict mapping { original_term: approved_translation }
        """
        if not terms:
            return {}

        # 1) Let Gemini propose translations for each term
        proposed = gemini_translator.translate_text_batch(
            texts=terms,
            source_lang=lang_selector.get_source(),
            target_lang=lang_selector.get_target(),
            temperature=0.1
        )

        glossary = {}
        # 2) In a real pipeline, you'd prompt user to accept or edit
        #    For demonstration, we'll automatically accept them
        for orig, trans in zip(terms, proposed):
            glossary[orig] = trans

        # This dictionary is used to enforce consistent translation
        return glossary

# ------------
# 4) MAJORITY VOTING TRANSLATOR
# ------------
def majority_vote_translations(
    translator: GeminiTranslator, 
    text: str,
    source: str,
    target: str,
    temperature: float = 0.2,
    n_votes: int = 3
) -> str:
    """
    Calls the translator n_votes times for the same segment and 
    returns the most frequent translation among them.
    If there's a tie or all different, returns the first.
    """

    translations = []
    for _ in range(n_votes):
        t = translator.translate_text(text, source, target, temperature)
        translations.append(t)

    # Tally
    counts = Counter(translations)
    # Get the highest frequency item
    most_common, freq = counts.most_common(1)[0]
    # If freq=1 for all, i.e. no majority, fallback to the first
    if freq == 1 and len(translations) == n_votes:
        return translations[0]
    return most_common

# ------------
# 5) SEGMENTATION & CONSISTENCY ENFORCEMENT
# ------------
def segment_text(html_text: str) -> List[str]:
    """
    Example function to segment text while preserving HTML structure.
    For demonstration, we'll do a naive approach: 
    - Parse with BeautifulSoup
    - For each block-level element (e.g., <p>, <li>, <hX>) we get the text.
    - Return a list of segments (strings).
    In a production scenario, you might do more refined segmentation 
    using LexNLP or a specialized approach for legal docs.
    """
    soup = BeautifulSoup(html_text, "lxml")

    segments = []
    # Just gather text from <p>, <h1..h6>, <li> etc.
    block_tags = ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "div"]

    for tag in soup.find_all(block_tags):
        segment_text = tag.get_text(separator=" ", strip=True)
        if segment_text:
            segments.append(segment_text)
    return segments

def reassemble_translated_html(original_html: str, translated_segments: List[str]) -> str:
    """
    Place the translated text back into the HTML structure in the same order.
    This is a simplified approach: we assume each block-level tag's text 
    is replaced with the corresponding translated segment in order.
    If original has N block-level tags, we have N segments.
    """
    soup = BeautifulSoup(original_html, "lxml")
    block_tags = soup.find_all(["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "div"])

    idx = 0
    for tag in block_tags:
        # Replace the text content of the tag
        if idx < len(translated_segments):
            tag.string = translated_segments[idx]
            idx += 1

    return str(soup)

def enforce_glossary(text: str, glossary: Dict[str, str]) -> str:
    """
    Post-processing approach: for each term in the glossary, if it appears
    in the text (or a close variant), replace it with the approved translation.
    For simplicity, we do a naive case-insensitive replacement. 
    In a real scenario, you'd do a more robust matching to avoid partial words 
    or morphological variations.
    """
    # Simple approach: \b boundary match
    # Might still produce partial matches in some cases, so refine as needed.
    for orig_term, approved_trans in glossary.items():
        # We'll do a case-insensitive replacement
        # e.g., replace r'(?i)\b{orig_term}\b' with {approved_trans}
        pattern = re.compile(rf"(?i)\b{re.escape(orig_term)}\b")
        text = pattern.sub(approved_trans, text)
    return text

# ------------
# 6) END-TO-END PIPELINE
# ------------
def translate_contracts_in_jsonl(
    input_jsonl_path: str,
    output_jsonl_path: str,
    gemini_translator: GeminiTranslator,
    lang_selector: LanguageSelector,
    top_n_terms=20,
    parallel_workers=4
):
    """
    Main pipeline function:
      1. Reads input.jsonl line by line.
      2. For each contract in 'contracts' key, extracts top terms, 
         obtains user-approved glossary, segments text, does majority-vote translation, 
         enforces consistency, and reassembles translated HTML.
      3. Saves output.jsonl with 'contratos' key (translated contract).
    """

    # Prepare the term extractor
    term_extractor = LegalTermExtractor(top_n_terms=top_n_terms)

    # We'll process each line (contract) in parallel for speed
    # but we also preserve line ordering in the output.
    def process_line(line_data: dict) -> dict:
        """
        Worker function to process a single contract dictionary. 
        Returns a new dict with 'contratos' key (translated HTML).
        """
        if "contracts" not in line_data:
            # nothing to do
            return line_data

        original_html = line_data["contracts"]

        # 1) Extract frequent terms & build glossary
        raw_text = BeautifulSoup(original_html, "lxml").get_text(separator=" ", strip=True)
        frequent_terms = term_extractor.extract_frequent_terms(raw_text)
        glossary_draft = term_extractor.user_review_and_approve(
            gemini_translator, lang_selector, frequent_terms
        )

        # 2) Segment HTML into blocks
        segments = segment_text(original_html)

        # 3) Translate each segment with majority voting
        translated_segments = []
        for seg in segments:
            # Enforce glossary pre-translation? 
            # Optionally we can do it post. We'll do post for demonstration
            # so the LLM can produce a natural translation, then we fix terms.
            voted_translation = majority_vote_translations(
                translator=gemini_translator,
                text=seg,
                source=lang_selector.get_source(),
                target=lang_selector.get_target(),
                temperature=0.2,
                n_votes=3
            )
            # We'll collect them for reassembly
            translated_segments.append(voted_translation)

        # 4) Reassemble into HTML
        partially_translated_html = reassemble_translated_html(original_html, translated_segments)

        # 5) Enforce glossary in the final text (post-processed)
        final_translated_html = enforce_glossary(partially_translated_html, glossary_draft)

        # 6) Create new key 'contratos'
        line_data["contratos"] = final_translated_html
        return line_data

    # Read input lines
    results = []
    with open(input_jsonl_path, "r", encoding="utf-8") as fin:
        lines = [json.loads(l.strip()) for l in fin if l.strip()]

    # We'll do parallel processing here
    with ThreadPoolExecutor(max_workers=parallel_workers) as executor:
        future_to_idx = {}
        for idx, data in enumerate(lines):
            future = executor.submit(process_line, data)
            future_to_idx[future] = idx

        # We'll collect results in the original order
        output_list = [None] * len(lines)
        for future in as_completed(future_to_idx):
            idx = future_to_idx[future]
            try:
                processed_data = future.result()
                output_list[idx] = processed_data
            except Exception as e:
                print(f"Error processing line {idx}: {e}")
                output_list[idx] = lines[idx]  # fallback

    # Write output lines
    with open(output_jsonl_path, "w", encoding="utf-8") as fout:
        for item in output_list:
            fout.write(json.dumps(item, ensure_ascii=False))
            fout.write("\n")

    print(f"Done! Results written to {output_jsonl_path}")


# ------------
# Example Main
# ------------
if __name__ == "__main__":
    """
    Example usage:
      python pipeline.py input.jsonl output.jsonl
    with environment variables or config for GCP credentials if needed.
    """
    import sys
    if len(sys.argv) < 3:
        print("Usage: python pipeline.py <input.jsonl> <output.jsonl>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 1) Initialize translator (Gemini placeholder)
    gemini = GeminiTranslator(
        project_id="my-gcp-project",
        location="us-central1",
        model_id="models/gemini-translator",
        credential_file="path/to/credentials.json"
    )

    # 2) Language selection (English -> Portuguese-BR)
    lang_sel = LanguageSelector(source="en", target="pt")

    # 3) Run pipeline
    translate_contracts_in_jsonl(
        input_jsonl_path=input_file,
        output_jsonl_path=output_file,
        gemini_translator=gemini,
        lang_selector=lang_sel,
        top_n_terms=20,
        parallel_workers=4
    )
How to Run
Install Dependencies (e.g. in a virtual environment):
bash
Copy
pip install beautifulsoup4 lexnlp requests lxml tqdm
Prepare Input: Create an input.jsonl where each line is a JSON object, for example:
jsonc
Copy
{"contracts": "<html><body><h1>LEASE AGREEMENT</h1><p>This Lease Agreement ('Agreement') is made by ...</p></body></html>"}
{"contracts": "<html><body><h2>SERVICE CONTRACT</h2><p>This Service Contract is between ...</p></body></html>"}
Run the Script:
bash
Copy
python pipeline.py input.jsonl output.jsonl
Check the Results in output.jsonl. Each line should now have "contratos" containing the “translated” HTML (in practice, a placeholder in this demo) with consistent term usage.
Key Points & Customization
Gemini API Integration:

Replace translate_text and translate_text_batch in GeminiTranslator with real calls to Google’s LLM.
Handle authentication with service accounts or OAuth.
Possibly implement error retries or rate limiting.
Term Enforcement:

We used a post-processing approach to enforce the final glossary. This is simpler to implement but can cause partial matches. A more robust approach might be to embed the glossary in the prompt or instructions.
For partial word collisions (e.g., searching “Lease” might match “Released”), you may want a more advanced matching strategy or morphological analyzers.
Segmenting Contracts:

We gave a basic HTML-based segmentation example. For more advanced segmentation (like dividing by sentence or clause, especially for complex legal docs), consider LexNLP’s section/sentence segmenters or a specialized pipeline that respects headings, enumerations, references, etc.
Parallelism:

This example uses a ThreadPoolExecutor to process lines in parallel. If your system supports multiple processes or if you want to scale horizontally, adapt it to your environment (e.g., ProcessPoolExecutor, Dask, Ray, etc.).
Majority voting calls the translator 3 times per segment. We do these calls sequentially in the snippet. For further speed, you can parallelize them via threads or async.
Reviewing Terms:

The method user_review_and_approve is currently auto-accepting the LLM’s translation. In a real scenario, you’d want to present these to a user for confirmation (e.g., a CLI prompt or a minimal web UI).
Data Privacy:

If your legal contracts are confidential, ensure you have the right to send them to an external LLM provider. Some organizations require on-premise or self-hosted solutions (e.g., Argos Translate, HuggingFace MarianMT) if data privacy is critical.
That’s the complete example of a modular pipeline for automatically translating legal contracts with consistent terminology and a best-of-three voting approach. You can enhance it further by integrating more advanced segmentation or a domain-tuned LLM, but this scaffolding covers the essential steps.

Feel free to adapt and expand this code to suit your workflow and to match real-world Gemini API methods once they become publicly documented.

Enjoy building your automated legal translation system!
