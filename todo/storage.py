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
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks")
        for task in tasks:
            conn.execute(
                "INSERT INTO tasks (id, task, done) VALUES (?, ?, ?)",
                (task["id"], task["task"], task["done"])

            )

def load():
    def load():
    with get_connection() as conn:
        cursor = conn.execute("SELECT id, task, done FROM tasks")
        rows = cursor.fetchall()
    return [{"id": rows[0], "task":rows[1], "done":bool(rows[2])}], max(id) + 1


