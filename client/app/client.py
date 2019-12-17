import requests
from app import app
from flask import render_template, request, redirect

rest_ip = "taskmanager"
rest_port = "9033"


@app.route('/index', methods=["GET"])
def index():
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/tasks".format(rest_ip, rest_port)

    r = requests.get(url=url, headers=header)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    tasks = r.json()
    return render_template("index.html", tasks=tasks)


@app.route('/add', methods=["POST"])
def add_task():
    description = request.form["description"]
    priority = request.form["priority"]
    status = request.form["status"]

    payload = {
        "description": description,
        "priority": priority,
        "status": status

    }
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/tasks".format(rest_ip, rest_port)

    r = requests.post(json=payload, headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    return redirect("/index")


@app.route('/delete', methods=["POST"])
def delete_task():
    identifier = request.form["id"]

    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/tasks/{}".format(rest_ip, rest_port, identifier)

    r = requests.delete(headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    return redirect("/index")


@app.route('/update', methods=["POST"])
def update_task():
    identifier = request.form["id"]
    description = request.form["description"]
    priority = request.form["priority"]
    status = request.form["status"]

    payload = {
        "id": identifier
    }
    if description != "":
        payload["description"] = description
    if priority != "":
        payload["priority"] = priority
    if status != "":
        payload["status"] = status

    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/tasks/{}".format(rest_ip, rest_port, identifier)

    r = requests.put(json=payload, headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))
    return redirect("/index")


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route('/loginIn', methods=['GET', 'POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user1 = {
        "username": username,
        "password": password
    }
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/users".format(rest_ip, rest_port)

    r = requests.get(url=url, headers=header)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))
    users = r.json()

    user = next((user for user in users if user["username"] == username), None)

    if len(user) is None:
        return "Please register"
    if user["username"] == user1["username"]:
        if user["password"] == user1["password"]:
            return redirect("/index")
        else:
            return "Wrong Password"
    else:
        return "Please register"


@app.route('/adduser', methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["password"]

    payload = {
        "username": username,
        "password": password

    }
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Web-Client"
    }
    url = "http://{}:{}/api/users".format(rest_ip, rest_port)

    r = requests.post(json=payload, headers=header, url=url)
    if r.status_code != 200:
        print("request failed with status: {}".format(r.status_code))

    return redirect("/index")
