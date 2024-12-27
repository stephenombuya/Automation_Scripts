import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Facebook API credentials
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN", "YOUR_PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "YOUR_VERIFY_TOKEN")

@app.route("/", methods=["GET"])
def webhook_verify():
    """
    Verifies webhook with Facebook.
    """
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return challenge, 200
    return "Verification failed", 403

@app.route("/", methods=["POST"])
def webhook_events():
    """
    Handles incoming webhook events from Facebook.
    """
    body = request.get_json()
    if body.get("object") == "page":
        for entry in body["entry"]:
            for event in entry.get("messaging", []):
                if "message" in event:
                    process_message(event)
                elif "postback" in event:
                    process_postback(event)
        return "EVENT_RECEIVED", 200
    return "Not a Messenger event", 404

def process_message(event):
    """
    Processes incoming messages.
    """
    sender_id = event["sender"]["id"]
    message_text = event["message"].get("text", "")

    if message_text:
        if message_text.lower() in ["hello", "hi"]:
            send_message(sender_id, "Hello! How can I assist you today?")
        elif message_text.lower() in ["help"]:
            send_message(sender_id, "Here are some commands you can try:\n1. Services\n2. Contact")
        else:
            send_message(sender_id, f"You said: {message_text}")

def process_postback(event):
    """
    Handles postback events triggered by button clicks.
    """
    sender_id = event["sender"]["id"]
    payload = event["postback"]["payload"]

    if payload == "GET_STARTED":
        send_message(sender_id, "Welcome to our bot! How can I assist you today?")
    elif payload == "CONTACT_INFO":
        send_message(sender_id, "You can reach us at contact@ourbusiness.com")

def send_message(recipient_id, message_text):
    """
    Sends a text message to the user.
    """
    url = "https://graph.facebook.com/v12.0/me/messages"
    headers = {"Content-Type": "application/json"}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
    }
    params = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(url, headers=headers, json=payload, params=params)
    if response.status_code != 200:
        print(f"Error sending message: {response.json()}")

@app.route("/set_persistent_menu", methods=["GET"])
def set_persistent_menu():
    """
    Sets a persistent menu for the bot.
    """
    url = f"https://graph.facebook.com/v12.0/me/messenger_profile"
    headers = {"Content-Type": "application/json"}
    payload = {
        "persistent_menu": [
            {
                "locale": "default",
                "composer_input_disabled": False,
                "call_to_actions": [
                    {
                        "type": "postback",
                        "title": "Get Started",
                        "payload": "GET_STARTED",
                    },
                    {
                        "type": "postback",
                        "title": "Contact Info",
                        "payload": "CONTACT_INFO",
                    },
                ],
            }
        ]
    }
    params = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(url, headers=headers, json=payload, params=params)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(port=5000, debug=True)
