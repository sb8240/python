# import smtplib
# import apppasss
# from email import encoders
# from email.mime.text import MIMEText
# # from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# server = smtplib.SMTP('smtp.gmail.com',465)

# server.ehlo()

# email_sender = 'hopepope911@gmail.com'
# email_reciever = 'hopepope911@gmail.com'
# password_p= apppasss.a

# server.login("hopepope911@gmail.com", password_p )

# msg = MIMEMultipart()
# msg['From'] = email_sender
# msg['To'] = email_reciever
# msg['Subject'] = 'just a test'

# with open('message.txt','r') as f:
#     a=f.read()

# msg.attach(MIMEText(a,'plain'))

# file_name = 'images.jpg'
# attachment = open(file_name,'rb')

# payload_object = ('application','octet-stream') #The payload is either a string or bytes object, in the case of simple message objects, or a list of EmailMessage objects, for MIME container documents such as multipart/* and message/rfc822 message objects.
# # # The "octet-stream" subtype is used to indicate that a body contains arbitrary binary data. The set of currently defined parameters is: (1) TYPE -- the general type or category of binary data. This is intended as information for the human recipient rather than for any automatic processing.

# payload_object.set_payload(attachment.read())

# encoders.encode_base64(payload_object)
# payload_object.add_header('Content-Disposition',f'attachment; filename={file_name}')
# msg.attach(payload_object)

# text = msg.as_string()
# server.sendmail(email_sender,email_reciever)
