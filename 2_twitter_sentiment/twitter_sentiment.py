import os
import tweepy
from textblob import TextBlob

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')

access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('trump')

filename = 'tweets.csv'
f = open(filename, 'w')
f.write('tweet,screen_name,polarity,subjectivity\n')

for tweet in public_tweets:
    tweet_text = tweet.text.replace('\'', '\\\'')
    screen_name = tweet.author.screen_name
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    f.write('\'{}\',\'@{}\',{},{}\n'.format(tweet_text, screen_name, polarity, subjectivity))
