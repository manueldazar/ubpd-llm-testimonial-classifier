"""
runner.py
Ejecución desde línea de comandos del clasificador UBPD.
Autor: Manuel Daza Ramirez
"""

import argparse
import json
import os
from typing import Optional

from classifier import classify_document


def read_text_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # Import db only when needed (lazy import for optional database functionality)
    try:
        from db import save_document_and_classification
    except ImportError:
        save_document_and_classification = None
    
    parser = argparse.ArgumentParser(
        description="Demo 2 – UBPD: Clasificador de documentos testimoniales"
    )
    parser.add_argument(
        "--text",
        type=str,
        help="Texto a clasificar (si se usa, tiene prioridad sobre --file).",
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Ruta a archivo de texto con el documento a clasificar.",
    )
    parser.add_argument(
        "--no-db",
        action="store_true",
        help="No guardar resultado en la base de datos, solo mostrar por pantalla.",
    )
    parser.add_argument(
        "--external-id",
        type=str,
        help="Identificador externo opcional para el documento.",
    )
    parser.add_argument(
        "--source-system",
        type=str,
        default="LOCAL_DEMO",
        help="Nombre del sistema de origen (default: LOCAL_DEMO).",
    )

    args = parser.parse_args()

    # Obtener texto
    if args.text:
        text = args.text
    elif args.file:
        text = read_text_from_file(args.file)
    else:
        print("Debe proporcionar --text o --file.")
        return

    # Verificar API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY no está definida en las variables de entorno.")
        return

    # Clasificar
    print("Clasificando documento...")
    classification = classify_document(text)

    # Añadir metadatos de modelo si quieres guardarlos en BD
    classification.setdefault("model_name", "gpt-5.1")
    classification.setdefault("model_version", "")

    # Mostrar resultado en pantalla
    print("\nResultado de clasificación:")
    print(json.dumps(classification, indent=2, ensure_ascii=False))

    # Guardar en BD si no se desactiva
    if not args.no_db:
        try:
            doc_id, run_id = save_document_and_classification(
                text=text,
                classification=classification,
                external_id=args.external_id,
                source_system=args.source_system,
                filename=args.file,
            )
            print(f"\nGuardado en BD.")
            print(f"  doc_id = {doc_id}")
            print(f"  run_id = {run_id}")
        except Exception as e:
            print(f"\nADVERTENCIA: No se pudo guardar en la base de datos: {e}")


if __name__ == "__main__":
    main()
