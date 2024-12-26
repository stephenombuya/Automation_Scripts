import tweepy
import time

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

def post_tweet(message):
    try:
        api.update_status(message)
        print(f"Tweet posted: {message}")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")

# Example usage
messages = [
    "Hello, Twitter! This is an automated tweet.",
    "Python automation is amazing!",
    "Learn to code and automate your tasks."
]

for message in messages:
    post_tweet(message)
    time.sleep(3600)  # Wait for 1 hour between tweets
