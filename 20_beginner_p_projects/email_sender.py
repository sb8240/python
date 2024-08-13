from email.message import EmailMessage
import apppasss
import ssl
import smtplib

email_sender = 'hopepope911@gmail.com'
email_password = apppasss.a

email_reciever = 'hopepope911@gmail.com'

subject = 'Hello i am pyhton3 testing for mail transfer...'
body = '''my unmatched perspecacity coupled with sheered indefatigability, makes me a feared opponent in any realm of human endeavor.'''

email_message = EmailMessage()
email_message['From'] = email_sender
email_message['To'] = email_reciever
email_message['subject'] = subject
email_message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, email_message.as_string())
