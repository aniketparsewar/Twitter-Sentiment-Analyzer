from django.shortcuts import render
import requests
import tweepy
from textblob import TextBlob


def tweet(word):
    if not word:
        word='Twitter'
    consumer_key = 'lI7sxfC9Jky8l4s92ynxi1WF6'
    consumer_secret = 'c1BPCYFEMgZfrtjz7Hr6rcYRc77zOS5OIOqX7a7LlFKRWmmyGx'

    access_token = '4567521216-nYWaj4NcxpWvHjHWKod8c31fzlOdPUfOzVNNt81'
    access_token_secret = 'T842HsFhYARg0BF3kHjdLwRwtTFaqjUKb5dTtrpisJS60'

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

