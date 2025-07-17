import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS photos;
        """
    )
    conn.execute(
        """
        CREATE TABLE todos (
          id INTEGER PRIMARY KEY NOT NULL,
          title TEXT,
          description INTEGER,
          completed BOOLEAN DEFAULT 0
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    todos_seed_data = [
        ("Homework", "Write an Essay for Englidh class.", 0),
        ("Shopping", "Buy groceries for the week.", 0),
        ("Laundry", "Wash and fold clothes.", 0),
    ]
    conn.executemany(
        """
        INSERT INTO todos (title, description, completed)
        VALUES (?,?,?)
        """,
        todos_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()


# web layer
def todos_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM todos
        """
    ).fetchall()
    return [dict(row) for row in rows]