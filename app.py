from flask import Flask, request
from flask_cors import CORS
import db

app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": "http://localhost:5173", "supports_credentials": True}})


@app.route('/')
def Welcome():
    return 'Welcome to the To Do App!'

# index route
@app.route("/todos.json")
def index():
    return db.todos_all()

# create route
@app.route("/todos.json", methods=["POST"])
def create():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    title = data.get("title")
    description = data.get("description")
    completed = data.get("description") or 0
    return db.todo_create(title, description, completed)

# show route
@app.route("/todos/<id>.json")
def show(id):
    return db.todos_find_by_id(id)

# update route
@app.route("/todos/<id>.json", methods=["PATCH"])
def update(id):
    if request.is_json:
        data = request.json
    else:
        data = request.form
    todo = db.todos_find_by_id(id)
    title = data.get("title") or todo["title"]
    description = data.get("description") or todo["description"]
    if "completed" in data:
        completed = data["completed"]
    else:
        completed = todo["completed"]
    # completed = data.get("completed") or todo["completed"]
    return db.todos_update_by_id(id, title, description, completed)

# destroy route
@app.route("/todos/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.todos_destroy_by_id(id)