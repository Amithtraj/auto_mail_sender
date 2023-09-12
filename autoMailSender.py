import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            
            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage:
sender_email = 'Your email'
sender_password = 'yourpassword'
receiver_email = 'receiveremail@gmail.com'
subject = 'Test Subject'
message = 'This is a test message.'

send_email(sender_email, sender_password, receiver_email, subject, message)
