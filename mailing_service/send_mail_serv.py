import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
def send_email(movie_name):

    subject = '🍿 Now Streaming: New Movies are Live!'
    body = f"""Hi There🙂\n\nThis is an automated notification.\n
            A new movie has been successfully published to the streaming catalog.\\n
            You can find movie details below...!\n \n {movie_name}"""
    smtp_server = "smtp.gmail.com"
    smtp_port = int(os.getenv('smtp_port'))
    from_email = os.getenv('sender_email')
    password = os.getenv('password')
    to_email = os.getenv('receiver_email')

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

#send_email('Greetings...!🙂', 'Hello,\n\nI hope this message finds you well. I am writing to follow up on our recent discussion and to confirm the next steps. Please let me know if any additional information is required.\n\nRegards,\nSunil')