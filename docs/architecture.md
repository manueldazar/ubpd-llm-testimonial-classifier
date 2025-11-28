---
layout: default
title: Architecture / Arquitectura – UBPD LLM Classifier
---

# Architecture / Arquitectura

[English](#english-version) · [Español](#spanish-version)

---

# English Version {#english-version}

## 1. High-Level Overview

This classifier is a modular LLM-based system designed for structured extraction of information from testimonial documents.

---

## 2. Component Breakdown

- Preprocessing layer  
- Ontology loader  
- Prompt builder  
- LLM client  
- JSON parser and validator  

---

## 3. Detailed Diagram

<div class="mermaid">
flowchart TD
    A[Testimonial Input] --> B[Preprocessing]
    B --> C[Ontology Loader]
    C --> D[Prompt Builder]
    D --> E[LLM Client]
    E --> F[JSON Parser]
    F --> G[Validator]
    G --> H[Structured Output]
</div>

---

# Versión en Español {#spanish-version}

## 1. Visión General

El clasificador está diseñado como un sistema modular para extraer información estructurada de testimonios.

---

## 2. Componentes

- Capa de preprocesamiento  
- Cargador de ontología  
- Constructor de prompts  
- Cliente LLM  
- Parser y validador JSON  

---

## 3. Diagrama

<div class="mermaid">
flowchart TD
    A[Texto Testimonial] --> B[Preprocesamiento]
    B --> C[Cargador de Ontología]
    C --> D[Constructor de Prompts]
    D --> E[Cliente LLM]
    E --> F[Parser JSON]
    F --> G[Validador]
    G --> H[Salida Estructurada]
</div>
