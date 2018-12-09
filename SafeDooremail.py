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

body = 'The details of the follwoing person is given along with the captured image'

msg.attach(MIMEText(body,'plain'))

filename='image.jpg'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)

msgPayload = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(user.user_email, user.user_password)

server.sendmail(user.user_email,user.sender_email,msgPayload)

server.quit()
