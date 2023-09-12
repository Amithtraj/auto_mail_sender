# Title: Automated Email Sender

# Description:
This Python script provides a simple utility for sending automated emails using the smtplib library. Users can specify the sender's email address, password (or app password if two-factor authentication is enabled), recipient's email address, subject, and the message body. The script creates a MIMEText object to represent the email, attaches the message, and connects to the SMTP server to send the email. It includes error handling for potential exceptions during the process.

# Note: Replace the placeholder email addresses and passwords with your actual credentials. It is recommended to use secure methods for handling sensitive information. Additionally, ensure that "less secure apps" is enabled in your email account settings or use an App Password if two-factor authentication is enabled.
