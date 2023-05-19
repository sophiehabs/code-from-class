from flask import Flask, render_template

app = Flask("Exercise 1")


@app.route("/<name>/<height>") #two parameters!! can only access through eg sophie/1.68
def index(name, height):
    return render_template(
        "exercise1.html",
        name=name,
        height=height,
        logged_in=True)

app.run(port=8080, debug=True)
