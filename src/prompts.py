"""
prompts.py
Prompts estructurados y auto-verificables para el clasificador UBPD.
Autor: Manuel Daza Ramirez
"""

from ontology import ontology_to_prompt_text, load_ontology


# Cargar ontología al inicio
ONTOLOGY = load_ontology()
ONTOLOGY_PROMPT = ontology_to_prompt_text(ONTOLOGY)


# ---------------------------------------------------------------------
# SYSTEM PROMPT (auto-verificable + comprimido)
# ---------------------------------------------------------------------
SYSTEM_PROMPT = f"""
Eres un clasificador para la UBPD. Devuelves SOLO un JSON válido usando únicamente los códigos permitidos.

CÓDIGOS VÁLIDOS:
{ONTOLOGY_PROMPT}

REGLAS:
- No inventes códigos.
- tipo_documento: un solo código.
- tipo_hecho: lista (puede ser vacía).
- periodo: un código.
- actores: lista (si vacía, usar ["ACT0"]).
- territorio: lista de departamentos o ["No identificado"].
- highlights: lista de frases textuales (o vacía).
- Si tipo_documento = "TD0" → ruteo = "RU0".

FORMATO OBLIGATORIO:
{{
  "tipo_documento": "...",
  "tipo_hecho": [...],
  "territorio": [...],
  "periodo": "...",
  "actores": [...],
  "ruteo": "...",
  "highlights": [...]
}}

VALIDACIÓN INTERNA (antes de responder):
1) ¿Los códigos pertenecen a las listas válidas?
2) ¿Están todos los campos requeridos?
3) ¿No hay campos adicionales?
4) ¿Se cumple la regla TD0 → RU0?
5) ¿territorio y highlights son listas?
6) Respóndeme SOLO el JSON final.
""".strip()


# ---------------------------------------------------------------------
# USER TEMPLATE (few-shot comprimido)
# ---------------------------------------------------------------------
USER_TEMPLATE = """
Ejemplo 1 (entrada):
"Yo, María, cuento que en 1997, en San Carlos, Antioquia, hombres armados de la guerrilla se llevaron a mi esposo. Debimos salir hacia Medellín."

Ejemplo 1 (salida):
{
  "tipo_documento": "TD1",
  "tipo_hecho": ["TH1","TH3"],
  "territorio": ["Antioquia"],
  "periodo": "PER2",
  "actores": ["ACT2"],
  "ruteo": "RU1",
  "highlights": [
    "1997, en San Carlos, Antioquia",
    "se llevaron a mi esposo"
  ]
}

Ejemplo 2 (entrada):
"Oficio 123 de 2020. Remito informe técnico."

Ejemplo 2 (salida):
{
  "tipo_documento": "TD0",
  "tipo_hecho": [],
  "territorio": ["No identificado"],
  "periodo": "PER5",
  "actores": ["ACT0"],
  "ruteo": "RU0",
  "highlights": []
}

Ahora clasifica este documento siguiendo exactamente el formato:

DOCUMENTO:
{{DOCUMENTO}}

Devuelve SOLO el JSON.
""".strip()


def build_user_prompt(text: str) -> str:
    """Inserta documento en la plantilla few-shot."""
    return USER_TEMPLATE.replace("{{DOCUMENTO}}", text.strip())
