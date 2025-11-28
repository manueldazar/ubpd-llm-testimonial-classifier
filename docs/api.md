---
layout: default
title: API – UBPD LLM Classifier
---

# API – UBPD LLM Classifier

[English](#english-version) · [Español](#spanish-version)

---

# English Version {#english-version}

## 1. Python API (Library Style)

### classify_document(text: str) -> dict

```python
from ubpd_classifier.classifier import classify_document

with open("example_testimony.txt", "r", encoding="utf-8") as f:
    text = f.read()

result = classify_document(text)
print(result)
```

Expected output (simplified):

```json
{
  "document_type": "victim_direct",
  "actors": ["FARC"],
  "events": ["forced_disappearance"],
  "territory": {
    "region": "Antioquia",
    "rurality": "rural"
  },
  "priority": "high"
}
```

## 2. CLI Usage (Runner)

```bash
python -m ubpd_classifier.runner --file path/to/testimony.txt
```

Options (example):

- `--file` – input file with testimonial text  
- `--output` – optional JSON file to write results  

---

# Versión en Español {#spanish-version}

## 1. API Python (Estilo Librería)

### classify_document(text: str) -> dict

```python
from ubpd_classifier.classifier import classify_document

with open("ejemplo_testimonio.txt", "r", encoding="utf-8") as f:
    text = f.read()

resultado = classify_document(text)
print(resultado)
```

Salida esperada (simplificada):

```json
{
  "tipo_documento": "victima_directa",
  "actores": ["FARC"],
  "hechos": ["desaparicion_forzada"],
  "territorio": {
    "region": "Antioquia",
    "ruralidad": "rural"
  },
  "prioridad": "alta"
}
```

## 2. Uso por Línea de Comando (Runner)

```bash
python -m ubpd_classifier.runner --file ruta/al/testimonio.txt
```

Opciones (ejemplo):

- `--file` – archivo de entrada con el testimonio  
- `--output` – archivo JSON opcional para guardar resultados  
