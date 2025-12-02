# 📄 Clasificador de Documentos Testimoniales - UBPD

**Autor:** Manuel Daza Ramírez  
**Versión:** 2025-02  
**Demo para:** Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)

---

## 📋 Descripción

Este proyecto implementa un **clasificador automático de documentos testimoniales** utilizando Modelos de Lenguaje (LLM) con ontología controlada. Está diseñado para apoyar el trabajo de la UBPD en la clasificación y priorización de testimonios relacionados con el conflicto armado colombiano.

### Contexto Institucional

La **UBPD (Unidad de Búsqueda de Personas dadas por Desaparecidas)** es una entidad del Estado colombiano creada en el marco del Acuerdo de Paz de 2016. Su misión es dirigir, coordinar y contribuir a la implementación de acciones humanitarias de búsqueda de personas dadas por desaparecidas en el contexto y en razón del conflicto armado.

La UBPD recibe miles de documentos testimoniales que contienen información crítica sobre:
- **Hechos victimizantes** (desaparición forzada, homicidio, desplazamiento, violencia sexual)
- **Actores armados** involucrados (guerrillas, paramilitares, fuerza pública)
- **Territorios** donde ocurrieron los hechos (33 departamentos de Colombia)
- **Períodos temporales** del conflicto (1985-2025)

---

## 🎯 Problema que Resuelve

La clasificación manual de testimonios presenta varios desafíos:

| Desafío | Descripción |
|---------|-------------|
| **Volumen** | Miles de documentos requieren clasificación |
| **Inconsistencia** | Diferentes analistas pueden clasificar el mismo documento de formas distintas |
| **Tiempo** | La clasificación manual consume recursos humanos escasos |
| **Priorización** | Es difícil identificar rápidamente casos urgentes que requieren atención inmediata |

### Solución

Este sistema utiliza un **LLM (Large Language Model)** con una **ontología controlada** para:

- ✅ Clasificar automáticamente documentos según categorías predefinidas
- ✅ Garantizar consistencia mediante vocabularios controlados
- ✅ Calcular scores de prioridad para enrutamiento
- ✅ Extraer fragmentos relevantes (highlights) para análisis posterior
- ✅ Persistir resultados en PostgreSQL para análisis y auditoría

---

## 🏗️ Arquitectura del Sistema

```
Texto crudo del documento
         │
         ▼
┌─────────────────────────────┐
│   preprocessing.py          │  Normalización Unicode, limpieza
│   preprocess_text()         │
└─────────────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   prompts.py                │  Template few-shot + ontología
│   build_user_prompt()       │
└─────────────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   classifier.py             │  Llamada a OpenAI API (GPT-4o)
│   call_llm()                │
└─────────────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   classifier.py             │  Extracción y parsing JSON
│   parse_model_response()    │
└─────────────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   classifier.py             │  Validación contra ontología
│   validate_and_fix()        │  + reglas de negocio + priority_score
└─────────────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   db.py                     │  Persistencia en PostgreSQL
│   save_document_and_        │  (opcional)
│   classification()          │
└─────────────────────────────┘
         │
         ▼
Clasificación final validada + almacenada
```

---

## 📁 Estructura del Proyecto

```
ubpd-llm-testimonial-classifier/
├── src/
│   ├── classifier.py         # Pipeline principal de clasificación
│   ├── db.py                  # Conexión PostgreSQL y persistencia
│   ├── ontology.py            # Carga y serialización de ontología
│   ├── preprocessing.py       # Limpieza y normalización de texto
│   ├── prompts.py             # System prompt y templates few-shot
│   └── runner.py              # CLI para ejecución desde terminal
│
├── ontology_ubpd.yaml         # Ontología de clasificación UBPD
├── requirements.txt           # Dependencias pip
├── environment.yml            # Entorno Conda (Windows)
├── .env                       # Variables de entorno (API keys, DB)
│
├── run-classifier-conda.ps1   # Script PowerShell (Conda)
├── run-classifier-gui.ps1     # Script PowerShell (GUI)
│
├── notebooks/
│   └── UBPD_Demo_Clasificador_Testimonios_Commented.ipynb
│
├── docs/                      # Documentación Jekyll
│   ├── architecture.html
│   ├── ontology.html
│   ├── api.html
│   └── demo.html
│
├── _config.yml                # Configuración Jekyll para GitHub Pages
└── README.md
```

---

## 🔧 Instalación

### Prerrequisitos

- Python 3.9+ (recomendado 3.13)
- PostgreSQL 14+ (opcional, para persistencia)
- Cuenta de OpenAI con acceso a la API

### Opción A: Instalación con pip

