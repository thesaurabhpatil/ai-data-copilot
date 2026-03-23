import sqlite3
import json
from datetime import datetime

DB_NAME = "chats.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        messages TEXT,
        created_at TEXT,
        updated_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_chat(title, messages):
    now = datetime.utcnow().isoformat()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats (title, messages, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (title, json.dumps(messages), now, now)
    )

    chat_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return chat_id


def update_chat(chat_id, messages):
    now = datetime.utcnow().isoformat()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE chats SET messages=?, updated_at=? WHERE id=?",
        (json.dumps(messages), now, chat_id)
    )

    conn.commit()
    conn.close()


def rename_chat(chat_id, new_title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE chats SET title=? WHERE id=?",
        (new_title, chat_id)
    )

    conn.commit()
    conn.close()


def load_chats(search_query=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if search_query:
        cursor.execute(
            "SELECT id, title, messages FROM chats WHERE title LIKE ? ORDER BY updated_at DESC",
            (f"%{search_query}%",)
        )
    else:
        cursor.execute(
            "SELECT id, title, messages FROM chats ORDER BY updated_at DESC"
        )

    rows = cursor.fetchall()
    conn.close()

    return [(r[0], r[1], json.loads(r[2])) for r in rows]


def delete_chat(chat_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM chats WHERE id=?", (chat_id,))
    conn.commit()
    conn.close()