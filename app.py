from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# index route
@app.route("/todos.json")
def index():
    return db.todos_all()

# create route
@app.route("/todos.json", methods=["POST"])
def create():
    title = request.args.get("title")
    description = request.args.get("description")
    completed = request.args.get("description") or 0
    return db.todo_create(title, description, completed)

# show route
@app.route("/todos/<id>.json")
def show(id):
    return db.todos_find_by_id(id)

# update route
@app.route("/todos/<id>.json", methods=["PATCH"])
def update(id):
    todo = db.todos_find_by_id(id)
    title = request.args.get("title") or todo["title"]
    description = request.args.get("description") or todo["description"]
    completed = request.args.get("completed") or todo["completed"]
    return db.todos_update_by_id(id, title, description, completed)

# destroy route
@app.route("/todos/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.todos_destroy_by_id(id)