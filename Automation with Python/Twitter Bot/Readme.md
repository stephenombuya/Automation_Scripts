# Twitter Automation Bot

This project is a Python-based Twitter automation bot that uses the Tweepy library to interact with the Twitter API. It can post tweets automatically from a predefined list or file, with customizable intervals between tweets.

## Features

- **Automated Tweet Posting:** Post tweets from a file or a predefined list.
- **Rate Limit Handling:** Automatically handles rate limits by pausing for 15 minutes when the rate limit is reached.
- **Logging:** Provides detailed logs for all operations, including errors and successful tweets.
- **Environment Variable Support:** Uses `.env` files for secure storage of API credentials.

---

## Requirements

- Python 3.6 or higher
- Tweepy library
- Python `dotenv` library

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/stephenombuya/Automation_Scripts/tree/main/Automation%20with%20Python/Twitter%20Bot
cd twitter-automation-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Twitter API
1. Create a Twitter Developer account and obtain the following credentials:
   - `TWITTER_CONSUMER_KEY`
   - `TWITTER_CONSUMER_SECRET`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`
2. Create a `.env` file in the project directory with the following content:
```env
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

---

## Usage

### 1. Load Messages from a File
Create a text file (e.g., `tweets.txt`) with one tweet per line. Example:
```
Hello, Twitter! This is an automated tweet.
Python automation is amazing!
Learn to code and automate your tasks.
```

### 2. Run the Script
```bash
python main.py
```

The script will:
- Load tweets from the specified file.
- Post each tweet at the configured interval (default: 1 hour).

---

## Configuration

### Interval Between Tweets
The time interval between tweets can be set by modifying the `tweet_interval` variable in the `main.py` file (in seconds):
```python
tweet_interval = 3600  # 1 hour
```

### Default Messages
If the file specified in `tweet_file` is not found, the script will use the predefined list of messages in the `messages` variable:
```python
messages = [
    "Hello, Twitter! This is an automated tweet.",
    "Python automation is amazing!",
    "Learn to code and automate your tasks."
]
```

---

## Error Handling

- **File Not Found:** If the specified tweet file is not found, the script logs an error and uses the predefined list of messages.
- **Twitter API Errors:** Handles Tweepy exceptions and pauses for 15 minutes if the rate limit is reached.
- **Other Errors:** Logs the error details and raises the exception for further debugging.

---

## Logging

All actions are logged to the console with timestamps and log levels (INFO, ERROR, WARNING). Example:
```
2024-12-27 10:00:00 - INFO - Tweet posted: Hello, Twitter! This is an automated tweet.
2024-12-27 10:01:00 - INFO - Waiting for 60 minutes before the next tweet...
```

---

## Future Enhancements

- Support for scheduling tweets at specific times.
- Sentiment analysis for tweets before posting.
- Integration with a database for better message management.
- Multi-account support.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or suggestions, feel free to contact:
- **GitHub:** [stephenombuya](https://github.com/stephenombuya)

