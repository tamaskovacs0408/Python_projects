from email.message import EmailMessage
from userdata import user_email, user_password

email_sender = user_email
email_password = user_password
email_reciever = ""

subject = "Python email"
body = """
This email is sent by a Python code.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["Subject"] = subject
em.set_content(body)

