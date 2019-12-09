from flask import Flask, jsonify, abort, request

app = Flask(__name__)

tasks = [
    {
        "id": 122,
        "description": "Webservice entwicklen",
        "priority": "medium",
        "status": "open"
    },
    {
        "id": 123,
        "description": "Test schreiben",
        "priority": "urgent",
        "status": "in progress"
    },
    {
        "id": 124,
        "description": "Sicherheitsanforderung implementieren",
        "priority": "urgent",
        "status": "in progress"
    },
    {
        "id": 125,
        "description": "Anfragen für Webservice entwickeln",
        "priority": "urgent",
        "status": "in progress"
    },
    {
        "id": 126,
        "description": "user management einbinden",
        "priority": "urgent",
        "status": "in progress"
    },
    {
        "id": 127,
        "description": "Flask Framework anschauen",
        "priority": "urgent",
        "status": "in progress"
    },
    {
        "id": 128,
        "description": "docker container bauen",
        "priority": "urgent",
        "status": "in progress"
    },
    {
        "id": 129,
        "description": "deployment",
        "priority": "urgent",
        "status": "in progress"
    }

]


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks to do": tasks})


@app.route('/api/tasks/', methods=["GET"])
def get_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})


@app.route('/api/tasks', methods=['POST'])
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
# def set_status(task_id):
#    pass  # set status for each task

# def set_priority(task_id):
#    pass  # set a priority for each task

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
    task.remove(task[0])
    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(port=1234)
