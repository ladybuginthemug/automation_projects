#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import os.path
import smtplib
import ssl

def generate(subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = EmailMessage()
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)

    return message


def send(message, receiver):
    """Sends the message to the configured SMTP server."""
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start a secure TLS connection

        # Login to your Gmail account
        sender = 'sender@mail.com'
        password = '1234'
        server.login(sender, password)

        # Send the email
        server.send_message(message, sender, receiver)
        print('Email sent successfully!')

        # Disconnect from the server
        server.quit()

    except Exception as e:
        print('Error:', str(e))



