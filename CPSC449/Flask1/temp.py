from flask import Flask, request, redirect, url_for
import json

app = Flask(__name__)

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Joe"},
]


@app.route("/hello/<args>")
def hello(args):
    return f"Hello, {args}!"


@app.route("/")
@app.route("/home")
def home_page():
    return "Welcome to the home page!"


@app.route("/users/<int:id>")
def get_user_by_id(id):
    for user in users:
        if user["id"] == id:
            return user
            # return redirect(url_for("home_page"))
    return {"error": "User not found"}


@app.route("/users", methods=["GET"])
def get_user_by_id_post():
    request_data = request.get_json()
    request_id = request_data["id"]

    # return request_dict
    for user in users:
        if user["id"] == int(request_id):
            return user
    return {"error": "User not found"}


@app.route("/query_strings")
def query_strings():
    language = request.args.get("language", "something")
    return f"The language is {language}"


@app.route("/form-example", methods=["GET", "POST"])
def form_example():
    if request.method == "GET":
        return """<form method="POST">
        <input type="text" name="language">
        <input type="text" name="framework">
        <input type="submit">
        </form>"""
    elif request.method == "POST":
        language = request.form.get("language")
        framework = request.form.get("framework")
        return f"The language is {language}, and the framework is {framework}"


@app.route("/homes")
def home():
    # Use triple quotes to write multi-line string
    return """<h1> WELCOME HOME </h1>
    <p> This is a paragraph </p>"""


# return "<h1> WELCOME HOME </h1>"


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    # Use host and port to run app on external server
    app.run(host="0.0.0.0", port=80, debug=True)
