---
layout: default
title: Tests – Quick Start / Inicio Rápido
---

# Tests – Quick Start / Inicio Rápido

[English](#english-version) • [Español](#spanish-version)

---

## English Version {#english-version}

### 1. Environment

```bash
pip install -r requirements.txt
pytest --version
```

### 2. Run all tests

```bash
pytest
```

### 3. Run with verbose output

```bash
pytest -v
```

### 4. Run a single module

```bash
pytest tests/test_classifier.py -v
```

### 5. Run by pattern

```bash
pytest -k "priority" -v
```

### 6. Coverage

```bash
pytest --cov=src/ubpd_classifier --cov-report=html
```

---

## Versión en Español {#spanish-version}

### 1. Entorno

```bash
pip install -r requirements.txt
pytest --version
```

### 2. Ejecutar todas las pruebas

```bash
pytest
```

### 3. Ejecutar con salida detallada

```bash
pytest -v
```

### 4. Ejecutar un módulo específico

```bash
pytest tests/test_classifier.py -v
```

### 5. Ejecutar por patrón

```bash
pytest -k "priority" -v
```

### 6. Cobertura

```bash
pytest --cov=src/ubpd_classifier --cov-report=html
```
