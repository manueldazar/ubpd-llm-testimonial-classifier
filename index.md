---
layout: default
title: LLM Testimonial Classifier – Project Overview
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

This is a **YAML-driven LLM classifier.** This could be useful for human rights or justice organizations.*.

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

<form id="demo-form-full">
  <label><strong>Testimonial Text</strong></label><br>
  <textarea id="demo-text-full" rows="8" style="width:100%;"></textarea><br><br>

  <button type="button" id="demo-run-full">Run Classifier (Mock)</button>
</form>

<pre id="demo-output-full" style="margin-top:1rem;">
{
  "document_type": null,
  "actors": [],
  "events": [],
  "territory": {
    "region": null,
    "rurality": null
  },
  "time_period": null,
  "priority": null
}
</pre>

<script>
  (function() {
    const ontology = {
      document_types: ["victim_direct", "family_member", "witness", "institutional_document"],

      armed_groups: ["FARC", "AUC", "ELN", "Public Forces"],
      victims: ["direct_victim", "indirect_victim", "community"],

      events: {
        disappearance: ["forced_disappearance", "kidnapping"],
        violence: ["homicide", "torture", "threats"]
      },

      regions: ["Antioquia", "Meta", "Cauca", "Norte de Santander"],
      rurality: ["rural", "urban", "mixed"],

      time_periods: ["1980–1990", "1990–2000", "2000–2010", "2010–2020"]
    };

    function matchFromText(text, list) {
      text = text.toLowerCase();
      return list.filter(item => text.includes(item.toLowerCase()));
    }

    document.getElementById("demo-run-full").addEventListener("click", function() {
      const txt = (document.getElementById("demo-text-full").value || "").toLowerCase();

      let result = {
        document_type: "victim_direct",    // default assumption
        actors: [],
        events: [],
        territory: { region: null, rurality: null },
        time_period: null,
        priority: "medium"
      };

      // 1. Actors
      result.actors.push(...matchFromText(txt, ontology.armed_groups));
      result.actors.push(...matchFromText(txt, ontology.victims));

      // 2. Events
      for (const category in ontology.events) {
        result.events.push(...matchFromText(txt, ontology.events[category]));
      }

      // 3. Territory (simple heuristics)
      result.territory.region = ontology.regions.find(r => txt.includes(r.toLowerCase())) || null;
      result.territory.rurality = ontology.rurality.find(r => txt.includes(r)) || null;

      // 4. Time period (approx heuristic)
      if (txt.match(/199\d/)) result.time_period = "1990–2000";
      if (txt.match(/200\d/)) result.time_period = "2000–2010";

      // 5. Priority (simulate)
      if (txt.includes("desapar") || txt.includes("missing")) result.priority = "high";
      if (txt.includes("homicid")) result.priority = "high";

      document.getElementById("demo-output-full").textContent =
        JSON.stringify(result, null, 2);
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

Este repositorio presenta un **clasificador basado en LLM** y guiado por una ontología YAML, diseñado para apoyar tareas de análisis de testimonios.

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
- Aplica una salida determinista  

### User Prompt
- Contiene el texto testimonial  
- Solicita clasificación únicamente dentro del esquema JSON  
- Evita la ambiguedad o las instrucciones abiertas  

---

## 4. Estrategia de Evaluación

Una vez disponible un conjunto de datos etiquetado, el clasificador puede evaluarse mediante:

- **Precisión/Recuperación por categoría**  
- **Matrices de confusión para clases superpuestas**  
- **Concordancia entre anotadores LLM y codificadores humanos**  
- **Pruebas de estrés  con testimonios ruidosos, incompletos o contradictorios** 
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

<form id="demo-form-es-full">
  <label><strong>Texto del testimonio</strong></label><br>
  <textarea id="demo-text-es-full" rows="8" style="width:100%;"></textarea><br><br>

  <button type="button" id="demo-run-es-full">Ejecutar Clasificador (Simulación)</button>
</form>

<pre id="demo-output-es-full" style="margin-top:1rem;">
{
  "tipo_documento": null,
  "actores": [],
  "hechos": [],
  "territorio": {
    "region": null,
    "ruralidad": null
  },
  "periodo": null,
  "prioridad": null
}
</pre>

<script>
  (function() {
    const ont = {
      tipos: ["victima_directa", "familiar", "testigo", "documento_institucional"],

      grupos_armados: ["FARC", "AUC", "ELN", "Fuerza Pública"],
      victimas: ["victima_directa", "victima_indirecta", "comunidad"],

      hechos: {
        desaparicion: ["desaparicion_forzada", "secuestro"],
        violencia: ["homicidio", "tortura", "amenazas"]
      },

      regiones: ["Antioquia", "Meta", "Cauca", "Norte de Santander"],
      ruralidad: ["rural", "urbano", "mixto"],

      periodos: ["1980–1990", "1990–2000", "2000–2010", "2010–2020"]
    };

    function match(text, list) {
      text = text.toLowerCase();
      return list.filter(item => text.includes(item.toLowerCase()));
    }

    document.getElementById("demo-run-es-full").addEventListener("click", function() {
      const txt = (document.getElementById("demo-text-es-full").value || "").toLowerCase();

      let out = {
        tipo_documento: "victima_directa",
        actores: [],
        hechos: [],
        territorio: { region: null, ruralidad: null },
        periodo: null,
        prioridad: "media"
      };

      // Actores
      out.actores.push(...match(txt, ont.grupos_armados));
      out.actores.push(...match(txt, ont.victimas));

      // Hechos
      for (const cat in ont.hechos) {
        out.hechos.push(...match(txt, ont.hechos[cat]));
      }

      // Territorio
      out.territorio.region = ont.regiones.find(r => txt.includes(r.toLowerCase())) || null;
      out.territorio.ruralidad = ont.ruralidad.find(r => txt.includes(r)) || null;

      // Periodo
      if (txt.match(/199\d/)) out.periodo = "1990–2000";
      if (txt.match(/200\d/)) out.periodo = "2000–2010";

      // Prioridad
      if (txt.includes("desapar") || txt.includes("perdido")) out.prioridad = "alta";
      if (txt.includes("homicid")) out.prioridad = "alta";

      document.getElementById("demo-output-es-full").textContent =
        JSON.stringify(out, null, 2);
    });
  })();
</script>

---

## 7. Documentación

- [Arquitectura](docs/architecture.html)  
- [Ontología](docs/ontology.html)  
- [API](docs/api.html)  
- [Pruebas](docs/tests/index.html)  
