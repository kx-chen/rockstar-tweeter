

'''Post a message to twitter'''


from __future__ import print_function

import configparser

import os
import sys
import twitter



USAGE = '''Usage: tweet [options] message
  This script posts a message to Twitter.
  Options:
    -h --help : print this help
    --consumer-key : the twitter consumer key
    --consumer-secret : the twitter consumer secret
    --access-key : the twitter access token key
    --access-secret : the twitter access token secret
    --encoding : the character set encoding used in input strings, e.g. "utf-8". [optional]
  Documentation:
  If either of the command line flags are not present, the environment
  variables TWEETUSERNAME and TWEETPASSWORD will then be checked for your
  consumer_key or consumer_secret, respectively.
  If neither the command line flags nor the environment variables are
  present, the .tweetrc file, if it exists, can be used to set the
  default consumer_key and consumer_secret.  The file should contain the
  following three lines, replacing *consumer_key* with your consumer key, and
  *consumer_secret* with your consumer secret:
  A skeletal .tweetrc file:
    [Tweet]
    consumer_key: *consumer_key*
    consumer_secret: *consumer_password*
    access_key: *access_key*
    access_secret: *access_password*
'''


def print_usage_and_exit():
    print(USAGE)
    sys.exit(2)


class TweetRc(object):
    def __init__(self):
        self._config = None

    def GetConsumerKey(self):
        return self._GetOption('consumer_key')

    def GetConsumerSecret(self):
        return self._GetOption('consumer_secret')

    def GetAccessKey(self):
        return self._GetOption('access_key')

    def GetAccessSecret(self):
        return self._GetOption('access_secret')

    def _GetOption(self, option):
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


def main():
    config = TweetRc()

    api = twitter.Api(consumer_key=config.GetConsumerKey(), consumer_secret=config.GetConsumerSecret(),
                      access_token_key=config.GetAccessKey(), access_token_secret=config.GetAccessSecret(),
                      input_encoding="utf-8")
    try:
        # status = api.PostUpdate("@RockstarGames Hey. It's Paige Harris. We worked together on that job, remember? With you know who... I basically ran the thing while he took credit. I've got a new sideline you might be interested in.. high end scores, taken elegantly, using the latest tech. ")
        # status2 = api.PostUpdate("There's a Terrorbyte truck on Warstock that I can turn into our Nerve Center. Get one, we'll store it under the club, and get moving on this immedidately.", in_reply_to_status_id=1031438789577564160)
        status3 = api.PostUpdate("@RockstarGames Hey. Paige Harris here. You and me should do this. It makes sense. Buy the Terrorbyte truck on Warstock, we turn it into a Nerve Center, and start taking scores. I've got some great ideas, I just need someone to execute them.")
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)

    # print("{0} just posted: {1}".format(status.user.name, status.text))
    # print("{0} just posted: {1}".format(status2.user.name, status2.text))
    print("{0} just posted: {1}".format(status3.user.name, status3.text))


if __name__ == "__main__":
    main()

