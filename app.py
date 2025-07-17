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
    completed = 0
    return db.todo_create(title, description, completed)

# show route
@app.route("/todos/<id>.json")
def show(id):
    return db.todos_find_by_id(id)

# # update route
# @app.route("/todos/<int:id>.json", methods=["PUT"])
# def update(id):
#     todo = request.get_json()
#     return db.todos_update(id, todo)

# # destroy route
# @app.route("/todos/<int:id>.json", methods=["DELETE"])
# def destroy(id):
#     return db.todos_destroy(id)