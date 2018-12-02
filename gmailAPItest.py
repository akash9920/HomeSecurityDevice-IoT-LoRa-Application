import smtplib
#from userDefinedVariables import user
import userDefinedVariables as user
message = 'This is the sample message to test the api'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(user.user_email, user.user_password)

server.sendmail(user.user_email,user.sender_email,message)

server.quit()
