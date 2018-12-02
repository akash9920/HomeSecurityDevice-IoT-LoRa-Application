import smtplib
import userDefinedVariables as user
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

subject = 'SafeDoor'
msg = MIMEMultipart()

msg['From'] = user.user_email
msg['To'] = user.sender_email
msg['Subject'] = subject

body = 'This is the sample message to test the api'

msg.attach(MIMEText(body,'plain'))

msgPayload = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(user.user_email, user.user_password)

server.sendmail(user.user_email,user.sender_email,msgPayload)

server.quit()
