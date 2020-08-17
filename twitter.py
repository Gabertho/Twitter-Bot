import tweepy
import time 

auth = tweepy.OAuthHandler('uOx4nLBThjG45o17AleIe0FDr','326F8cSpfD1zrpB41JKFuXHDFdC9ea223mYiQdcO94mFI8nEez')

auth.set_access_token('1295218133830180865-ZPfzVdX5WPFRkD1zZqMbf5K9WtQmYT','EnEZaW5MRGRSDrJVAsPo1LzZVqCAMgRkgkOiB6jNNOxEA')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me

search = 'Brasil'
nrTweets= 1000

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print('Tweet retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
