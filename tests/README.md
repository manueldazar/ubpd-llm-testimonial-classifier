# UBPD Classifier Unit Tests Guide

## Overview

This directory contains comprehensive unit tests for the UBPD (Unidad de Búsqueda de Personas Desaparecidas) document classifier. The tests are organized by module and include fixtures for common test data.

## Test Structure

```
tests/
├── conftest.py                 # Shared pytest fixtures
├── test_preprocessing.py       # Tests for text preprocessing
├── test_ontology.py            # Tests for ontology loading and conversion
├── test_prompts.py             # Tests for LLM prompt generation
├── test_classifier.py          # Tests for classification logic
├── test_runner.py              # Tests for CLI and file operations
└── README.md                   # This file
```

## Test Coverage

### test_preprocessing.py
Tests the text normalization and preprocessing pipeline:
- **TestNormalizeUnicode**: Unicode normalization functions
- **TestCollapseSpaces**: Whitespace collapsing and normalization
- **TestRemoveHeadersAndFooters**: Document header/footer removal
- **TestPreprocessText**: Complete preprocessing pipeline

**Coverage**: All text preprocessing utilities

### test_ontology.py
Tests ontology loading and prompt generation:
- **TestLoadOntology**: Validates ontology structure and content
- **TestOntologyToPromptText**: Tests conversion to LLM-friendly format

**Coverage**: Ontology data structure and formatting

### test_prompts.py
Tests LLM prompt construction:
- **TestSystemPrompt**: Validates system prompt structure
- **TestUserTemplate**: Validates user prompt template
- **TestOntologyObjects**: Tests ONTOLOGY and ONTOLOGY_PROMPT objects
- **TestBuildUserPrompt**: Tests prompt building with document injection
- **TestPromptConsistency**: Tests consistency between prompts

**Coverage**: Prompt building and validation

### test_classifier.py
Tests the core classification logic (largest test file):
- **TestExtractJsonBlock**: JSON extraction from LLM responses
- **TestParseModelResponse**: JSON parsing and validation
- **TestFixSingleLabel**: Single field value correction
- **TestFixMultiLabels**: Multi-value field validation
- **TestFixTerritorio**: Department/territory normalization
- **TestComputePriority**: Priority score calculation
- **TestValidateAndFix**: Complete validation and fixing pipeline
- **TestClassifyDocumentWithMocks**: Mocked end-to-end classification

**Coverage**: All classification validation and fixing functions

### test_runner.py
Tests CLI and file operations:
- **TestReadTextFromFile**: File reading and encoding
- **TestRunnerArgumentParsing**: CLI argument parsing
- **TestRunnerIntegration**: Integration with example documents

**Coverage**: CLI utilities and file I/O

## Running Tests

### Run all tests
```bash
pytest
```

### Run with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_preprocessing.py -v
```

### Run specific test class
```bash
pytest tests/test_classifier.py::TestFixSingleLabel -v
```

### Run specific test function
```bash
pytest tests/test_classifier.py::TestFixSingleLabel::test_fix_valid_label -v
```

### Run tests with coverage report
```bash
pytest --cov=src/ubpd_classifier --cov-report=html
```

### Run tests matching a pattern
```bash
pytest -k "test_fix" -v
```

### Run with markers
```bash
pytest -m unit  # Run only unit tests
pytest -m "not slow"  # Run all except slow tests
```

## Test Fixtures (conftest.py)

Shared fixtures available to all tests:

### Data Fixtures
- **sample_ontology**: Complete UBPD ontology structure
- **sample_victim_testimony**: Testimony from direct victim
- **sample_non_testimonial**: Administrative non-testimonial document
- **sample_displacement_testimony**: Testimony involving displacement
- **sample_sexual_violence_testimony**: Testimony about sexual violence

### Response Fixtures
- **valid_classification_response**: Valid classification output
- **invalid_classification_response**: Classification needing fixes
- **td0_classification_response**: Non-testimonial classification

## Test Data

Tests use realistic Spanish testimonies and documents matching the UBPD use case:
- Direct victim testimonies
- Family member testimonies
- Administrative documents
- Real Colombian department names
- Authentic time periods and actors

## Mocking Strategy

- **External API calls**: Mocked using `unittest.mock.patch`
- **LLM responses**: Mocked with realistic JSON responses
- **File operations**: Use `tempfile` for isolated testing
- **Database calls**: Avoided in unit tests (integration tests only)

## Code Organization Best Practices

1. **Test organization**: Tests grouped into classes by function
2. **Naming**: Clear test names describing what is tested
3. **Fixtures**: Reusable test data via pytest fixtures
4. **Isolation**: Each test is independent
5. **Clarity**: Comments explaining complex test logic

## Adding New Tests

When adding new tests:

1. Identify the module being tested
2. Create test class for that component
3. Name tests descriptively: `test_<function>_<scenario>`
4. Use appropriate fixtures from `conftest.py`
5. Mock external dependencies
6. Add docstrings explaining the test
7. Group related tests in classes

Example:
```python
class TestNewFeature:
    """Test suite for new feature."""
    
    def test_new_feature_basic_case(self):
        """Test basic functionality."""
        # Arrange
        input_data = "test"
        
        # Act
        result = new_function(input_data)
        
        # Assert
        assert result == "expected"
```

## Continuous Integration

These tests are designed to run in CI/CD pipelines:
- No external API calls required (all mocked)
- No database connection needed
- Fast execution (< 1 second per test)
- Deterministic results
- Clear error messages

## Known Limitations

1. **classify_document function**: Requires LLM API key, tested with mocks
2. **Database functions**: Not extensively tested (require PostgreSQL setup)
3. **Integration tests**: Some require actual files in examples/ directory

## Troubleshooting

### Import errors
If you get "Import X could not be resolved":
- Ensure `src/ubpd_classifier` is in Python path
- Check that conftest.py sys.path modification is working
- Run pytest from project root directory

### Fixture errors
If fixtures aren't found:
- Ensure conftest.py is in tests/ directory
- Check pytest can discover conftest.py

### Mock errors
If mocks aren't working:
- Ensure patches are applied at correct import location
- Verify the patched module is being imported correctly

## Contributing

When contributing tests:
1. Maintain test-to-code coverage ratio
2. Follow existing naming conventions
3. Include docstrings for clarity
4. Use appropriate markers (@pytest.mark.unit, etc.)
5. Keep tests focused and isolated
6. Update this README if adding new test modules

## Performance

Current test suite runs in approximately:
- Full suite: < 5 seconds
- Single module: < 1 second
- Single test: < 100ms

## Dependencies

Tests require:
- pytest >= 7.0
- pytest-cov (for coverage reports)
- Standard library modules (unittest.mock, tempfile, json, etc.)

Install test dependencies:
```bash
pip install -r requirements.txt
pytest  # Run tests
```
