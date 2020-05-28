from django.shortcuts import render
import requests
import tweepy
from textblob import TextBlob


def tweet(word):
    if not word:
        word='Twitter'
    consumer_key = 'API-KEY'
    consumer_secret = 'API-KEY'

    access_token = 'access-token'
    access_token_secret = 'access-token'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Step 3 - Retrieve Tweets
    public_tweets = api.search(word)


    return public_tweets

def index(request):
    tweet_dict = {}
    #s_tweet = 'Twitter'
    s_tweet = request.GET.get('search_string')
    s = tweet(s_tweet)
    for tweets in s:
        #print(tweets.text)
        # Step 4 Perform Sentiment Analysis on Tweets
        analysis = TextBlob(tweets.text)
        #print if Polarity is not 0
        if analysis.sentiment[0] != 0:
            tweet_dict[tweets.text] =  analysis.sentiment[0]
            #print(analysis.sentiment)
            #print("")

    #print(tweet_dict)

    return render(request, 'twitter/home.html',{'tweet_dict':tweet_dict})

