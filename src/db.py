"""
db.py
Conexión a PostgreSQL y persistencia de documentos + clasificaciones UBPD.
Autor: Manuel Daza Ramirez
"""

import os
import json
from typing import Tuple, Dict, Any

import psycopg2
from psycopg2.extras import Json


# ---------------------------------------------------------------------
# Conexión
# ---------------------------------------------------------------------


def get_connection():
    """
    Crea una conexión a PostgreSQL usando variables de entorno:

    - DB_HOST (default: localhost)
    - DB_PORT (default: 5432)
    - DB_NAME (default: ubpd)
    - DB_USER (default: ubpd)
    - DB_PASSWORD (default: ubpd)
    """
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "ubpd"),
        user=os.getenv("DB_USER", "ubpd"),
        password=os.getenv("DB_PASSWORD", "ubpd"),
    )


# ---------------------------------------------------------------------
# Creación de tablas mínimas
# ---------------------------------------------------------------------


SCHEMA_SQL = """
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS doc_document (
    doc_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id     TEXT,
    source_system   TEXT,
    filename        TEXT,
    mime_type       TEXT,
    ingestion_ts    TIMESTAMPTZ NOT NULL DEFAULT now(),
    language        TEXT DEFAULT 'es',
    text_content    TEXT NOT NULL,
    created_by      TEXT,
    updated_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS doc_classification_run (
    run_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    doc_id          UUID NOT NULL REFERENCES doc_document(doc_id),
    model_name      TEXT NOT NULL,
    model_version   TEXT,
    run_ts          TIMESTAMPTZ NOT NULL DEFAULT now(),
    runtime_ms      INTEGER,
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    created_by      TEXT,
    notes           TEXT
);

CREATE TABLE IF NOT EXISTS doc_classification_labels (
    run_id          UUID PRIMARY KEY REFERENCES doc_classification_run(run_id),
    tipo_documento  VARCHAR(4) NOT NULL,
    periodo         VARCHAR(4) NOT NULL,
    ruteo           VARCHAR(4) NOT NULL,
    priority_score  NUMERIC(5,4),
    raw_json        JSONB
);

CREATE TABLE IF NOT EXISTS doc_classification_hecho (
    run_id          UUID NOT NULL REFERENCES doc_classification_run(run_id),
    hecho_code      VARCHAR(4) NOT NULL,
    PRIMARY KEY (run_id, hecho_code)
);

CREATE TABLE IF NOT EXISTS doc_classification_territorio (
    run_id          UUID NOT NULL REFERENCES doc_classification_run(run_id),
    territorio_name TEXT NOT NULL,
    PRIMARY KEY (run_id, territorio_name)
);

CREATE TABLE IF NOT EXISTS doc_classification_actor (
    run_id          UUID NOT NULL REFERENCES doc_classification_run(run_id),
    actor_code      VARCHAR(4) NOT NULL,
    PRIMARY KEY (run_id, actor_code)
);

CREATE TABLE IF NOT EXISTS doc_classification_highlight (
    highlight_id    BIGSERIAL PRIMARY KEY,
    run_id          UUID NOT NULL REFERENCES doc_classification_run(run_id),
    field_name      TEXT,
    snippet         TEXT NOT NULL,
    char_start      INTEGER,
    char_end        INTEGER
);
"""


def create_tables():
    """Crea las tablas mínimas si no existen."""
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(SCHEMA_SQL)
        print("Tablas creadas o ya existentes.")
    finally:
        conn.close()


# ---------------------------------------------------------------------
# Inserción de documento + clasificación
# ---------------------------------------------------------------------


def save_document_and_classification(
    text: str,
    classification: Dict[str, Any],
    external_id: str | None = None,
    source_system: str = "LOCAL_DEMO",
    filename: str | None = None,
    mime_type: str = "text/plain",
    language: str = "es",
    created_by: str = "UBPD_Demo2",
) -> Tuple[str, str]:
    """
    Guarda documento y clasificación en la base de datos.
    Devuelve (doc_id, run_id).

    classification debe contener al menos:
      - tipo_documento (str)
      - periodo (str)
      - ruteo (str)
      - priority_score (float)
      - tipo_hecho (list[str])
      - territorio (list[str])
      - actores (list[str])
      - highlights (list[str])
    """

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                # 1) Insertar documento
                cur.execute(
                    """
                    INSERT INTO doc_document (
                        external_id, source_system, filename, mime_type,
                        language, text_content, created_by
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING doc_id;
                    """,
                    (
                        external_id,
                        source_system,
                        filename,
                        mime_type,
                        language,
                        text,
                        created_by,
                    ),
                )
                (doc_id,) = cur.fetchone()

                # 2) Insertar run de clasificación
                cur.execute(
                    """
                    INSERT INTO doc_classification_run (
                        doc_id, model_name, model_version, is_active, created_by
                    )
                    VALUES (%s, %s, %s, TRUE, %s)
                    RETURNING run_id;
                    """,
                    (
                        doc_id,
                        classification.get("model_name", "gpt-5.1"),
                        classification.get("model_version", ""),
                        created_by,
                    ),
                )
                (run_id,) = cur.fetchone()

                # 3) Etiquetas "simples"
                cur.execute(
                    """
                    INSERT INTO doc_classification_labels (
                        run_id, tipo_documento, periodo, ruteo, priority_score, raw_json
                    )
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """,
                    (
                        run_id,
                        classification.get("tipo_documento"),
                        classification.get("periodo"),
                        classification.get("ruteo"),
                        classification.get("priority_score", 0.0),
                        Json(classification),
                    ),
                )

                # 4) Multi-etiquetas: tipo_hecho
                for hecho in classification.get("tipo_hecho", []):
                    cur.execute(
                        """
                        INSERT INTO doc_classification_hecho (run_id, hecho_code)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING;
                        """,
                        (run_id, hecho),
                    )

                # 5) Multi-etiquetas: territorio
                for terr in classification.get("territorio", []):
                    cur.execute(
                        """
                        INSERT INTO doc_classification_territorio (run_id, territorio_name)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING;
                        """,
                        (run_id, terr),
                    )

                # 6) Multi-etiquetas: actores
                for actor in classification.get("actores", []):
                    cur.execute(
                        """
                        INSERT INTO doc_classification_actor (run_id, actor_code)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING;
                        """,
                        (run_id, actor),
                    )

                # 7) Highlights (sin posiciones por ahora)
                for snippet in classification.get("highlights", []):
                    cur.execute(
                        """
                        INSERT INTO doc_classification_highlight (
                            run_id, field_name, snippet, char_start, char_end
                        )
                        VALUES (%s, %s, %s, NULL, NULL);
                        """,
                        (run_id, None, snippet),
                    )

        return str(doc_id), str(run_id)
    finally:
        conn.close()


# ---------------------------------------------------------------------
# CLI simple para crear tablas
# ---------------------------------------------------------------------


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "create-tables":
        create_tables()
    else:
        print("Uso:")
        print("  python db.py create-tables")
