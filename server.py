from flask import Flask, request
from main import tweet
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Go to /tweet."


@app.route('/tweet')
def tweet_route():
    """
    The endpoint for a webhook of sorts that should trigger a post.

    """
    try:
        tweet()
    except Exception as e:
        # TODO: Fix this up. Better error handling.
        print(e)
        return "There was an error."

    return "Tweeted"
