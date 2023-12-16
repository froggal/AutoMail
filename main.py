# import modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv
import os

# load dotenv
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
print('DOTENV LOAD SUCESS!')
print('----------')

# load account
pw = os.getenv("PASSWORD")
send = os.getenv("SENDER")
receive = os.getenv("RECEIVER")
print('ACCOUNT LOAD SUCESS!')
print('----------')

# set up SMTP
smtp = smtplib.SMTP(os.getenv("SERVER"), os.getenv("PORT"))
smtp.ehlo()
smtp.starttls()
smtp.login(send, pw)
print('SMTP SET UP SUCESS!')
print('----------')

# send mail function
def sendMail(subject, text): 
    msg = MIMEMultipart()
    msg['Subject'] = subject
    part = MIMEText(text)
    msg.attach(part)
    msg["To"] = receive
    smtp.sendmail(send, receive, msg.as_string())
    print(f'SEND SUCESS! \n ---------- \n Sender : {send} \n Receiver : {receive}')