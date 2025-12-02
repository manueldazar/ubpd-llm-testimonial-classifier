# LLM Testimonial Classifier

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?logo=openai&logoColor=white)](https://openai.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-See_Terms-orange)](LICENSE)

**Clasificador automático de documentos testimoniales para organizaciones de derechos humanos**

*Automatic testimonial document classifier for human rights organizations*

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Casos de Uso](#-casos-de-uso)
- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Ontología de Clasificación](#-ontología-de-clasificación)
- [Base de Datos](#-base-de-datos)
- [API de Módulos](#-api-de-módulos)
- [Personalización](#-personalización)
- [Próximos Pasos](#-próximos-pasos)
- [Crédito Intelectual y Procedencia](#-crédito-intelectual-y-procedencia)
- [Autor](#-autor)

---

## 📖 Descripción

Sistema de **clasificación automática de documentos testimoniales** utilizando Modelos de Lenguaje (LLM) con ontología controlada. Diseñado para organizaciones de derechos humanos, comisiones de la verdad, fiscalías especializadas y entidades que procesan testimonios relacionados con conflictos armados, violaciones de derechos humanos o justicia transicional.

### El Problema

| Desafío | Descripción |
|---------|-------------|
| **Alto volumen** | Miles de testimonios pendientes de clasificación |
| **Inconsistencia** | Variabilidad en criterios entre analistas |
| **Tiempo limitado** | Recursos humanos escasos para tareas repetitivas |
| **Priorización** | Dificultad para identificar casos urgentes |

### La Solución

Un sistema que combina **GPT-4o** con una **ontología controlada y personalizable** para:

- ✅ Clasificar documentos automáticamente en múltiples dimensiones
- ✅ Garantizar consistencia mediante vocabularios estandarizados
- ✅ Calcular scores de prioridad para enrutamiento de casos
- ✅ Extraer fragmentos clave (highlights) para análisis humano
- ✅ Persistir resultados en PostgreSQL para auditoría

---

## 🎯 Casos de Uso

Este clasificador puede ser utilizado por:

| Organización | Aplicación |
|--------------|------------|
| **Comisiones de la Verdad** | Procesamiento de testimonios de víctimas y testigos |
| **Fiscalías Especializadas** | Clasificación de declaraciones en casos de lesa humanidad |
| **ONGs de Derechos Humanos** | Análisis de denuncias y reportes de campo |
| **Unidades de Búsqueda** | Priorización de casos de personas desaparecidas |
| **Tribunales de Justicia Transicional** | Categorización de evidencia testimonial |
| **Organizaciones Internacionales** | Procesamiento de documentación humanitaria |

---

## ✨ Características

- **Clasificación multi-etiqueta**: Tipo de documento, hechos, actores, territorio, período
- **Ontología YAML extensible**: Fácil de personalizar para diferentes contextos
- **Validación automática**: Corrección de códigos inválidos con valores por defecto
- **Score de prioridad**: Cálculo automático para enrutamiento de casos
- **Persistencia PostgreSQL**: Esquema normalizado para análisis y auditoría
- **CLI completo**: Ejecución desde terminal con múltiples opciones
- **Soporte Conda/pip**: Instalación flexible para diferentes entornos

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PIPELINE DE CLASIFICACIÓN                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐   │
│  │  Documento   │───▶│preprocessing │───▶│     prompts.py       │   │
│  │  Testimonial │    │     .py      │    │  (System + Few-shot) │   │
│  └──────────────┘    └──────────────┘    └──────────┬───────────┘   │
│                                                      │               │
│                                                      ▼               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐   │
│  │  PostgreSQL  │◀───│    db.py     │◀───│    classifier.py     │   │
│  │   Database   │    │ (Persistir)  │    │  (LLM + Validación)  │   │
│  └──────────────┘    └──────────────┘    └──────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Flujo de Datos

1. **Entrada**: Texto crudo del documento testimonial
2. **Preprocesamiento**: Normalización Unicode, limpieza de espacios
3. **Prompt Engineering**: Inyección de ontología + ejemplos few-shot
4. **Clasificación LLM**: Llamada a GPT-4o con temperature=0
5. **Validación**: Verificación contra ontología + reglas de negocio
6. **Enriquecimiento**: Cálculo de priority_score
7. **Persistencia**: Almacenamiento en PostgreSQL (opcional)

---

## 📁 Estructura del Proyecto

```
llm-testimonial-classifier/
│
├── src/
│   ├── classifier.py        # Pipeline principal de clasificación
│   ├── db.py                 # Conexión y persistencia PostgreSQL
│   ├── ontology.py           # Carga de ontología YAML
│   ├── preprocessing.py      # Limpieza y normalización de texto
│   ├── prompts.py            # System prompt y templates few-shot
│   └── runner.py             # CLI para ejecución desde terminal
│
├── ontology.yaml             # Ontología de clasificación (personalizable)
├── requirements.txt          # Dependencias pip
├── environment.yml           # Entorno Conda (Windows)
├── .env.example              # Plantilla de variables de entorno
│
├── run-classifier-conda.ps1  # Script PowerShell (Conda)
├── run-classifier-gui.ps1    # Script PowerShell (GUI)
│
├── notebooks/
│   └── Demo_Clasificador_Testimonios.ipynb
│
├── docs/                     # Documentación Jekyll
│   ├── architecture.html
│   ├── ontology.html
│   ├── api.html
│   └── demo.html
│
├── _config.yml               # Configuración GitHub Pages
├── index.md                  # Homepage del sitio
└── README.md                 # Este archivo
```

---

## 🔧 Instalación

### Prerrequisitos

- Python 3.9+ (recomendado 3.13)
- PostgreSQL 14+ (opcional, para persistencia)
- API Key de OpenAI

### Opción A: pip (Linux/Mac/Windows)

```bash
# Clonar repositorio
git clone https://github.com/manueldazar/llm-testimonial-classifier.git
cd llm-testimonial-classifier

# Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Opción B: Conda (Windows)

```bash
# Clonar repositorio
git clone https://github.com/manueldazar/llm-testimonial-classifier.git
cd llm-testimonial-classifier

# Crear entorno desde environment.yml
conda env create -f environment.yml

# Activar entorno
conda activate classifier_env
```

### Dependencias Principales

| Paquete | Propósito |
|---------|-----------|
| `openai` | Cliente API OpenAI |
| `pyyaml` | Parser de ontología YAML |
| `psycopg2-binary` | Driver PostgreSQL |
| `python-dotenv` | Variables de entorno |
| `fastapi` | API REST (opcional) |
| `uvicorn` | Servidor ASGI (opcional) |

---

## ⚙️ Configuración

### Variables de Entorno

Crear archivo `.env` en el directorio raíz:

```env
# === OpenAI API ===
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx

# === PostgreSQL (opcional) ===
DB_HOST=localhost
DB_PORT=5432
DB_NAME=testimonials
DB_USER=classifier
DB_PASSWORD=tu_password_seguro
```

> ⚠️ **Nunca commitear el archivo `.env` a Git**

### Inicializar Base de Datos (Opcional)

```bash
# Crear tablas en PostgreSQL
python src/db.py create-tables
```

---

## 🚀 Uso

### Opción 1: Línea de Comandos (CLI)

```bash
# Clasificar texto directo (sin guardar en BD)
python src/runner.py --text "El testigo declara que en 1998..." --no-db

# Clasificar desde archivo
python src/runner.py --file documento.txt --no-db

# Clasificar y guardar en PostgreSQL
python src/runner.py --file documento.txt

# Con metadatos adicionales
python src/runner.py --file doc.txt --external-id "CASO-2024-001" --source-system "ARCHIVO"
```

### Opción 2: Como Módulo Python

```python
from classifier import classify_document

testimonio = """
Yo, María, declaro que en 1997, en el municipio de San Carlos, 
hombres armados se llevaron a mi esposo. Desde ese día no volvimos 
a saber de él. Después comenzaron las amenazas y tuvimos que 
desplazarnos a la ciudad.
"""

resultado = classify_document(testimonio)
print(resultado)
```

### Opción 3: Notebook Jupyter

```bash
jupyter lab notebooks/Demo_Clasificador_Testimonios.ipynb
```

### Resultado Esperado

```json
{
  "tipo_documento": "TD1",
  "tipo_hecho": ["TH1", "TH3"],
  "territorio": ["Antioquia"],
  "periodo": "PER2",
  "actores": ["ACT2"],
  "ruteo": "RU1",
  "highlights": [
    "1997, en el municipio de San Carlos",
    "se llevaron a mi esposo"
  ],
  "priority_score": 0.7
}
```

---

## 📚 Ontología de Clasificación

La ontología define el vocabulario controlado. Se carga desde `ontology.yaml` y es completamente personalizable.

### Tipo de Documento (`tipo_documento`)

| Código | Descripción |
|--------|-------------|
| TD0 | No testimonial |
| TD1 | Testimonio de víctima directa |
| TD2 | Testimonio de familiar o persona buscadora |
| TD3 | Testimonio de exintegrante de grupo armado |
| TD4 | Testimonio de tercero testigo |

### Tipo de Hecho (`tipo_hecho`)

| Código | Descripción |
|--------|-------------|
| TH1 | Desaparición forzada |
| TH2 | Homicidio |
| TH3 | Desplazamiento forzado |
| TH4 | Violencia sexual |
| TH5 | Reclutamiento de menores |
| TH6 | Tortura o tratos crueles |
| TH7 | Otros hechos relevantes |

### Actores (`actores`)

| Código | Descripción |
|--------|-------------|
| ACT0 | No aparece actor |
| ACT1 | Fuerza Pública o agentes estatales |
| ACT2 | Guerrillas |
| ACT3 | Paramilitares / AUC |
| ACT4 | Grupos posdesmovilización / BACRIM |
| ACT5 | Actor no identificado |

### Período (`periodo`)

| Código | Descripción |
|--------|-------------|
| PER0 | No identificado |
| PER1 | 1985-1990 |
| PER2 | 1991-2000 |
| PER3 | 2001-2010 |
| PER4 | 2011-2016 |
| PER5 | 2017-2025 |

### Ruteo (`ruteo`)

| Código | Descripción |
|--------|-------------|
| RU0 | No aplica |
| RU1 | Búsqueda e identificación |
| RU2 | Esclarecimiento y patrones |
| RU3 | Atención psicosocial |
| RU4 | No prioritario |

---

## 🗄️ Base de Datos

### Esquema Relacional

```
┌─────────────────────┐
│   doc_document      │──────┐
│   (documento base)  │      │
└─────────────────────┘      │
                             │ 1:N
┌─────────────────────┐      │
│ doc_classification_ │◀─────┘
│ run (ejecución)     │──────┬──────┬──────┬──────┐
└─────────────────────┘      │      │      │      │
                             │      │      │      │
    ┌────────────────────────┼──────┼──────┼──────┼────────────────┐
    │                        │      │      │      │                │
    ▼                        ▼      ▼      ▼      ▼                ▼
┌────────┐  ┌────────┐  ┌────────┐ ┌────────┐ ┌────────┐  ┌────────────┐
│_labels │  │ _hecho │  │ _terr  │ │ _actor │ │ _high  │  │  raw_json  │
│ (1:1)  │  │ (1:N)  │  │ (1:N)  │ │ (1:N)  │ │ (1:N)  │  │  (JSONB)   │
└────────┘  └────────┘  └────────┘ └────────┘ └────────┘  └────────────┘
```

### Tablas Principales

| Tabla | Descripción |
|-------|-------------|
| `doc_document` | Documento original con texto y metadatos |
| `doc_classification_run` | Ejecución de clasificación (modelo, timestamp) |
| `doc_classification_labels` | Etiquetas simples + priority_score |
| `doc_classification_hecho` | Hechos victimizantes (multi-etiqueta) |
| `doc_classification_territorio` | Territorios (multi-etiqueta) |
| `doc_classification_actor` | Actores (multi-etiqueta) |
| `doc_classification_highlight` | Fragmentos destacados |

---

## 🔌 API de Módulos

### `preprocessing.py`

| Función | Descripción |
|---------|-------------|
| `normalize_unicode(text)` | Normaliza caracteres a forma NFC |
| `collapse_spaces(text)` | Reduce espacios múltiples |
| `preprocess_text(text)` | Pipeline completo de limpieza |

### `ontology.py`

| Función | Descripción |
|---------|-------------|
| `load_ontology(path)` | Carga YAML a diccionario Python |
| `ontology_to_prompt_text(ontology)` | Serializa para incluir en prompts |

### `prompts.py`

| Elemento | Descripción |
|----------|-------------|
| `SYSTEM_PROMPT` | Prompt de sistema con ontología y reglas |
| `USER_TEMPLATE` | Template con ejemplos few-shot |
| `build_user_prompt(text)` | Construye prompt con documento |

### `classifier.py`

| Función | Descripción |
|---------|-------------|
| `call_llm(system, user)` | Llamada a OpenAI API |
| `parse_model_response(raw)` | Extracción segura de JSON |
| `validate_and_fix(pred)` | Validación contra ontología |
| `compute_priority(pred)` | Cálculo de priority_score |
| `classify_document(text)` | **Función principal** |

### `db.py`

| Función | Descripción |
|---------|-------------|
| `get_connection()` | Conexión a PostgreSQL |
| `create_tables()` | Inicialización de esquema |
| `save_document_and_classification()` | Persistir documento + clasificación |

---

## 🎨 Personalización

### Modificar la Ontología

Editar `ontology.yaml` para adaptar a tu contexto:

```yaml
tipo_hecho:
  TH1: "Desaparición forzada"
  TH2: "Homicidio"
  TH8: "Nuevo tipo de hecho"  # Agregar nuevos códigos

territorio:
  departments:
    - "Tu Región 1"
    - "Tu Región 2"
```

### Ajustar Pesos de Prioridad

En `classifier.py`, modificar `compute_priority()`:

```python
def compute_priority(pred: dict) -> float:
    score = 0.0
    hechos = set(pred.get("tipo_hecho", []))
    
    if "TH1" in hechos:  # Desaparición forzada
        score += 0.4    # Ajustar peso según necesidad
    # ...
```

### Cambiar Modelo LLM

En `classifier.py`:

```python
MODEL_NAME = "gpt-4o"        # Por defecto
# MODEL_NAME = "gpt-4-turbo"  # Mayor capacidad
# MODEL_NAME = "gpt-3.5-turbo"  # Más económico
```

---

## 📈 Próximos Pasos

### Corto plazo
- [ ] Retry logic y manejo de rate limits
- [ ] Logging estructurado (JSON)
- [ ] Más ejemplos few-shot para casos límite

### Mediano plazo
- [ ] Batch processing para múltiples documentos
- [ ] API REST con FastAPI
- [ ] Dashboard de monitoreo
- [ ] Métricas de calidad (accuracy, F1)

### Largo plazo
- [ ] Fine-tuning con datos etiquetados
- [ ] Explicabilidad de clasificaciones
- [ ] Búsqueda semántica con embeddings
- [ ] Soporte multi-idioma

---

## 📜 Crédito Intelectual y Procedencia

### Español

Este proyecto —incluyendo su arquitectura, el diseño de la ontología, la estrategia de prompt engineering, el plan de evaluación y la implementación de referencia— fue concebido, diseñado y desarrollado por **Manuel Daza**. Todos los componentes conceptuales (formulación del problema, justificación del esquema de datos, ontología de clasificación, plantillas de prompt, criterios de evaluación y flujos del demostrador) se originan en este repositorio y en su historial de commits.

El código, la documentación y el enfoque metodológico se publican para ofrecer transparencia y fomentar una discusión responsable, y **no constituyen autorización implícita** para uso institucional, trabajo derivado con fines comerciales o despliegue operativo. Cualquier reutilización, adaptación o implementación institucional debe reconocer explícitamente al autor original y cumplir con la licencia del proyecto.

**Si este proyecto se cita, referencia o utiliza como base para desarrollos posteriores, incluya la siguiente atribución:**

> **Manuel Daza** — Autor y Arquitecto Original  
> GitHub: [https://github.com/manueldazar](https://github.com/manueldazar)  
> URL del proyecto: [https://github.com/manueldazar/llm-testimonial-classifier](https://github.com/manueldazar/llm-testimonial-classifier)

Para colaboración, pilotos o acompañamiento en la implementación, por favor contacte directamente al autor.

---

### English — Intellectual Credit and Provenance

This project —including its architecture, ontology design, prompt engineering strategy, evaluation plan, and reference implementation— was conceived, designed, and developed by **Manuel Daza**. All conceptual components (problem formulation, data schema rationale, classification ontology, prompt templates, evaluation criteria, and demonstrator workflows) originate in this repository and its commit history.

The code, documentation, and methodological approach are published to provide transparency and encourage responsible discussion, and **do not constitute implicit authorization** for institutional use, commercial derivative work, or operational deployment. Any reuse, adaptation, or institutional implementation must explicitly acknowledge the original author and comply with the project license.

**If this project is cited, referenced, or used as a basis for further development, please include the following attribution:**

> **Manuel Daza** — Original Author and Architect  
> GitHub: [https://github.com/manueldazar](https://github.com/manueldazar)  
> Project URL: [https://github.com/manueldazar/llm-testimonial-classifier](https://github.com/manueldazar/llm-testimonial-classifier)

For collaboration, pilots, or implementation support, please contact the author directly.

---

## 👨‍💻 Autor

**Manuel Daza Ramírez**  
AI Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/manueldazaramirez)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/manueldazar)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:manuel.dazaramirez@gmail.com)

---

## ⚠️ Aviso Legal

Este es un **prototipo de demostración**. Los testimonios de ejemplo son **sintéticos** y no representan casos reales. El despliegue en producción requiere:

- Revisión humana de clasificaciones de alta prioridad
- Auditoría y logging para trazabilidad
- Cumplimiento de normativas de protección de datos sensibles
- Validación con expertos del dominio específico
