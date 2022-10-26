from email.message import EmailMessage
from userdata import user_email, user_password
import ssl
import smtplib

email_sender = user_email
email_password = user_password
email_reciever = "mimox13542@3mkz.com"

subject = "Python email"
body = """
This email is sent by a Python code.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_reciever, em.as_string())