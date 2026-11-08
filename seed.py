
import sqlite3
import faker
from random import choice
from pathlib import Path

DB_PATH = Path(__file__).with_name("task_management.db")

NUMBER_USERS = 10
NUMBER_TASKS = 30

fake_data = faker.Faker()


def generate_fake_data(number_users, number_tasks):
    fake_users = []
    fake_tasks = []

    # Generate users
    for _ in range(number_users):
        fake_users.append((
            fake_data.name(),
            fake_data.unique.email()
        ))

    # Generate tasks
    for _ in range(number_tasks):
        fake_tasks.append((
            fake_data.sentence(nb_words=5),
            fake_data.text(),
            choice([1, 2, 3]),
            choice(range(1, number_users + 1))
        ))

    return fake_users, fake_tasks


def prepare_data(users, tasks):
    for_users = []

    for user in users:
        for_users.append(user)

    for_tasks = []

    for task in tasks:
        for_tasks.append(task)

    return for_users, for_tasks


def insert_data_to_db(users, tasks):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        # Enable foreign key constraints
        cur.execute("PRAGMA foreign_keys = ON")

        # Insert users
        sql_to_users = """
            INSERT INTO users (fullname, email)
            VALUES (?, ?)
        """
        cur.executemany(sql_to_users, users)

        # Insert statuses
        statuses = [
            ("new",),
            ("in progress",),
            ("completed",)
        ]

        sql_to_status = """
            INSERT INTO status (name)
            VALUES (?)
        """
        cur.executemany(sql_to_status, statuses)

        # Insert tasks
        sql_to_tasks = """
            INSERT INTO tasks (title, description, status_id, user_id)
            VALUES (?, ?, ?, ?)
        """
        cur.executemany(sql_to_tasks, tasks)

        con.commit()


if __name__ == "__main__":
    users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)

    users, tasks = prepare_data(users, tasks)

    insert_data_to_db(users, tasks)

    print("Database successfully filled!")
