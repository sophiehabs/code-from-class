# 0. import flask
from flask import Flask

# 1. create the flask application
app = Flask("server")

@app.route("/")
def index():
    return """
    <h1>Hello MCSBT</h1>
    <p>
        <a href="/potato">link</a>
    </p>
    """

@app.route("/potato")
def jj():
    return "Hey y'all"

@app.route("/users/<user>")
def say_hello(user):
    if user == "pepe":
        return "hey Professor"
    else:
        return "hello " + user

# 2. create a route
# 3. run the application
app.run()
