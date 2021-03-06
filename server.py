from tweet import tweet
from app import create_app

app = create_app()


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
