---
layout: default
title: LLM Testimonial Classifier
description: Clasificador automático de documentos testimoniales para organizaciones de derechos humanos | Automatic testimonial document classifier for human rights organizations
lang: es
---

# LLM Testimonial Classifier

[🇪🇸 Español](#español) | [🇺🇸 English](#english)

---

## Español

### Clasificador de Documentos Testimoniales con IA

Sistema de **clasificación automática de documentos testimoniales** para organizaciones de derechos humanos, comisiones de la verdad y entidades que procesan testimonios relacionados con conflictos armados o justicia transicional.

---

### El Problema

Las organizaciones que trabajan con documentación testimonial enfrentan desafíos críticos:

| Desafío | Impacto |
|---------|---------|
| **Alto volumen** | Miles de testimonios pendientes de clasificación |
| **Inconsistencia** | Variabilidad en criterios entre analistas |
| **Tiempo limitado** | Recursos humanos escasos |
| **Priorización** | Dificultad para identificar casos urgentes |

---

### La Solución

Un sistema que combina **Modelos de Lenguaje (GPT-4o)** con una **ontología controlada** para:

- ✅ Clasificar documentos automáticamente en múltiples dimensiones
- ✅ Garantizar consistencia mediante vocabularios estandarizados
- ✅ Calcular scores de prioridad para enrutamiento de casos
- ✅ Extraer fragmentos clave para análisis humano
- ✅ Persistir resultados para auditoría

---

### Arquitectura del Sistema

```
Documento       Preprocesamiento      Prompt + Ontología
Testimonial  ──────────────────────▶  ──────────────────▶  LLM (GPT-4o)
                                                                │
                                                                ▼
PostgreSQL   ◀────  Persistencia  ◀────  Validación + Score de Prioridad
```

---

### Dimensiones de Clasificación

**Tipo de Documento**
- Testimonio de víctima directa
- Testimonio de familiar
- Testimonio de exintegrante
- Testimonio de tercero testigo

**Hechos Victimizantes**
- Desaparición forzada
- Homicidio
- Desplazamiento forzado
- Violencia sexual
- Reclutamiento de menores
- Tortura

**Actores**
- Fuerza Pública
- Guerrillas
- Paramilitares
- Grupos criminales

**Territorio y Período**
- Regiones geográficas configurables
- Períodos históricos personalizables

---

### Inicio Rápido

```bash
# Clonar e instalar
git clone https://github.com/manueldazar/llm-testimonial-classifier.git
cd llm-testimonial-classifier
pip install -r requirements.txt

# Configurar API key
echo "OPENAI_API_KEY=sk-..." > .env

# Clasificar un documento
python src/runner.py --text "El testigo declara que en 1998..." --no-db
```

---

### Casos de Uso

Este clasificador está diseñado para:

- **Comisiones de la Verdad** — Procesamiento de testimonios de víctimas
- **Fiscalías Especializadas** — Clasificación de declaraciones
- **ONGs de Derechos Humanos** — Análisis de denuncias
- **Unidades de Búsqueda** — Priorización de casos
- **Tribunales de Justicia Transicional** — Categorización de evidencia
- **Organizaciones Internacionales** — Documentación humanitaria

---

### Documentación

| Sección | Descripción |
|---------|-------------|
| [Arquitectura](docs/architecture.html) | Diseño técnico del sistema |
| [Ontología](docs/ontology.html) | Vocabulario controlado completo |
| [API](docs/api.html) | Referencia de funciones |
| [Demo](docs/demo.html) | Ejemplos interactivos |

---

### Crédito Intelectual y Procedencia

Este proyecto —incluyendo su arquitectura, el diseño de la ontología, la estrategia de prompt engineering, el plan de evaluación y la implementación de referencia— fue concebido, diseñado y desarrollado por **Manuel Daza**. Todos los componentes conceptuales (formulación del problema, justificación del esquema de datos, ontología de clasificación, plantillas de prompt, criterios de evaluación y flujos del demostrador) se originan en este repositorio y en su historial de commits.

El código, la documentación y el enfoque metodológico se publican para ofrecer transparencia y fomentar una discusión responsable, y **no constituyen autorización implícita** para uso institucional, trabajo derivado con fines comerciales o despliegue operativo. Cualquier reutilización, adaptación o implementación institucional debe reconocer explícitamente al autor original y cumplir con la licencia del proyecto.

**Atribución requerida:**

> **Manuel Daza** — Autor y Arquitecto Original  
> GitHub: [https://github.com/manueldazar](https://github.com/manueldazar)

Para colaboración, pilotos o acompañamiento en la implementación, por favor contacte directamente al autor.

---

## English

### AI-Powered Testimonial Document Classifier

**Automatic classification system for testimonial documents** designed for human rights organizations, truth commissions, and entities processing testimonies related to armed conflicts or transitional justice.

---

### The Problem

Organizations working with testimonial documentation face critical challenges:

| Challenge | Impact |
|-----------|--------|
| **High volume** | Thousands of testimonies pending classification |
| **Inconsistency** | Variability in criteria among analysts |
| **Limited time** | Scarce human resources |
| **Prioritization** | Difficulty identifying urgent cases |

---

### The Solution

A system combining **Large Language Models (GPT-4o)** with a **controlled ontology** to:

- ✅ Automatically classify documents across multiple dimensions
- ✅ Ensure consistency through standardized vocabularies
- ✅ Calculate priority scores for case routing
- ✅ Extract key fragments for human analysis
- ✅ Persist results for audit trails

---

### System Architecture

```
Testimonial      Preprocessing        Prompt + Ontology
Document     ──────────────────────▶  ──────────────────▶  LLM (GPT-4o)
                                                                │
                                                                ▼
PostgreSQL   ◀────  Persistence   ◀────  Validation + Priority Score
```

---

### Classification Dimensions

**Document Type**
- Direct victim testimony
- Family member testimony
- Former combatant testimony
- Third-party witness

**Victimizing Events**
- Forced disappearance
- Homicide
- Forced displacement
- Sexual violence
- Child recruitment
- Torture

**Actors**
- Public Forces
- Guerrillas
- Paramilitaries
- Criminal groups

**Territory and Period**
- Configurable geographic regions
- Customizable historical periods

---

### Quick Start

```bash
# Clone and install
git clone https://github.com/manueldazar/llm-testimonial-classifier.git
cd llm-testimonial-classifier
pip install -r requirements.txt

# Configure API key
echo "OPENAI_API_KEY=sk-..." > .env

# Classify a document
python src/runner.py --text "The witness states that in 1998..." --no-db
```

---

### Use Cases

This classifier is designed for:

- **Truth Commissions** — Processing victim testimonies
- **Specialized Prosecutors** — Classifying statements
- **Human Rights NGOs** — Analyzing complaints
- **Search Units** — Prioritizing cases
- **Transitional Justice Tribunals** — Categorizing evidence
- **International Organizations** — Humanitarian documentation

---

### Documentation

| Section | Description |
|---------|-------------|
| [Architecture](docs/architecture.html) | System technical design |
| [Ontology](docs/ontology.html) | Complete controlled vocabulary |
| [API](docs/api.html) | Function reference |
| [Demo](docs/demo.html) | Interactive examples |

---

### Intellectual Credit and Provenance

This project —including its architecture, ontology design, prompt engineering strategy, evaluation plan, and reference implementation— was conceived, designed, and developed by **Manuel Daza**. All conceptual components (problem formulation, data schema rationale, classification ontology, prompt templates, evaluation criteria, and demonstrator workflows) originate in this repository and its commit history.

The code, documentation, and methodological approach are published to provide transparency and encourage responsible discussion, and **do not constitute implicit authorization** for institutional use, commercial derivative work, or operational deployment. Any reuse, adaptation, or institutional implementation must explicitly acknowledge the original author and comply with the project license.

**Required attribution:**

> **Manuel Daza** — Original Author and Architect  
> GitHub: [https://github.com/manueldazar](https://github.com/manueldazar)

For collaboration, pilots, or implementation support, please contact the author directly.

---

## Author / Autor

**Manuel Daza Ramírez**  
AI Engineer

[LinkedIn](https://linkedin.com/in/manueldazaramirez) | [GitHub](https://github.com/manueldazar) | [Email](mailto:manuel.dazaramirez@gmail.com)

---

## Disclaimer / Aviso Legal

**English:** This is a demonstration prototype. Example testimonies are synthetic and do not represent real cases. Production deployment requires human review, audit logging, and compliance with data protection regulations.

**Español:** Este es un prototipo de demostración. Los testimonios de ejemplo son sintéticos y no representan casos reales. El despliegue en producción requiere revisión humana, logging de auditoría y cumplimiento de normativas de protección de datos.

---

*LLM Testimonial Classifier · 2025 · Manuel Daza*
