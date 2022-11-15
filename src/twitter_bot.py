import os as _os
import dotenv as _dotenv
import time as _time
import tweepy as _tweepy
import services as _services
import unsplash as _unsplash

_dotenv.load_dotenv

API_KEY = _os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET_KEY"]
ACCESS_TOKEN = _os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


# define a function to access the twitter api
def _get_twitter_api():
    auth = _tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = _tweepy.API(
        auth, wait_on_rate_limit=True)

    return twitter_api


# define a function to write the tweet
def _write_tweet():
    tweet = _services.get_tweet()
    twitter_api = _get_twitter_api()
    twitter_api.update_status(tweet)


_write_tweet()
