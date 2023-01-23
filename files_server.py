from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("html/", "index.html")

app.run(port=8080, debug=True)