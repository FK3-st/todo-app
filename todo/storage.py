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
    with get_connection() as conn:
        cursor = conn.execute("SELECT id, task, done FROM tasks")
        rows = cursor.fetchall()
        for row in rows:
            tasks = {"id": rows[0], 
                     "task":rows[1], 
                     "done":bool(rows[2])
                }

        next_id = max(row[0] for in rows) + 1 if rows else 1

    return tasks, next_id