```bash
# 1. Clonar repositorio
git clone https://github.com/manueldazar/ubpd-llm-testimonial-classifier.git
cd ubpd-llm-testimonial-classifier

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Opción B: Instalación con Conda (Windows)

```bash
# 1. Clonar repositorio
git clone https://github.com/manueldazar/ubpd-llm-testimonial-classifier.git
cd ubpd-llm-testimonial-classifier

# 2. Crear entorno desde environment.yml
conda env create -f environment.yml

# 3. Activar entorno
conda activate ubpd_env
```

### Configuración de Variables de Entorno

Crear archivo `.env` en el directorio raíz:

```env
# OpenAI API
OPENAI_API_KEY=sk-tu-api-key-aqui

# PostgreSQL (opcional)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ubpd
DB_USER=ubpd
DB_PASSWORD=ubpd
```

> ⚠️ **IMPORTANTE:** Nunca commitear el archivo `.env` a control de versiones.

### Configuración de Base de Datos (Opcional)

Si deseas persistir las clasificaciones:

```bash
# Crear tablas en PostgreSQL
python src/db.py create-tables
```

---

## 📖 Uso

### Opción 1: Línea de Comandos (CLI)

```bash
# Clasificar texto directo
python src/runner.py --text "Mi hermano desapareció en 1998 en Urabá..."

# Clasificar desde archivo
python src/runner.py --file documento.txt

# Sin guardar en base de datos
python src/runner.py --text "..." --no-db

# Con identificador externo
python src/runner.py --file doc.txt --external-id "CASO-2024-001" --source-system "SIIJEP"
```

### Opción 2: Como Módulo Python

```python
from classifier import classify_document

testimonio = """
Yo, María, cuento que en 1997, en el municipio de San Carlos, Antioquia, 
hombres armados que se identificaron como de la guerrilla se llevaron a mi esposo. 
Desde ese día no volvimos a saber de él. Después de eso comenzaron las amenazas 
y nos tocó salir de la vereda e irnos para Medellín, dejando todo atrás.
"""

resultado = classify_document(testimonio)
print(resultado)
```

### Opción 3: Notebook Jupyter

```bash
jupyter lab notebooks/UBPD_Demo_Clasificador_Testimonios_Commented.ipynb
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
    "1997, en el municipio de San Carlos, Antioquia",
    "se llevaron a mi esposo"
  ],
  "priority_score": 0.7
}
```

---

## 📚 Ontología UBPD

La ontología define el vocabulario controlado para la clasificación. Se carga desde `ontology_ubpd.yaml`.

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

### Territorio

Lista completa de los 33 departamentos de Colombia + "No identificado".

---

## 📊 Sistema de Prioridad

El `priority_score` es un valor entre 0.0 y 1.0 calculado según:

| Condición | Puntos | Justificación |
|-----------|--------|---------------|
| TH1 (Desaparición forzada) | +0.4 | Mandato principal de la UBPD |
| TH4 (Violencia sexual) | +0.2 | Alto impacto, requiere atención especializada |
| RU1 (Búsqueda e identificación) | +0.3 | Caso activo de búsqueda |
| RU3 (Atención psicosocial) | +0.1 | Requiere acompañamiento |

### Interpretación

```
0.0 - 0.3: Prioridad baja (documentos administrativos, no testimoniales)
0.4 - 0.6: Prioridad media (testimonios con información parcial)
0.7 - 1.0: Prioridad alta (desapariciones activas, casos urgentes)
```

---

## 🗄️ Modelo de Base de Datos

El sistema persiste documentos y clasificaciones en PostgreSQL con el siguiente esquema:

```
┌─────────────────────┐
│   doc_document      │──────┐
│   (documento base)  │      │
└─────────────────────┘      │
                             │ 1:N
┌─────────────────────┐      │
│ doc_classification_ │◄─────┘
│ run (ejecución)     │──────┬──────┬──────┬──────┐
└─────────────────────┘      │      │      │      │
                             │      │      │      │
    ┌────────────────────────┼──────┼──────┼──────┼────────────────────┐
    │                        │      │      │      │                    │
    ▼                        ▼      ▼      ▼      ▼                    ▼
