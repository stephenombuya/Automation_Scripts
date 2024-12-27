# Instagram Automation Bot

This project is a Python-based Instagram automation bot that interacts with the Instagram platform using the `instagrapi` library. It can perform actions like posting images, liking posts, and following users programmatically.

## Features

- **Automated Posting:** Upload images with captions to Instagram.
- **Engagement:** Like posts and follow users.
- **Secure Login:** Handles login securely using environment variables.
- **Logging:** Provides detailed logs for actions and errors.

---

## Requirements

- Python 3.7 or higher
- `instagrapi` library
- `dotenv` library

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/stephenombuya/Automation_Scripts/tree/main/Automation%20with%20Python/Instagram%20Bot
cd instagram-automation-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Instagram Credentials
1. Create a `.env` file in the project directory with the following content:
```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```
2. Replace `your_username` and `your_password` with your Instagram login credentials.

---

## Usage

### 1. Login to Instagram
The script uses your credentials from the `.env` file to log in securely.

### 2. Automated Posting
Prepare a directory with images to post and a `captions.txt` file with captions (one per line). Example:

#### Directory Structure
```
images/
    image1.jpg
    image2.jpg
captions.txt
```

#### Run the Script
```bash
python main.py --action post --image-path images/ --captions captions.txt
```

### 3. Like Posts
You can like posts by hashtags or user handles:
```bash
python main.py --action like --hashtag travel
```

### 4. Follow Users
You can follow users by providing a list of usernames in a file:
```bash
python main.py --action follow --usernames usernames.txt
```

---

## Configuration

### Actions
The script supports the following actions:
- `post`: Upload images to Instagram.
- `like`: Like posts based on hashtags or user handles.
- `follow`: Follow users listed in a file.

### Logging Level
Modify the `logging.basicConfig` configuration in the script to adjust the logging level (e.g., DEBUG, INFO, WARNING).

---

## Error Handling

- **Login Failures:** Ensures secure login and retries up to 3 times before exiting.
- **Invalid Input Files:** Logs errors for missing or malformed input files (e.g., missing captions).
- **Rate Limits:** Detects rate limits and pauses accordingly.
- **API Errors:** Logs errors from the Instagram API for debugging purposes.

---

## Logging

The script logs all actions to the console and a `bot.log` file. Example:
```
2024-12-27 10:00:00 - INFO - Logged in as your_username
2024-12-27 10:10:00 - INFO - Posted image: image1.jpg
2024-12-27 10:20:00 - INFO - Liked 50 posts with hashtag: travel
```

---

## Future Enhancements

- Schedule posts at specific times.
- Automatically respond to comments.
- Detect and skip duplicate posts.
- Analytics for engagement metrics (e.g., likes, comments).

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

