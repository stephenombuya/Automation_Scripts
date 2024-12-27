import tweepy
import time
import os
import logging
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Twitter API credentials
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def post_tweet(message):
    """
    Posts a tweet using the Twitter API.

    Args:
        message (str): The message to be posted as a tweet.
    """
    try:
        api.update_status(message)
        logging.info(f"Tweet posted: {message}")
    except tweepy.TweepyException as e:
        logging.error(f"Error posting tweet: {e}")
        if e.api_codes and 88 in e.api_codes:
            logging.warning("Rate limit reached. Pausing for 15 minutes.")
            time.sleep(15 * 60)  # Wait for rate limit reset
        else:
            raise  # Raise other errors to handle them elsewhere

def load_messages(file_path):
    """
    Loads tweet messages from a file.

    Args:
        file_path (str): Path to the file containing tweet messages.

    Returns:
        list: List of tweet messages.
    """
    try:
        with open(file_path, "r") as file:
            messages = [line.strip() for line in file if line.strip()]
            logging.info(f"{len(messages)} messages loaded from {file_path}")
            return messages
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

# Example usage
if __name__ == "__main__":
    # Load tweets from a file or define them manually
    tweet_file = "tweets.txt"  # Replace with your file path
    messages = load_messages(tweet_file) or [
        "Hello, Twitter! This is an automated tweet.",
        "Python automation is amazing!",
        "Learn to code and automate your tasks."
    ]

    # Set the interval between tweets (in seconds)
    tweet_interval = 3600  # 1 hour

    for message in messages:
        post_tweet(message)
        logging.info(f"Waiting for {tweet_interval // 60} minutes before the next tweet...")
        time.sleep(tweet_interval)
