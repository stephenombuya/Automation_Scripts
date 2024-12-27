import os
import logging
from instagrapi import Client
from dotenv import load_dotenv
from typing import List

# Load environment variables
load_dotenv()

# Configure logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("bot.log")]
)

# Instagram credentials
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Initialize Instagram client
client = Client()

def validate_env_vars():
    """Ensure necessary environment variables are set."""
    if not USERNAME or not PASSWORD:
        logging.critical("Missing Instagram credentials in environment variables.")
        raise EnvironmentError("INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD are required.")

def login():
    """Log in to Instagram using credentials from environment variables."""
    try:
        client.login(USERNAME, PASSWORD)
        logging.info("Logged in successfully as %s", USERNAME)
    except Exception as e:
        logging.error("Login failed: %s", e)
        raise

def load_images(image_dir: str) -> List[str]:
    """Load and validate image files from a directory."""
    images = sorted([os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('.jpg', '.png'))])
    if not images:
        logging.warning("No images found in directory: %s", image_dir)
    return images

def load_captions(captions_file: str) -> List[str]:
    """Load captions from a file."""
    try:
        with open(captions_file, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        logging.error("Captions file not found: %s", captions_file)
        raise

def post_images(image_dir: str, captions_file: str):
    """Post images with captions from a specified directory."""
    images = load_images(image_dir)
    captions = load_captions(captions_file)

    if len(images) != len(captions):
        logging.warning("Number of images (%d) and captions (%d) do not match.", len(images), len(captions))

    for i, image in enumerate(images):
        caption = captions[i] if i < len(captions) else ""
        try:
            client.photo_upload(image, caption)
            logging.info("Posted image: %s with caption: %s", image, caption)
        except Exception as e:
            logging.error("Failed to post image: %s. Error: %s", image, e)

def like_posts_by_hashtag(hashtag: str, max_likes: int = 50):
    """Like posts under a specific hashtag."""
    try:
        medias = client.hashtag_medias_recent(hashtag, amount=max_likes)
        for media in medias:
            client.media_like(media.id)
            logging.info("Liked post with ID: %s", media.id)
    except Exception as e:
        logging.error("Error liking posts for hashtag '%s': %s", hashtag, e)

def follow_users_from_file(usernames_file: str):
    """Follow users listed in a file."""
    try:
        with open(usernames_file, "r") as file:
            usernames = [line.strip() for line in file.readlines()]

        for username in usernames:
            try:
                user_id = client.user_id_from_username(username)
                client.user_follow(user_id)
                logging.info("Followed user: %s", username)
            except Exception as e:
                logging.error("Failed to follow user: %s. Error: %s", username, e)
    except FileNotFoundError:
        logging.error("Usernames file not found: %s", usernames_file)
        raise

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Instagram Automation Bot")
    subparsers = parser.add_subparsers(dest="action", required=True)

    # Post action
    post_parser = subparsers.add_parser("post", help="Post images with captions")
    post_parser.add_argument("--image-path", required=True, help="Path to the directory containing images")
    post_parser.add_argument("--captions", required=True, help="Path to the captions file")

    # Like action
    like_parser = subparsers.add_parser("like", help="Like posts by hashtag")
    like_parser.add_argument("--hashtag", required=True, help="Hashtag to like posts from")
    like_parser.add_argument("--max-likes", type=int, default=50, help="Maximum number of posts to like")

    # Follow action
    follow_parser = subparsers.add_parser("follow", help="Follow users from file")
    follow_parser.add_argument("--usernames", required=True, help="Path to the file containing usernames to follow")

    args = parser.parse_args()

    validate_env_vars()
    login()

    if args.action == "post":
        post_images(args.image_path, args.captions)
    elif args.action == "like":
        like_posts_by_hashtag(args.hashtag, args.max_likes)
    elif args.action == "follow":
        follow_users_from_file(args.usernames)
