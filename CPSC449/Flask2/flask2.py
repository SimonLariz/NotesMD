import flask

app = flask.Flask(__name__)

name = [
    {id: 1, "name": "John"},
    {id: 2, "name": "Paul"},
    {id: 3, "name": "George"},
]

@app


