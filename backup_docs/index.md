---
layout: default
title: UBPD LLM Testimonial Classifier
description: Bilingual demo of a testimonial document classifier for the UBPD using LLMs.
permalink: /
---

# Demo – UBPD LLM Testimonial Classifier / Clasificador de documentos testimoniales

<p class="badge-row">
  <img src="https://img.shields.io/badge/status-demo-orange.svg">
  <img src="https://img.shields.io/badge/language-Python-blue.svg">
  <img src="https://img.shields.io/badge/LLM-OpenAI%20GPT-lightgrey.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
</p>

*Navigation: [English](#english-version) • [Español](#spanish-version) • [Repository](https://github.com/manueldazar/ubpd-llm-testimonial-classifier)*

---

## English Version {#english-version}

### Overview

This project is a **prototype LLM-based classifier** for testimonial documents from the  
**Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)** in Colombia.

The system loads a UBPD-oriented ontology defined in YAML, builds structured prompts,  
and forces the model to return a controlled JSON with:

- Document type  
- Event categories  
- Actors  
- Time period  
- Territory  
- Priority / routing  

The goal is to demonstrate early-stage **machine-assisted analysis** of testimonial content.

### Tech Stack

- Python  
- OpenAI GPT (configurable model)  
- YAML ontology  
- `.env` configuration  
- Jupyter / VS Code  

### Architecture

```text
ubpd-llm-testimonial-classifier/
  notebooks/
  src/
    ubpd_classifier/
  data/ontology/
  docs/
  tests/
  .env.example
  requirements.txt
```

### Quick Start

```bash
pip install -r requirements.txt
```

```text
OPENAI_API_KEY=your_key_here
```

```python
from ubpd_classifier.classifier import classify_document

sample = "My brother disappeared in 1997 in rural Antioquia..."
pred = classify_document(sample)
print(pred)
```

---

## Versión en Español {#spanish-version}

### Descripción general

Este proyecto es un **prototipo de clasificador basado en LLM** para documentos testimoniales  
de la **UBPD** en Colombia.

El sistema carga una ontología en YAML, construye prompts estructurados  
y fuerza al modelo a devolver un JSON controlado con:

- Tipo de documento  
- Tipos de hechos  
- Actores  
- Periodo  
- Territorio  
- Prioridad  

### Tecnologías

- Python  
- OpenAI GPT  
- Ontología YAML  
- Variables en `.env`  
- Notebooks Jupyter  

### Uso rápido

```bash
pip install -r requirements.txt
```

```text
OPENAI_API_KEY=tu_api_key_aqui
```

```python
from ubpd_classifier.classifier import classify_document

t = "Mi hermano desapareció en 1997 en una vereda de Antioquia..."
print(classify_document(t))
```

---

## Project Status {#project-status}

Research prototype / demo. Not a production system.

## License {#license}

MIT License — see `LICENSE`.

## How to Cite / Cómo citar

> Daza Ramírez, M. (2025). *Demo – UBPD LLM Testimonial Classifier*.  
> Prototype repository exploring LLM-based classification of testimonial documents  
> for the Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD), Colombia.  
> Available at: GitHub (public repository).

> Daza Ramírez, M. (2025). *Demo – Clasificador de documentos testimoniales UBPD con LLM*.  
> Repositorio prototipo que explora la clasificación de testimonios mediante modelos de lenguaje  
> para la Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD), Colombia.  
> Disponible en: GitHub (repositorio público).
