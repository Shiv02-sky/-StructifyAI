import sqlite3
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "database"
DB_DIR.mkdir(exist_ok=True)

DATABASE_NAME = DB_DIR / "structify.db"


def initialize_database():
    conn = sqlite3.connect(str(DATABASE_NAME))

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        filetype TEXT,

        extracted_text TEXT,

        structured_json TEXT,

        summary TEXT,

        created_at TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_document(filename, filetype, text, json_data, summary):
    conn = sqlite3.connect(str(DATABASE_NAME))

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO documents(
        filename,
        filetype,
        extracted_text,
        structured_json,
        summary,
        created_at
    )
    VALUES(?,?,?,?,?,?)
    """,
    (
        filename,
        filetype,
        text,
        json_data,
        summary,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    )
    )

    conn.commit()
    conn.close()


def get_documents():
    conn = sqlite3.connect(str(DATABASE_NAME))

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, filename, created_at
    FROM documents
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_document(doc_id):
    conn = sqlite3.connect(str(DATABASE_NAME))

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM documents
    WHERE id=?
    """, (doc_id,))

    row = cursor.fetchone()
    conn.close()
    return row