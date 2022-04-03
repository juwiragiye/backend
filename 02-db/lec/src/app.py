import json
from turtle import done
import db
from flask import Flask, request


app = Flask(__name__)

DB = db.DatabaseDriver()


@app.route("/")
@app.route("/tasks/")
def get_tasks():
    return json.dumps({"tasks": DB.get_all_tasks()}), 200


@app.route("/tasks/", methods=["POST"])
def create_task():
    """
    Endpoint for creating a task.
    """
    body = json.loads(request.data)
    desc = body["description"]
    task_id = DB.insert_task(desc, False)
    task = DB.get_task(task_id)
    return json.dumps({"task": task}), 201
    



@app.route("/tasks/<int:task_id>/")
def get_task(task_id):
    pass


@app.route("/tasks/<int:task_id>/", methods=["POST"])
def update_task(task_id):
    pass


@app.route("/tasks/<int:task_id>/", methods=["DELETE"])
def delete_task(task_id):
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
