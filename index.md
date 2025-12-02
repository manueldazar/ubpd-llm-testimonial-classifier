---
layout: default
title: UBPD LLM Testimonial Classifier
description: Clasificador automático de documentos testimoniales usando LLM | Automatic testimonial document classifier using LLM
lang: es
---

<div class="lang-selector" style="text-align: right; margin-bottom: 2rem;">
  <a href="#español" style="margin-right: 1rem;">🇨🇴 Español</a>
  <a href="#english">🇺🇸 English</a>
</div>

---

<div id="español">

# 📄 Clasificador de Documentos Testimoniales UBPD

> **Sistema de clasificación automática de testimonios del conflicto armado colombiano mediante Inteligencia Artificial**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-Demo-orange.svg)](#)

---

## 🎯 Propósito

Este proyecto desarrolla un **clasificador inteligente** para apoyar a la [Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)](https://ubpd.gov.co/) en el procesamiento de miles de documentos testimoniales relacionados con el conflicto armado colombiano.

### El Desafío

| Problema | Impacto |
|----------|---------|
| 📚 **Alto volumen** | Miles de testimonios pendientes de clasificación |
| ⚖️ **Inconsistencia** | Variabilidad en criterios entre analistas |
| ⏱️ **Tiempo limitado** | Recursos humanos escasos para tareas repetitivas |
| 🎯 **Priorización** | Dificultad para identificar casos urgentes |

### La Solución

Un sistema que combina **Modelos de Lenguaje (LLM)** con una **ontología controlada** para:

- ✅ Clasificar documentos automáticamente
- ✅ Garantizar consistencia mediante vocabularios estandarizados
- ✅ Calcular scores de prioridad para enrutamiento
- ✅ Extraer fragmentos clave para análisis humano

---

## 🏗️ Arquitectura

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Documento      │────▶│   Preprocesado   │────▶│   Clasificación  │
│   Testimonial    │     │   + Normalización│     │   LLM (GPT-4o)   │
└──────────────────┘     └──────────────────┘     └────────┬─────────┘
                                                           │
┌──────────────────┐     ┌──────────────────┐              │
│   Base de Datos  │◀────│   Validación     │◀─────────────┘
│   PostgreSQL     │     │   + Ontología    │
└──────────────────┘     └──────────────────┘
```

---

## 📊 Ontología de Clasificación

El sistema clasifica documentos en múltiples dimensiones:

<div class="grid-container" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">

<div class="card">
<h4>📋 Tipo de Documento</h4>
<ul>
<li>Testimonio de víctima directa</li>
<li>Testimonio de familiar</li>
<li>Testimonio de exintegrante</li>
<li>Testimonio de tercero</li>
</ul>
</div>

<div class="card">
<h4>⚠️ Hechos Victimizantes</h4>
<ul>
<li>Desaparición forzada</li>
<li>Homicidio</li>
<li>Desplazamiento forzado</li>
<li>Violencia sexual</li>
</ul>
</div>

<div class="card">
<h4>👥 Actores Armados</h4>
<ul>
<li>Fuerza Pública</li>
<li>Guerrillas</li>
<li>Paramilitares / AUC</li>
<li>BACRIM</li>
</ul>
</div>

<div class="card">
<h4>📍 Territorio & Período</h4>
<ul>
<li>33 departamentos de Colombia</li>
<li>Períodos: 1985-2025</li>
<li>Ruteo a equipos especializados</li>
</ul>
</div>

</div>

---

## 🚀 Inicio Rápido

```bash
# Clonar repositorio
git clone https://github.com/manueldazar/ubpd-llm-testimonial-classifier.git
cd ubpd-llm-testimonial-classifier

# Instalar dependencias
pip install -r requirements.txt

# Configurar API key
echo "OPENAI_API_KEY=sk-..." > .env

# Clasificar un documento
python src/runner.py --text "Mi hermano desapareció en 1998 en Urabá..." --no-db
```

---

## 📖 Documentación

| Sección | Descripción |
|---------|-------------|
| [🏛️ Arquitectura](docs/architecture.html) | Diseño técnico del sistema |
| [📚 Ontología](docs/ontology.html) | Vocabulario controlado completo |
| [🔌 API](docs/api.html) | Referencia de funciones |
| [🎮 Demo](docs/demo.html) | Ejemplos interactivos |
| [🧪 Tests](docs/tests/index.html) | Suite de pruebas |

---

## 👨‍💻 Autor

**Manuel Daza Ramírez**  
AI Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue.svg)](https://linkedin.com/in/manueldazaramirez)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black.svg)](https://github.com/manueldazar)
[![Email](https://img.shields.io/badge/Email-Contact-red.svg)](mailto:manuel.dazaramirez@gmail.com)

</div>

---

<div id="english">

# 📄 UBPD Testimonial Document Classifier

> **Automatic classification system for Colombian armed conflict testimonies using Artificial Intelligence**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-Demo-orange.svg)](#)

---

## 🎯 Purpose

This project develops an **intelligent classifier** to support the [Unit for the Search of Persons Deemed Disappeared (UBPD)](https://ubpd.gov.co/) in processing thousands of testimonial documents related to the Colombian armed conflict.

### The Challenge

| Problem | Impact |
|---------|--------|
| 📚 **High volume** | Thousands of testimonies pending classification |
| ⚖️ **Inconsistency** | Variability in criteria among analysts |
| ⏱️ **Limited time** | Scarce human resources for repetitive tasks |
| 🎯 **Prioritization** | Difficulty identifying urgent cases |

### The Solution

A system that combines **Large Language Models (LLM)** with a **controlled ontology** to:

- ✅ Automatically classify documents
- ✅ Ensure consistency through standardized vocabularies
- ✅ Calculate priority scores for routing
- ✅ Extract key fragments for human analysis

---

## 🏗️ Architecture

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Testimonial    │────▶│   Preprocessing  │────▶│   Classification │
│   Document       │     │   + Normalization│     │   LLM (GPT-4o)   │
└──────────────────┘     └──────────────────┘     └────────┬─────────┘
                                                           │
┌──────────────────┐     ┌──────────────────┐              │
│   PostgreSQL     │◀────│   Validation     │◀─────────────┘
│   Database       │     │   + Ontology     │
└──────────────────┘     └──────────────────┘
```

---

## 📊 Classification Ontology

The system classifies documents across multiple dimensions:

<div class="grid-container" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">

<div class="card">
<h4>📋 Document Type</h4>
<ul>
<li>Direct victim testimony</li>
<li>Family member testimony</li>
<li>Former combatant testimony</li>
<li>Third-party witness</li>
</ul>
</div>

<div class="card">
<h4>⚠️ Victimizing Events</h4>
<ul>
<li>Forced disappearance</li>
<li>Homicide</li>
<li>Forced displacement</li>
<li>Sexual violence</li>
</ul>
</div>

<div class="card">
<h4>👥 Armed Actors</h4>
<ul>
<li>Public Forces</li>
<li>Guerrillas</li>
<li>Paramilitaries / AUC</li>
<li>Criminal bands</li>
</ul>
</div>

<div class="card">
<h4>📍 Territory & Period</h4>
<ul>
<li>33 Colombian departments</li>
<li>Periods: 1985-2025</li>
<li>Routing to specialized teams</li>
</ul>
</div>

</div>

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/manueldazar/ubpd-llm-testimonial-classifier.git
cd ubpd-llm-testimonial-classifier

# Install dependencies
pip install -r requirements.txt

# Configure API key
echo "OPENAI_API_KEY=sk-..." > .env

# Classify a document
python src/runner.py --text "My brother disappeared in 1998 in Urabá..." --no-db
```

---

## 📖 Documentation

| Section | Description |
|---------|-------------|
| [🏛️ Architecture](docs/architecture.html) | System technical design |
| [📚 Ontology](docs/ontology.html) | Complete controlled vocabulary |
| [🔌 API](docs/api.html) | Function reference |
| [🎮 Demo](docs/demo.html) | Interactive examples |
| [🧪 Tests](docs/tests/index.html) | Test suite |

---

## 🌍 Context: The Colombian Armed Conflict

The UBPD (Unidad de Búsqueda de Personas dadas por Desaparecidas) is a Colombian state entity created under the 2016 Peace Agreement. Its mission is to lead humanitarian actions to search for persons disappeared in the context of the armed conflict.

Key statistics:
- **Duration**: Over 50 years of internal conflict
- **Disappeared persons**: Estimated 80,000+
- **Testimonies**: Thousands of documents from victims, families, and witnesses

This classifier aims to accelerate the processing of these testimonies while maintaining human oversight for critical decisions.

---

## 🔬 Technical Highlights

### Prompt Engineering
- **Few-shot learning** with domain-specific examples
- **Controlled vocabulary** injection in system prompt
- **Self-verification** instructions for the LLM
- **JSON schema enforcement** for structured output

### Data Model
- Normalized PostgreSQL schema for multi-label classification
- JSONB storage for raw LLM responses (auditability)
- UUID-based document tracking

### Validation Pipeline
- Ontology-based code validation
- Business rules enforcement (e.g., TD0 → RU0)
- Priority score calculation for case routing

---

## 👨‍💻 Author

**Manuel Daza Ramírez**  
AI Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue.svg)](https://linkedin.com/in/manueldazaramirez)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black.svg)](https://github.com/manueldazar)
[![Email](https://img.shields.io/badge/Email-Contact-red.svg)](mailto:manuel.dazaramirez@gmail.com)

---

## ⚠️ Disclaimer

This is a **demonstration prototype**. All example testimonies are **synthetic** and do not represent real cases. Production deployment requires:

- Human review of high-priority classifications
- Audit logging for accountability
- Compliance with sensitive data regulations
- Model quality monitoring

</div>

---

<footer style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #eee;">
  <p>
    <strong>UBPD LLM Testimonial Classifier</strong> · Demo Project · 2025
  </p>
  <p>
    <a href="https://github.com/manueldazar/ubpd-llm-testimonial-classifier">GitHub Repository</a> ·
    <a href="https://ubpd.gov.co/">About UBPD</a>
  </p>
</footer>
