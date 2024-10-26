from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Called endpoint '/'\n"


@app.route("/api/<path>")
def show_user_profile(path):
    return f"Called api endpoint of path /api/{escape(path)}\n"
