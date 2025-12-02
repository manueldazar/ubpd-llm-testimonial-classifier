---
layout: default
title: Tests – Visual Overview / Vista Visual
---

# Tests – Visual Overview / Vista Visual

[English](#english-version) • [Español](#spanish-version)

---

## English Version {#english-version}

### Test tree

```text
tests/
  conftest.py
  test_preprocessing.py
  test_ontology.py
  test_prompts.py
  test_classifier.py
  test_runner.py
```

### Mermaid – mapping tests to modules

```mermaid
flowchart TD
    A[tests/test_preprocessing.py] --> P[preprocessing.py]
    B[tests/test_ontology.py] --> O[ontology.py]
    C[tests/test_prompts.py] --> R[prompts.py]
    D[tests/test_classifier.py] --> C1[classifier.py]
    E[tests/test_runner.py] --> R1[runner.py]
```

---

## Versión en Español {#spanish-version}

### Árbol de pruebas

```text
tests/
  conftest.py
  test_preprocessing.py
  test_ontology.py
  test_prompts.py
  test_classifier.py
  test_runner.py
```

### Mermaid – mapeo pruebas → módulos

```mermaid
flowchart TD
    A[tests/test_preprocessing.py] --> P[preprocessing.py]
    B[tests/test_ontology.py] --> O[ontology.py]
    C[tests/test_prompts.py] --> R[prompts.py]
    D[tests/test_classifier.py] --> C1[classifier.py]
    E[tests/test_runner.py] --> R1[runner.py]
```
