"""
preprocessing.py
Funciones de limpieza y normalización del texto antes de enviarlo al LLM.
Autor: Manuel Daza Ramirez
"""

import re
import unicodedata


def normalize_unicode(text: str) -> str:
    """Normaliza unicode para evitar inconsistencias en acentos/espacios."""
    return unicodedata.normalize("NFC", text)


def collapse_spaces(text: str) -> str:
    """Reduce espacios múltiples y saltos de línea."""
    return re.sub(r"\s+", " ", text).strip()


def remove_headers_and_footers(text: str) -> str:
    """
    Elimina encabezados/pies de página comunes en documentos UBPD.
    Puedes ajustar expresiones regulares según nuevas fuentes de datos.
    """
    # TODO: añadir patrones UBPD si aparecen en producción.
    return text


def preprocess_text(text: str) -> str:
    """Pipeline completo de preprocesamiento."""
    text = normalize_unicode(text)
    text = remove_headers_and_footers(text)
    text = collapse_spaces(text)
    return text
