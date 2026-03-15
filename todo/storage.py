import sqlite3

DB = "todo.db"

def get_connection():
    return sqlite3.connect(DB)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        """)

def save(tasks, next_id=None):
    pass

def load():
    return [], 1

