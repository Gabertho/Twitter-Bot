import tweepy
import time 

auth = tweepy.OAuthHandler('YOUR PERSONAL API KEY','YOUR PERSONAL API KEY PASSWORD')

auth.set_access_token('YOUR PERSONAL ACCESS TOKEN','YOUR PERSONAL ACCES TOKEN PASSWORD')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #Guarantee that we will not reach the maximum allowed requests from Twitter API.


user = api.me

search = 'Brasil' #The word we are going to search on tweets.
nrTweets= 1000 #The maximum number of tweets that we are going to search.
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite() 
        print('Tweet retweeted')
        tweet.retweet()
        time.sleep(10) #Pause os 10 seconds.
    except tweepy.TweepError as e:
        print(e.reason) #Prints the error reason.
    except StopIteration:
        break #Exit the Iteration
