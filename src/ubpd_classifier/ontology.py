"""
ontology.py
Carga y manejo de la ontología UBPD (YAML → diccionario → texto para prompt).
Autor: Manuel Daza Ramirez
"""

import yaml
from pathlib import Path


def load_ontology(path: str = None) -> dict:
    """Carga la ontología UBPD desde YAML."""
    if path is None:
        # Resolve path relative to this module's directory
        module_dir = Path(__file__).parent
        path = module_dir / "ontology_ubpd.yaml"
    
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ontology_to_prompt_text(ontology: dict) -> str:
    """
    Compacta la ontología en texto para incrustarla en el prompt.
    Solo imprime códigos válidos, no descripciones largas.
    """
    lines = []

    lines.append("tipo_documento:")
    for code in ontology["tipo_documento"].keys():
        lines.append(f"  - {code}")

    lines.append("tipo_hecho:")
    for code in ontology["tipo_hecho"].keys():
        lines.append(f"  - {code}")

    lines.append("periodo:")
    for code in ontology["periodo"].keys():
        lines.append(f"  - {code}")

    lines.append("actores:")
    for code in ontology["actores"].keys():
        lines.append(f"  - {code}")

    lines.append("ruteo:")
    for code in ontology["ruteo"].keys():
        lines.append(f"  - {code}")

    return "\n".join(lines)
