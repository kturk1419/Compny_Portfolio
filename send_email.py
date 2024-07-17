import os
import smtplib, ssl


def send_email(user_email, user_message, user_topic):
    host = 'smtp.gmail.com'
    port = 465
    username = 'kturk1419@gmail.com'
    password = 'nsxvivkxizgspwdh'
    receiver = 'kturk1419@gmail.com'
    context = ssl.create_default_context()
    message = f"""
    Subject: {user_topic}
    {user_message}
    From: 
    {user_email}
    """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)