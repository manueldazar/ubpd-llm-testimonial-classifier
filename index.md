---
layout: default
title: UBPD LLM Testimonial Classifier – Project Overview
---

# UBPD LLM Testimonial Classifier  
**Bilingual Project Site (English / Español)**  

<p class="badge-row">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Status: active">
  <img src="https://img.shields.io/badge/LLM-GPT--4.1-blue" alt="LLM: GPT-4.1">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="License: MIT">
</p>

[English](#english-version) · [Español](#spanish-version)

---

# English Version {#english-version}

## 1. What This Project Does

This is a **YAML-driven LLM classifier** aligned with the workflows of the *Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)*.

The system:

- Ingests testimonial or narrative text  
- Applies preprocessing  
- Injects ontology categories into prompts  
- Calls an LLM with strict JSON expectations  
- Validates against controlled vocabularies  
- Returns a structured classification suitable for dashboards, audits, or routing  

---

## 2. High-Level Diagram

<div class="mermaid">
flowchart TD
    A[Testimonial Input] --> B[Preprocessing]
    B --> C[Ontology Loader]
    C --> D[Prompt Builder]
    D --> E[LLM Client]
    E --> F[JSON Decoder + Validation]
    F --> G[Structured Output]
</div>

---

## 3. Prompt Engineering Strategy

The system uses a **two-layer structured prompt**:

### System Prompt
- Defines a strict JSON schema  
- Injects ontology categories (actors, events, document types, etc.)  
- Describes classification responsibilities  
- Enforces deterministic output  

### User Prompt
- Contains the testimonial text  
- Requests classification strictly in the defined JSON format  
- Avoids ambiguity or open-ended instructions  

---

## 4. Evaluation Strategy (Future Work)

Once a labeled dataset is available, the classifier can be evaluated using:

- **Precision / Recall per category**  
- **Confusion matrices** for overlapping classes  
- **Inter-annotator agreement** between LLM and human coders  
- **Stress tests** using noisy, incomplete, or conflicting testimonies  

---

## 5. Data Governance Considerations

A production-grade system must include:

- **Privacy protection** for sensitive personal information  
- **Data minimization**  
- **Secure storage and access control**  
- **Audit logs** for transparency and accountability  
- **Human-in-the-loop verification** for critical decisions  

---

## 6. Try the Classifier Online (Interactive Mockup)

> This page is a **front-end mockup**. It does not call real APIs yet, but it illustrates how a future web demo could work.

<form id="demo-form">
  <label for="demo-text"><strong>Testimonial Text</strong></label><br>
  <textarea id="demo-text" name="demo-text" rows="7" style="width:100%;"></textarea><br><br>
  <button type="button" id="demo-run">Run Classifier (Mock)</button>
</form>

<pre id="demo-output" style="margin-top:1rem;">
{
  "document_type": null,
  "actors": [],
  "events": [],
  "territory": {},
  "priority": null
}
</pre>

<script>
  (function() {
    var btn = document.getElementById('demo-run');
    var txt = document.getElementById('demo-text');
    var out = document.getElementById('demo-output');
    if (!btn || !txt || !out) return;

    btn.addEventListener('click', function() {
      var text = (txt.value || "").toLowerCase();
      var result = {
        document_type: "unknown",
        actors: [],
        events: [],
        territory: {},
        priority: "medium"
      };

      if (text.includes("desapar") || text.includes("missing")) {
        result.events.push("forced_disappearance");
        result.priority = "high";
      }
      if (text.includes("farc")) {
        result.actors.push("FARC");
      }
      if (text.includes("auc")) {
        result.actors.push("AUC");
      }

      out.textContent = JSON.stringify(result, null, 2);
    });
  })();
</script>

---

## 7. Documentation

- [Architecture](docs/architecture.html)  
- [Ontology](docs/ontology.html)  
- [API](docs/api.html)  
- [Tests Overview](docs/tests/index.html)  

---

# Versión en Español {#spanish-version}

## 1. Qué Hace Este Proyecto

Este repositorio presenta un **clasificador basado en LLM** y guiado por una ontología YAML, diseñado para apoyar tareas de análisis de testimonios en la **UBPD**.

---

## 2. Diagrama General

<div class="mermaid">
flowchart TD
    A[Texto Testimonial] --> B[Preprocesamiento]
    B --> C[Cargador de Ontología]
    C --> D[Constructor de Prompts]
    D --> E[Cliente LLM]
    E --> F[Decodificador + Validación JSON]
    F --> G[Salida Estructurada]
</div>

---

## 3. Estrategia de Prompt Engineering

### System Prompt
- Define un esquema JSON estricto  
- Incluye todas las etiquetas de la ontología  
- Describe responsabilidades del clasificador  
- Minimiza ambigüedad  

### User Prompt
- Contiene el texto testimonial  
- Solicita clasificación únicamente dentro del esquema JSON  
- Evita instrucciones abiertas  

---

## 4. Estrategia de Evaluación

Con un conjunto de datos anotado, se podrán calcular:

- **Precisión / Recall por categoría**  
- **Matrices de confusión**  
- **Acuerdo entre LLM y anotadores humanos**  
- **Pruebas de estrés** con testimonios ruidosos o incompletos  

---

## 5. Gobernanza de Datos

Una versión real del sistema debe incorporar:

- **Protección de privacidad**  
- **Minimización de datos**  
- **Manejo seguro de información sensible**  
- **Registros de auditoría**  
- **Supervisión humana** en decisiones críticas  

---

## 6. Probar el Clasificador (Mockup)

Esta página ilustra cómo podría verse una futura **demo web**, sin exponer datos reales ni claves de API.

---

## 7. Documentación

- [Arquitectura](docs/architecture.html)  
- [Ontología](docs/ontology.html)  
- [API](docs/api.html)  
- [Pruebas](docs/tests/index.html)  
