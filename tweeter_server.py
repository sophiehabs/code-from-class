from flask import Flask, request

app = Flask(__name__)

tweets = []


@app.route("/tweets", methods=["POST"])
def handle_tweet():
    tweet = request.get_json()
    tweets.append(tweet)
    return "Tweet created", 201


@app.route('/')
def index():
    # Exercise: create an HTML string that represents
    #           the list of tweets

    html_string = ""

    for tweet in tweets:
        username = tweet["username"]
        content = tweet["content"]
        list_element = "<li>" + username + ": " + content + "</li>"
        html_string = html_string + list_element

    return "<ol>" + html_string + "</ol>"


app.run(port=8080, debug=True)