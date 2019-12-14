from flask import jsonify, abort, request
import mysql.connector
from app import app

tasks = [
    {
        'id': 1,
        'description': 'moon landing',
        'priority': 'low',
        'status': 'open'
    },
{
        'id': 2,
        'description': 'train for the marathon',
        'priority': 'high',
        'status': 'in progress'
    }

]


@app.route('/api/tasks/', methods=['GET'])
def get_tasks():
    return jsonify({"tasks to do": tasks})


@app.route('/api/tasks/', methods=["GET"])
def get_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})


@app.route('/api/tasks/', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    if len(tasks) != 0:
        id = tasks[-1]["id"] + 1
    else:
        id = 1

    task = {
        "id": id,
        "description": request.json["description"],
        "priority": request.json["priority"],
        "status": request.json["status"]
    }
    tasks.append(task)
    return jsonify({"task": task})


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)

    task[0]["description"] = request.json.get("description", task[0]["description"])
    task[0]["priority"] = request.json.get("priority", task[0]["priority"])
    task[0]["status"] = request.json.get("status", task[0]["status"])
    return jsonify({"task": task[0]})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    else:
        print(task_id)
        print(task)
        tasks.remove(task[0])
    return jsonify({"result": True})


@app.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    if len(users) != 0:
        id = users[-1]["id"] + 1
    else:
        id = 1

    user = {
        "id": id,
        "username": request.json["username"],
        "password": request.json["password"]
    }
    users.append(user)
    return jsonify({"User": user})



@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)



def getMysqlConnection():
    return mysql.connector.connect(user='user', host='mysql', port='3306', password='admin', database='tasks')


