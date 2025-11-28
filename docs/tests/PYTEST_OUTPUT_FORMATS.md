# Pytest Output Formats Explained

## The Question

You're seeing individual test names like:
```
tests/test_classifier.py::TestExtractJsonBlock::test_extract_simple_json PASSED [  0%]
```

But the documentation shows dots like:
```
tests/test_classifier.py ..............................................................  [ 39%]
```

**Why the difference?** → It's just a formatting preference!

## Both Are Correct ✅

Both outputs mean **exactly the same thing**: All 157 tests passed.

### Output Format 1: Compact (with dots)
```bash
pytest -q
```

Shows:
```
tests/test_classifier.py ..............................................................  [ 39%]
tests/test_ontology.py ..................                                           [ 50%]
tests/test_preprocessing.py ..............................                           [ 70%]
tests/test_prompts.py ..............................                                [ 89%]
tests/test_runner.py .................                                              [100%]

========================= 157 passed in 0.83s =========================
```

**Pros**: 
- ✅ Quick visual overview
- ✅ Clean and concise
- ✅ Easy to see progress
- ✅ Great for CI/CD

**Cons**:
- ❌ Can't see individual test names
- ❌ Hard to find which test failed (if one does)

### Output Format 2: Verbose (with test names)
```bash
pytest -v
```
or just:
```bash
pytest
```

Shows:
```
tests/test_classifier.py::TestExtractJsonBlock::test_extract_simple_json PASSED      [  0%]
tests/test_classifier.py::TestExtractJsonBlock::test_extract_json_with_surrounding_text PASSED [  1%]
tests/test_classifier.py::TestExtractJsonBlock::test_extract_nested_json PASSED      [  1%]
... (157 total lines, one per test) ...
tests/test_runner.py::TestRunnerIntegration::test_read_example_document PASSED      [100%]

========================= 157 passed in 0.83s =========================
```

**Pros**:
- ✅ See exactly which test passed/failed
- ✅ Can identify specific failures
- ✅ Good for debugging
- ✅ Great for development

**Cons**:
- ❌ Longer output
- ❌ Harder to read at a glance
- ❌ Scrolls off screen with many tests

### Output Format 3: Very Quiet
```bash
pytest -q --tb=no
```

Shows:
```
157 passed in 0.83s
```

**Pros**:
- ✅ Absolutely minimal
- ✅ Just the summary

## How to Control Output

| Command | Format | Use Case |
|---------|--------|----------|
| `pytest` | Default (verbose) | Development, debugging |
| `pytest -v` | Verbose with names | See all test names |
| `pytest -q` | Compact with dots | Quick overview |
| `pytest -q --tb=no` | Just the summary | Minimal output |
| `pytest --tb=short` | Show short tracebacks | Debugging failures |
| `pytest --tb=long` | Show full tracebacks | Detailed debugging |

## What Your Output Means

```
platform win32 -- Python 3.13.7, pytest-9.0.1, pluggy-1.6.0
```
→ System information (Windows, Python 3.13.7, pytest 9.0.1)

```
cachedir: .pytest_cache
rootdir: C:\Users\...\ubpd-llm-demo-clasificador-testimonios
configfile: pytest.ini
```
→ Test configuration info

```
plugins: anyio-4.10.0, cov-7.0.0
collected 157 items
```
→ Installed plugins and number of tests found

```
tests/test_classifier.py::TestExtractJsonBlock::test_extract_simple_json PASSED [  0%]
```
→ Individual test result (each line = one test)

```
========================= 157 passed in 0.83s =========================
```
→ **Summary: All tests passed!** ✅

## Quick Reference

**Want compact output like documentation shows?**
```bash
pytest -q
```

**Want to see test names (default)?**
```bash
pytest
```

**Want detailed output for debugging?**
```bash
pytest -vv
```

**Want to see only failures?**
```bash
pytest -q --tb=short
```

**Want to stop at first failure?**
```bash
pytest -x
```

---

## Bottom Line

✅ **Your tests are ALL PASSING** (157/157)

The output format is just a matter of preference:
- Use `-q` for clean, compact output
- Use `-v` (or default) for detailed output
- Use `-vv` for maximum detail

**All three show the same result: 157 tests passed in 0.83 seconds!**

---

**Need help?** Run:
```bash
pytest --help
```

For full pytest options and documentation.
