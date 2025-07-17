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


# WEB LAYER

# index action - to get all todos
def todos_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM todos
        """
    ).fetchall()
    return [dict(row) for row in rows]

# create action - to create a new todo
def todo_create(title, description, completed):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO todos (title, description, completed)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (title, description, completed),
    ).fetchone()
    conn.commit()
    return dict(row)

# show action - find a todo by id
def todos_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM todos
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

# update action - update a todo
def todos_update_by_id(id, title, description, completed):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE todos SET title = ?, description = ?, completed = ?
        WHERE id = ?
        RETURNING *
        """,
        (title, description, completed, id),
    ).fetchone()
    conn.commit()
    return dict(row)

# # destroy action - delete a todo
# def todos_destroy(id):
#     conn = connect_to_db()
#     conn.execute(
#         """
#         DELETE FROM todos
#         WHERE id = ?
#         """,
#         (id,),
#     )
#     conn.commit()
#     return {"message": "Todo deleted successfully"}