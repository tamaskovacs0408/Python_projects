<h2>Email sender</h2>

  1. Because it uses Gmail, in the Google account we have to turn on 2-Step Verification.
  2. On the App passwords (still in Google account) click on the  *Select app* => *Other (Custom name)* => Add name of the app => Generate
  3. Copy the generated *Your app password for your device* code

Create variables for the `email_sender` (The email which sends the message) and the `email_password`, (Worthy import them from another file, or use Python's dotenv library) and `email_receiver` (where the message will be sent. For the test we can generate a temporary email address with <a href="https://temp-mail.org/">TempMail</a>).

Create the email preferences such as `subject` and `body`.

Create an instance from the `EmailMessage` and preferences from the variables created before.

Import the `ssl` and the `smtlib` libraries. Create `context` with the `ssl.create_default_context()`.

After that we use the `smtplib` to gain access to the sender email.
```py
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_reciever, em.as_string())
```