┌─────────┐  ┌─────────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────────────────┐
│ _labels │  │ _hecho  │  │_terr│  │_actor│ │_high│  │   raw_json      │
│(1:1)    │  │ (1:N)   │  │(1:N)│  │(1:N) │ │(1:N)│  │   (JSONB)       │
└─────────┘  └─────────┘  └─────┘  └─────┘  └─────┘  └─────────────────┘
```

### Tablas Principales

- `doc_document`: Documento original con texto y metadatos
- `doc_classification_run`: Ejecución de clasificación (modelo, timestamp)
- `doc_classification_labels`: Etiquetas simples + priority_score + raw_json
- `doc_classification_hecho`: Hechos victimizantes (multi-etiqueta)
- `doc_classification_territorio`: Territorios (multi-etiqueta)
- `doc_classification_actor`: Actores (multi-etiqueta)
- `doc_classification_highlight`: Fragmentos destacados

---

## 🔍 Módulos del Sistema

### `preprocessing.py`
Funciones de limpieza y normalización de texto:
- `normalize_unicode()`: Normaliza caracteres a forma NFC
- `collapse_spaces()`: Reduce espacios múltiples
- `remove_headers_and_footers()`: Elimina encabezados institucionales
- `preprocess_text()`: Pipeline completo

### `ontology.py`
Manejo de la ontología UBPD:
- `load_ontology()`: Carga YAML a diccionario Python
- `ontology_to_prompt_text()`: Serializa para incluir en prompts

### `prompts.py`
Prompts estructurados para el LLM:
- `SYSTEM_PROMPT`: Rol, ontología, reglas, formato JSON
- `USER_TEMPLATE`: Ejemplos few-shot
- `build_user_prompt()`: Inserta documento en template

### `classifier.py`
Pipeline principal:
- `call_llm()`: Llamada a OpenAI API
- `parse_model_response()`: Extracción segura de JSON
- `validate_and_fix()`: Validación contra ontología
- `compute_priority()`: Cálculo de priority_score
- `classify_document()`: Función principal

### `db.py`
Persistencia en PostgreSQL:
- `get_connection()`: Conexión a BD
- `create_tables()`: Inicialización de esquema
- `save_document_and_classification()`: Guardar documento + clasificación

### `runner.py`
Interfaz de línea de comandos:
- Argumentos: `--text`, `--file`, `--no-db`, `--external-id`, `--source-system`

---

## ⚙️ Configuración Avanzada

### Cambiar el Modelo

En `classifier.py`:

```python
MODEL_NAME = "gpt-4o"        # Por defecto
# MODEL_NAME = "gpt-4-turbo"  # Mayor capacidad
# MODEL_NAME = "gpt-3.5-turbo"  # Más económico
```

### Parámetros del Modelo

```python
temperature=0.0  # Determinismo máximo para clasificación consistente
```

### Extender la Ontología

Editar `ontology_ubpd.yaml` para agregar nuevos códigos:

```yaml
tipo_hecho:
  TH1: "Desaparición forzada"
  TH8: "Nuevo tipo de hecho"  # Agregar aquí
```

---

## 🧪 Reglas de Negocio

El sistema implementa las siguientes reglas automáticas:

1. **TD0 → RU0**: Documentos no testimoniales no se enrutan
2. **Actor por defecto**: Si no hay actor identificado, usar `["ACT0"]`
3. **Territorio por defecto**: Si no hay ubicación, usar `["No identificado"]`
4. **Validación de códigos**: Solo se aceptan códigos de la ontología

---

## 📈 Próximos Pasos

### Corto plazo
- [ ] Agregar retry logic y manejo de rate limits
- [ ] Implementar logging estructurado (JSON)
- [ ] Validar ontología con expertos UBPD
- [ ] Agregar más ejemplos few-shot

### Mediano plazo
- [ ] Batch processing para múltiples documentos
- [ ] API REST con FastAPI
- [ ] Dashboard de monitoreo
- [ ] Métricas de calidad (accuracy, F1)

### Largo plazo
- [ ] Fine-tuning con datos etiquetados UBPD
- [ ] Explicabilidad de clasificaciones
- [ ] Búsqueda semántica con embeddings
- [ ] Clasificación multi-documento

---

## 🌐 Documentación en Línea

El proyecto incluye documentación Jekyll para GitHub Pages:

- **Home**: Introducción y overview
- **Architecture**: Diagrama de arquitectura
- **Ontology**: Detalle de códigos
- **API**: Referencia de funciones
- **Demo**: Ejemplos interactivos

Acceder en: `https://manueldazar.github.io/ubpd-llm-testimonial-classifier`

---

## ⚠️ Notas Importantes

- Este es un **prototipo de demostración**
- Los testimonios de ejemplo son **sintéticos** (no casos reales)
- En producción se requiere:
  - Auditoría de clasificaciones
  - Revisión humana de casos prioritarios
  - Monitoreo de calidad del modelo
  - Cumplimiento de normativas de datos sensibles

---

## 📞 Contacto

**Manuel Daza Ramírez**  
AI Engineer - Prototipo de clasificación de documentos testimoniales

- 🔗 LinkedIn: [linkedin.com/in/manueldazaramirez](https://linkedin.com/in/manueldazaramirez)
- 📧 Email: manuel.dazaramirez@gmail.com
- 🐙 GitHub: [github.com/manueldazar](https://github.com/manueldazar)

---

## 📄 Licencia

Este proyecto es un prototipo de demostración desarrollado para mostrar capacidades de clasificación automática de documentos testimoniales usando LLMs.
