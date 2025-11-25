"""
classifier.py
Pipeline completo del clasificador UBPD.
Autor: Manuel Daza Ramirez
"""

import json
import os
from typing import Dict, Any, List
from openai import OpenAI

from preprocessing import preprocess_text
from prompts import SYSTEM_PROMPT, build_user_prompt, ONTOLOGY
from ontology import load_ontology


# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = "gpt-5.1"


# ---------------------------------------------------------------------
# Llamada al modelo
# ---------------------------------------------------------------------
def call_llm(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.0,
    )

    # SDK nuevo: message es un objeto, no un dict
    return response.choices[0].message.content



# ---------------------------------------------------------------------
# Extracción segura de JSON
# ---------------------------------------------------------------------
def extract_json_block(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No se encontró JSON válido en la salida del modelo.")
    return text[start:end + 1]


def parse_model_response(raw: str) -> Dict[str, Any]:
    return json.loads(extract_json_block(raw))


# ---------------------------------------------------------------------
# Validación y arreglos post-modelo
# ---------------------------------------------------------------------
def fix_single_label(value: str, allowed: dict, default: str):
    return value if value in allowed else default


def fix_multi_labels(values, allowed: dict):
    if not isinstance(values, list):
        return []
    return [v for v in values if v in allowed]


def fix_territorio(values):
    if not isinstance(values, list) or len(values) == 0:
        return ["No identificado"]
    return list({v.strip() for v in values})


def compute_priority(pred: dict) -> float:
    score = 0.0
    hechos = set(pred.get("tipo_hecho", []))
    ruteo = pred.get("ruteo")

    if "TH1" in hechos:
        score += 0.4
    if "TH4" in hechos:
        score += 0.2
    if ruteo == "RU1":
        score += 0.3
    if ruteo == "RU3":
        score += 0.1

    return min(score, 1.0)


def validate_and_fix(pred: dict) -> dict:
    ont = ONTOLOGY

    pred["tipo_documento"] = fix_single_label(
        pred.get("tipo_documento"),
        ont["tipo_documento"],
        "TD0"
    )

    pred["tipo_hecho"] = fix_multi_labels(
        pred.get("tipo_hecho", []),
        ont["tipo_hecho"]
    )

    pred["periodo"] = fix_single_label(
        pred.get("periodo"),
        ont["periodo"],
        "PER0"
    )

    pred["actores"] = fix_multi_labels(
        pred.get("actores", []),
        ont["actores"]
    )

    pred["ruteo"] = fix_single_label(
        pred.get("ruteo"),
        ont["ruteo"],
        "RU0"
    )

    # Regla automática
    if pred["tipo_documento"] == "TD0":
        pred["ruteo"] = "RU0"

    pred["territorio"] = fix_territorio(pred.get("territorio", []))

    if not isinstance(pred.get("highlights"), list):
        pred["highlights"] = []

    pred["priority_score"] = compute_priority(pred)
    return pred


# ---------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------
def classify_document(text: str) -> dict:
    clean = preprocess_text(text)
    user_prompt = build_user_prompt(clean)
    raw = call_llm(SYSTEM_PROMPT, user_prompt)
    pred = parse_model_response(raw)
    fixed = validate_and_fix(pred)
    return fixed
