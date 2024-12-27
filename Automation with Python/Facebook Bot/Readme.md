# Facebook Bot Project Documentation

## Overview
This project is a comprehensive Facebook Messenger bot designed to interact with users dynamically. The bot supports rich media responses, persistent menus, and postback handling, making it suitable for a variety of applications, including customer support, e-commerce, and automated messaging.

The bot is built using **Python**, **Flask**, and the **Facebook Graph API**, with additional support for environment management using **dotenv**.

---

## Features
1. **Dynamic Message Handling:**
   - Processes user text messages and provides appropriate responses.

2. **Rich Media Support:**
   - Sends images, buttons, and templates for enhanced user interaction.

3. **Persistent Menu:**
   - Includes a menu for easy navigation, enabling users to access features like "Get Started" and "Contact Info."

4. **Postback Handling:**
   - Handles button clicks and triggers actions based on user selection.

5. **Webhook Integration:**
   - Uses a webhook to communicate with the Facebook Messenger API.

6. **Environment Management:**
   - Securely manages sensitive data like access tokens and verification tokens through environment variables.

7. **Deployment Ready:**
   - Can be tested locally with `ngrok` and deployed to platforms like Heroku or AWS.

---

## Prerequisites
1. **Facebook Developer Account**
   - Create an app and add the Messenger product.
   - Link the app to a Facebook Page.

2. **Python Environment**
   - Install Python 3.7+.

3. **Required Libraries**
   - Install dependencies using:
     ```bash
     pip install flask requests python-dotenv
     ```

4. **Ngrok (for local testing)**
   - Download and set up [ngrok](https://ngrok.com/).

---

## Project Structure
```plaintext
facebook_bot/
├── app.py               # Main bot logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── ngrok.sh             # Script for ngrok tunneling
└── README.md            # Documentation
```

---

## Setup and Configuration

### 1. Environment Variables
Create a `.env` file in the project directory and add the following:
```env
PAGE_ACCESS_TOKEN=your_page_access_token_here
VERIFY_TOKEN=your_verify_token_here
```

### 2. Flask Server
Run the bot locally using:
```bash
python app.py
```

### 3. Ngrok (Local Testing)
Start ngrok to expose the local server:
```bash
./ngrok http 5000
```

Update the Facebook App Webhook URL with the public ngrok URL.

---

## Key Endpoints

### 1. **Webhook Verification**
- **Route:** `/`
- **Method:** `GET`
- **Description:** Verifies the webhook setup with Facebook.

### 2. **Webhook Event Handling**
- **Route:** `/`
- **Method:** `POST`
- **Description:** Processes messages and postbacks from users.

### 3. **Set Persistent Menu**
- **Route:** `/set_persistent_menu`
- **Method:** `GET`
- **Description:** Configures a persistent menu for the bot.

---

## Core Functions

### 1. **process_message(event)**
- Handles incoming user messages.
- Responds based on message content.

### 2. **process_postback(event)**
- Handles postback events triggered by button clicks.
- Executes specific actions based on payloads.

### 3. **send_message(recipient_id, message_text)**
- Sends a text message to the user.
- Uses the Facebook Graph API to send messages.

### 4. **set_persistent_menu()**
- Configures the bot's persistent menu.
- Allows users to access predefined options easily.

---

## Example Usage
### Sending a Message
- When a user sends "hello," the bot responds with:
  ```
  Hello! How can I assist you today?
  ```

### Persistent Menu
- Options in the menu:
  - "Get Started"
  - "Contact Info"

### Rich Media
- Example JSON payload for sending an image:
  ```python
  payload = {
      "recipient": {"id": recipient_id},
      "message": {
          "attachment": {
              "type": "image",
              "payload": {"url": "IMAGE_URL", "is_reusable": True},
          }
      },
  }
  ```

---

## Deployment

### 1. Local Testing
- Use Flask and ngrok for testing:
  ```bash
  python app.py
  ./ngrok http 5000
  ```

### 2. Production Deployment
- Deploy to platforms like:
  - **Heroku**:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    heroku create
    git push heroku main
    ```
  - **AWS Lambda** or **Google Cloud Functions**.

---

## Future Enhancements
1. **AI Integration:**
   - Use NLP tools like Dialogflow or Wit.ai for advanced language understanding.

2. **Multimedia Responses:**
   - Include carousels, videos, and quick replies.

3. **Database Integration:**
   - Connect to a database for user data storage.

4. **Analytics:**
   - Integrate tools like Google Analytics for Messenger to track user interactions.

---

## References
- [Meta for Developers](https://developers.facebook.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api/)
- [Ngrok Documentation](https://ngrok.com/docs/)

---

## Author
This bot was created by an intelligent and skilled software engineer specializing in backend development, automation, and web development.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

