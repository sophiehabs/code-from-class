from flask import Flask, render_template

app = Flask("Exercise 3")


@app.route("/")
def index():
    return render_template(
        "home.html"
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        price_per_tortita="15"
    )

app.run(port=8080, debug=True)
