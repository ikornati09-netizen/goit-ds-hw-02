import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("task_management.db")
SQL_PATH = Path(__file__).with_name("create_db.sql")


def create_db():
    print("SQL file exists:", SQL_PATH.exists())
    print("SQL file path:", SQL_PATH)

    sql = SQL_PATH.read_text()
    print("SQL content:")
    print(sql)

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.executescript(sql)

        tables = cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()

        print("Database:", DB_PATH)
        print("Created tables:", tables)


if __name__ == "__main__":
    create_db()
