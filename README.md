# Demo – UBPD: Testimonial Document Classifier with LLM  
# Demo – UBPD: Clasificador de documentos testimoniales con LLM

---

## 🇺🇸 English Version

### Overview

This repository contains a prototype LLM-based classifier for testimonial documents from the **Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)** in Colombia.  
The system loads a UBPD ontology defined in YAML, builds structured system/user prompts, and forces the model to return a controlled JSON output with the following fields:

- Document type  
- Types of events  
- Actors  
- Time period  
- Territory  
- Priority / internal routing  

This prototype demonstrates how LLMs can support early‑stage analysis of testimonial documents in contexts of enforced disappearance, transitional justice, and humanitarian search processes.

---

### Technical Architecture

- **`notebooks/UBPD_Demo_Clasificador_Testimonios_autor.ipynb`** – Interactive demo.  
- **`src/ubpd_classifier/`:**  
  - `preprocessing.py` – Basic text normalization.  
  - `ontology.py` – Loads ontology from `ontology_ubpd.yaml`.  
  - `prompts.py` – Builds system/user prompts from YAML structure.  
  - `classifier.py` – Implements `classify_document(text)` and JSON validation.  
- **`data/ontology/ontology_ubpd.yaml`** – Controlled vocabulary and categories.

---

### Requirements

```bash
pip install -r requirements.txt
```

Environment variables (`.env.example`):

```text
OPENAI_API_KEY=your_key_here
```

---

### Quick Start

```python
from ubpd_classifier.classifier import classify_document

sample = """My brother disappeared in 1997 in rural Antioquia..."""
pred = classify_document(sample)
print(pred)
```

For the notebook demo:

1. Start Jupyter or VS Code.  
2. Open `notebooks/UBPD_Demo_Clasificador_Testimonios_autor.ipynb`.  
3. Configure `.env` with your API key.  
4. Run cells until the example output.

---

### Project Status

This project is a **working demo** for exploring how LLMs can help classify testimonial documents in search-for-disappeared-persons contexts.  
It is **not** a production system.

Next steps:

- Improve validation rules and priority heuristics.  
- Connect to a document store or DB.  
- Add evaluation metrics using an annotated dataset.  
- Experiment with Spanish‑legal domain embeddings.  
- Add a small RAG pipeline for cross‑document consistency checks.

---

### Extended Documentation

#### 1. Ontology Design  
The YAML ontology includes controlled vocabularies for:  
- Document types  
- Event categories  
- Actor categories  
- Known time periods (pre‑conflict, conflict peaks, post‑agreement)  
- Administrative/geographical divisions  

YAML is used because it is readable, editable, and easy to serialize into prompts.

#### 2. Prompt Engineering Strategy  
The prompt is divided into:  
- **System prompt:**  
  - Defines strict JSON format  
  - Enforces allowed labels from ontology  
  - Describes the classifier's responsibilities  

- **User prompt:**  
  - Contains the testimonial text  
  - Requests classification in the defined schema  

A deterministic JSON format is enforced to make downstream processing easier.

#### 3. Evaluation Strategy (Future Work)  
Once an annotated dataset exists:  
- Precision/recall per category  
- Confusion matrices for overlapping classes  
- Agreement analysis between LLM and human annotators  
- Stress tests with noisy or incomplete testimonies  

#### 4. Data Governance Considerations  
Although this demo uses synthetic text, a real system must incorporate:  
- Privacy protection  
- Data minimization  
- Secure handling of sensitive victim information  
- Audit logs for transparency  
- Human‑in‑the‑loop verification  

These considerations make the project aligned with responsible AI practices.

---

---

## 🇪🇸 Versión en Español

### Descripción general

Este repositorio contiene un prototipo de clasificador de documentos testimoniales desarrollado para la **Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)**.  
El sistema carga una ontología definida en YAML, construye prompts estructurados (system + user) y fuerza al modelo a devolver un JSON con valores controlados, incluyendo:

- Tipo de documento  
- Tipos de hechos  
- Actores  
- Periodo temporal  
- Territorio  
- Prioridad / ruteo interno  

Este prototipo ilustra cómo los LLM pueden apoyar el análisis preliminar de testimonios en contextos de desaparición, justicia transicional y búsqueda humanitaria.

---

### Arquitectura técnica

- **`notebooks/UBPD_Demo_Clasificador_Testimonios_autor.ipynb`** – Demo interactiva.  
- **`src/ubpd_classifier/`:**  
  - `preprocessing.py` – Normalización básica del texto.  
  - `ontology.py` – Carga la ontología desde `ontology_ubpd.yaml`.  
  - `prompts.py` – Construcción de prompts system/user a partir de la ontología.  
  - `classifier.py` – Implementación de `classify_document(text)` y validación JSON.  
- **`data/ontology/ontology_ubpd.yaml`** – Ontología y vocabulario controlado.

---

### Requisitos

```bash
pip install -r requirements.txt
```

Variables de entorno (`.env.example`):

```text
OPENAI_API_KEY=tu_api_key_aqui
```

---

### Uso rápido

```python
from ubpd_classifier.classifier import classify_document

testimonio = """Mi hermano desapareció en 1997 en una vereda de Antioquia..."""
pred = classify_document(testimonio)
print(pred)
```

Para usar el notebook:

1. Iniciar Jupyter o VS Code.  
2. Abrir `notebooks/UBPD_Demo_Clasificador_Testimonios_autor.ipynb`.  
3. Configurar `.env` con tu API key.  
4. Ejecutar las celdas del ejemplo.

---

### Estado del proyecto

Este repositorio es una **demo funcional** para explorar el uso de LLMs en la clasificación de testimonios en contextos de desaparición forzada.  
No es un sistema de producción.

Próximos pasos:

- Mejorar reglas de validación y lógica de prioridad.  
- Conectar con un sistema de documentos o base de datos.  
- Crear un conjunto de datos anotado.  
- Añadir métricas de evaluación.  
- Explorar embeddings legales especializados.  
- Implementar un mini‑RAG para consistencia entre testimonios.

---

### Documentación ampliada

#### 1. Diseño de la ontología  
La ontología en YAML incluye vocabularios controlados para:  
- Tipos de documentos  
- Categorías de hechos  
- Categorías de actores  
- Periodos temporales  
- Divisiones territoriales  

YAML facilita edición, lectura y serialización.

#### 2. Estrategia de prompt engineering  
El prompt está dividido en:  
- **System prompt:**  
  - Define el formato JSON obligatorio  
  - Establece etiquetas permitidas según la ontología  
  - Indica las funciones del clasificador  

- **User prompt:**  
  - Contiene el texto testimonial  
  - Solicita el análisis en el esquema predefinido  

El JSON estricto facilita la integración con sistemas posteriores.

#### 3. Estrategia de evaluación (futuro)  
Tras obtener datos anotados:  
- Precisión/recobrado por categoría  
- Matrices de confusión  
- Análisis de concordancia humano–LLM  
- Pruebas con textos ruidosos o incompletos  

#### 4. Consideraciones de gobernanza de datos  
Aunque el demo usa texto sintético, un sistema real requiere:  
- Protección de datos sensibles  
- Minimización de datos personales  
- Manejo seguro de testimonios  
- Trazabilidad y auditoría  
- Validación humana obligatoria  


