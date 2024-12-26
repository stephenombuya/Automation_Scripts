import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server (using Gmail in this example)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("Email sent successfully")

# Example usage
sender_email = "your_email@gmail.com"
sender_password = "your_password"  # Use an app-specific password for security
receiver_email = "recipient@example.com"
subject = "Automated Email"
body = "This is an automated email sent from Python!"

send_email(sender_email, sender_password, receiver_email, subject, body)
