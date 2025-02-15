# contract_translator
# contract_translator

# Contract Translation Pipeline

A robust pipeline for processing and translating legal contracts with advanced NLP capabilities.

## Requirements

- Python >= 3.12
- UV package manager

## Installation

1. Install UV if you haven't already
2. Clone the repository
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```
4. Install dependencies using UV:
   ```bash
   uv pip install -e ".[dev,test]"
   ```

## Project Structure

```
.
├── legal_translation_pipeline/    # Main package directory
│   ├── pipeline.py               # Core pipeline implementation
│   └── input.jsonl               # Sample input data
├── tests/                        # Test suite
├── pyproject.toml               # Project configuration and dependencies
└── README.md                    # This file
```

## Pipeline Steps

1. **Document Preprocessing**
   - Text cleaning and normalization
   - Legal entity recognition
   - Structure parsing

2. **Translation Processing**
   - Legal terminology extraction
   - Context-aware translation
   - Format preservation

3. **Quality Assurance**
   - Legal compliance checking
   - Translation verification
   - Format validation

## Features

- Legal document parsing and preprocessing
- Advanced NLP processing using:
  - LexNLP for legal text analysis
  - NLTK for natural language processing
  - Gensim for document similarity
  - Scikit-learn for machine learning tasks
- Document format support:
  - Text-based documents
  - PDF processing
  - HTML parsing with BeautifulSoup4
- Elasticsearch integration for document storage and search
- Comprehensive test suite with pytest
- Performance monitoring with memory-profiler
- Supports parallel processing for batch translations

## Dependencies

Key dependencies are managed through `pyproject.toml` and include:

- **Document Processing**
  - lexnlp >= 2.3.0
  - beautifulsoup4 >= 4.13.3
  - lxml >= 5.3.1

- **NLP & Machine Learning**
  - nltk >= 3.9.1
  - scikit-learn >= 1.6.1
  - gensim >= 4.3.3

- **Data Processing**
  - pandas >= 2.2.3
  - numpy >= 1.26.4

- **Storage & Search**
  - elasticsearch >= 8.17.1

For a complete list of dependencies, see `pyproject.toml`.

## Usage

1. Prepare your input data in JSONL format (see `legal_translation_pipeline/input.jsonl` for example)
2. Run the pipeline:
   ```python
   from legal_translation_pipeline.pipeline import TranslationPipeline
   
   pipeline = TranslationPipeline()
   pipeline.process("path/to/input.jsonl")
   ```

## Development

- Use UV for package management
- Run tests with pytest: `uv run pytest`
- Follow the code style guidelines in `pyproject.toml`
- Check test coverage before submitting PRs

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- **arthrod** - *Initial work* - [arthrod@gmail.com]

## Acknowledgments

- LexNLP community for legal text processing tools
- NLTK team for natural language processing capabilities
- Elasticsearch for powerful search functionality

## Notes

- Always use UV instead of pip for package management
- Ensure you're using Python 3.12 or higher
- Check the test coverage before submitting PRs
- Regular updates to legal term dictionaries recommended
- Supports parallel processing for batch translations