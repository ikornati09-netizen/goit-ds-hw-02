import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("task_management.db")

with sqlite3.connect(DB_PATH) as con:
    cur = con.cursor()

    for table in ["users", "status", "tasks"]:
        count = cur.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]

        print(f"{table}: {count} rows")
