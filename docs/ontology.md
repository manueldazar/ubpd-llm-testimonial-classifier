---
layout: default
title: Ontology / Ontología – UBPD LLM Classifier
---

# Ontology / Ontología

[English](#english-version) · [Español](#spanish-version)

---

# English Version {#english-version}

## 1. Overview

The classifier uses a YAML ontology defining:

- Document types  
- Actors  
- Events  
- Territory metadata  

## 2. Example Structure

```yaml
document_types:
  - victim_direct
  - family_member
actors:
  armed_groups:
    - FARC
    - AUC
events:
  disappearance:
    - forced_disappearance
territory:
  region:
    - Antioquia
    - Meta
```

## 3. Ontology Diagram

<div class="mermaid">
flowchart TD
    A[Ontology] --> B[Document Types]
    A --> C[Actors]
    A --> D[Events]
    A --> E[Territory]
</div>

---

# Versión en Español {#spanish-version}

## 1. Descripción General

El clasificador usa una ontología YAML que define:

- Tipos de documento  
- Actores  
- Hechos  
- Información de territorio  

## 2. Ejemplo de Estructura

```yaml
document_types:
  - victima_directa
  - familiar
actors:
  grupos_armados:
    - FARC
    - AUC
events:
  desaparicion:
    - desaparicion_forzada
territorio:
  region:
    - Antioquia
    - Meta
```

## 3. Diagrama de Ontología

<div class="mermaid">
flowchart TD
    A[Ontología] --> B[Tipos de Documento]
    A --> C[Actores]
    A --> D[Hechos]
    A --> E[Territorio]
</div>
