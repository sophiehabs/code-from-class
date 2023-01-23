from flask import Flask

translations = {
    "en": "hello",
    "it": "ciao",
    "es": "hola",
    "de": "hallo"
}

app = Flask("translations")

@app.route("/")
def index():
    return "<h1>translations!</h1>"

@app.route("/<language>", methods = ["POST", "PUT"])
def update_translation(language):
    translations[language] = "default hello"
    return "translation created", 201

@app.route("/<language>")
def translate(language):
    if language in translations:
        return translations[language], 200
    else:
        return "language not found", 404

app.run()