import configparser
import os
import sys
import twitter
from datetime import datetime


class TweetRc(object):
    def __init__(self):
        self._config = None

    def get_consumer_key(self):
        return self._get_option('consumer_key')

    def get_consumer_secret(self):
        return self._get_option('consumer_secret')

    def get_access_key(self):
        return self._get_option('access_key')

    def get_access_secret(self):
        return self._get_option('access_secret')

    def _get_option(self, option):
        try:
            return self._GetConfig().get('Tweet', option)
        except:
            return None

    def _GetConfig(self):
        if not self._config:
            self._config = configparser.ConfigParser()
            path = os.path.dirname(os.path.abspath(__file__)) + "/.tweetrc"
            self._config.read(path)
        return self._config


def prepare_post_dialog():
    """
    Prepares the post dialog.

    """
    dialogs_paige = [
        "@RockstarGames Hey. It's Paige Harris. We worked together on that job, remember? With you know who... I basically ran the thing while he took credit. I've got a new sideline you might be interested in.. high end scores, taken elegantly, using the latest tech. ",
        "@RockstarGames Hey. Paige Harris here. You and me should do this. It makes sense. Buy the Terrorbyte truck on Warstock, we turn it into a Nerve Center, and start taking scores. I've got some great ideas, I just need someone to execute them."]

    current_time = datetime.now().strftime('%H:%M:%S')
    current_time_hour = int(datetime.now().strftime("%H"))

    # If current time is even, post reply index 0
    if current_time_hour % 2 == 0:
        post_dialog = dialogs_paige[0] + current_time

    # else, current time is odd. post index 1 reply
    else:
        post_dialog = dialogs_paige[1] + current_time

    return post_dialog


def tweet():
    """
    Uses the python twitter library to tweet from an array of possible dialogs.

    """
    config = TweetRc()

    consumer_key = os.environ.get('consumer_key', None) or config.get_consumer_key()
    consumer_secret = os.environ.get('consumer_secret', None) or config.get_consumer_secret()
    access_token_key = os.environ.get('access_token', None) or config.get_access_key()
    access_token_secret = os.environ.get('access_secret', None) or config.get_access_secret()

    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_token_key, access_token_secret=access_token_secret,
                      input_encoding="utf-8")

    post_dialog = prepare_post_dialog()

    try:
        status = api.PostUpdate(post_dialog)
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        sys.exit(2)

    print("{0} just posted: {1}".format(status.user.name, status.text))


if __name__ == "__main__":
    tweet()
