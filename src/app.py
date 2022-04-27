from crypt import methods
from distutils.log import debug
from flask import Flask

app = Flask(__name__)

todos = [{"label":"my first task for today", "done":False}, {"label": "go for dinner", "done":False}]

@app.route("/todos", methods=["GET"])
def handle_todos():
    return jsonify(todos)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)