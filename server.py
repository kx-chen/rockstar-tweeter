from flask import Flask, request
from main import tweet
app = Flask(__name__)


@app.route("/")
def index():
    return "Go to /tweet."


@app.route('/tweet')
def tweet_route():
    """The endpoint for a webhook of sorts that should trigger a post.
    The request MUST have a dialog_number parameter which references which dialog it would like to post."""
    try:
        tweet(request.args.get('dialog_number'))
    except Exception:
        # TODO: Fix this up. Better error handling.
        return "There was an error."

    return "Tweeted"