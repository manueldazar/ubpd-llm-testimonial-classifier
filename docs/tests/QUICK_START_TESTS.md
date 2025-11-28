# 🚀 Quick Start - Running the Tests

## Installation

Ensure pytest is installed:
```bash
pip install pytest pytest-cov
```

## Run All Tests

From the project root directory:
```bash
pytest
```

**Expected output (compact format - using `-q` flag):**
```
========================= test session starts =========================
collected 157 items

tests/test_classifier.py ..............................................................                    [ 39%]
tests/test_ontology.py ..................                                                                  [ 50%] 
tests/test_preprocessing.py ..............................                                                 [ 70%]
tests/test_prompts.py ..............................                                                       [ 89%]
tests/test_runner.py .................                                                                     [100%]

========================= 157 passed in 0.83s =========================
```

**What you'll actually see (default verbose format):**
```
platform win32 -- Python 3.13.7, pytest-9.0.1, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: C:\Users\...\ubpd-llm-demo-clasificador-testimonios
configfile: pytest.ini
plugins: anyio-4.10.0, cov-7.0.0
collected 157 items

tests/test_classifier.py::TestExtractJsonBlock::test_extract_simple_json PASSED                           [  0%]
tests/test_classifier.py::TestExtractJsonBlock::test_extract_json_with_surrounding_text PASSED           [  1%]
tests/test_classifier.py::TestExtractJsonBlock::test_extract_nested_json PASSED                          [  1%]
... (more individual test results) ...
tests/test_runner.py::TestRunnerIntegration::test_read_example_document PASSED                           [100%]

========================= 157 passed in 0.83s =========================
```

Both show **157 passed** - just different formatting! ✅

## Common Commands

### Get the Compact Format (Dots Only)
```bash
pytest -q
```
Shows dots (.) for passed tests - great for quick overview

### Verbose Output (Shows Test Names)
```bash
pytest -v
```
Shows each test name individually - good for debugging

### Run Single Test File
```bash
pytest tests/test_preprocessing.py -v
```

### Run Single Test Class
```bash
pytest tests/test_classifier.py::TestFixSingleLabel -v
```

### Run Single Test
```bash
pytest tests/test_classifier.py::TestFixSingleLabel::test_fix_valid_label -v
```

### Run Tests Matching Pattern
```bash
pytest -k "test_fix" -v
```

### Generate Coverage Report
```bash
pytest --cov=src/ubpd_classifier --cov-report=html
# Then open htmlcov/index.html in browser
```

### Stop on First Failure
```bash
pytest -x
```

### Run Only Last Failed Tests
```bash
pytest --lf
```

## Test Files Overview

| File | Tests | Focus |
|------|-------|-------|
| test_preprocessing.py | 30 | Text normalization |
| test_ontology.py | 17 | Ontology data validation |
| test_prompts.py | 28 | LLM prompt generation |
| test_classifier.py | 61 | Classification logic |
| test_runner.py | 17 | CLI and file operations |
| **Total** | **157** | **All modules** |

## Test Categories

### By Module
```bash
pytest tests/test_preprocessing.py     # Text processing
pytest tests/test_ontology.py          # Ontology validation
pytest tests/test_prompts.py           # Prompt generation
pytest tests/test_classifier.py        # Classification
pytest tests/test_runner.py            # CLI & I/O
```

### By Feature
```bash
pytest -k "fix_" -v                    # All fixing functions
pytest -k "compute" -v                 # Priority computation
pytest -k "parse" -v                   # JSON parsing
pytest -k "normalize" -v               # Text normalization
```

## Debugging

### See Full Output on Failure
```bash
pytest -vv --tb=long
```

### Show Print Statements
```bash
pytest -s
```

### Show Local Variables on Failure
```bash
pytest -l
```

### Debug Mode (Drop into pdb on failure)
```bash
pytest --pdb
```

## Performance

**Execution time**: ~0.83 seconds (157 tests)
**Memory usage**: < 50 MB
**No external dependencies**: All tests are isolated
**Status**: ✅ All 157 tests passing

## Next Steps

1. **Review test structure**: Open `tests/README.md`
2. **Check coverage**: `pytest --cov=src/ubpd_classifier`
3. **Run specific tests**: Use the commands above
4. **Add new tests**: Use existing tests as templates
5. **CI/CD integration**: Copy pytest.ini to your CI configuration

## Documentation

- 📖 **tests/README.md** - Comprehensive testing guide
- 📊 **TEST_SUMMARY.md** - Executive summary
- 🎨 **TESTS_VISUAL_OVERVIEW.md** - Visual reference
- ✅ **TESTS_CHECKLIST.md** - Implementation details

## Support

For issues:
1. Check tests/README.md Troubleshooting section
2. Verify pytest is installed: `pytest --version`
3. Ensure you're in project root directory
4. Check that src/ubpd_classifier path is accessible

---

**Happy testing!** ✅
