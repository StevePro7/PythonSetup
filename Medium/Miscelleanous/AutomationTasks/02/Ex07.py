# 07. Automate Social Media Posts
import tweepy


def post_tweet(api_key, api_secret, access_token, access_secret, tweet):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    api.update_status(tweet)
