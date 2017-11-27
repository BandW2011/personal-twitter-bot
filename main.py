#!/usr/bin/python3
import config, datetime, sys, threading, tweepy
from random import randint
from threading import Timer



rate = 60.0 * 60.0 * 24 # determines how often bot tweets, in seconds
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
with open('adjectives.txt') as f:
    adjectives = f.readlines()
adjectives = [line.strip() for line in open('adjectives.txt')]



def generic_tweet(text):
    api.update_status(text[:280])

def interval_func():
    generic_tweet(bot_tweet())
    print("Tweeted at " + datetime.datetime.now().isoformat())
    rate = 60.0 * 60.0 * randint(24, 48)
    Timer(rate, interval_func).start()

def bot_tweet():
    tweet = ""       
    while True:
        current_time = datetime.datetime.now().hour

        if current_time < 12:
            tweet = "Good morning!\nToday's gonna be "
        elif current_time >= 19:
            tweet = "Good morning.\nToday was "
        else:
            tweet = "Good morning.\nToday is "
        
        tweet += adjectives[randint(0, len(adjectives) - 1)]
        tweet += ".\n"
        tweet += str(randint(0, 9)) + "-" + "%02d" % randint(0, 99) + "-" + "%03d" % randint(0, 999)
        tweet += "\n#bot v" + config.version

        if len(tweet) <= 140:
            break
    return tweet

if sys.argv.__contains__("--manual-tweet"):
    tweet_index = sys.argv.index("--manual-tweet") + 1
    if tweet_index < len(sys.argv):
        generic_tweet(sys.argv[tweet_index])
    else:
        print("No tweet given!")
else:
    print("No tweet given.") #interval_func()
