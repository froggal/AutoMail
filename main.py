# import modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv
import os

# load dotenv
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# load account/server
pw = os.getenv("PASSWORD")
send = os.getenv("SENDER")
receive = os.getenv("RECEIVER")

# set up SMTP
smtp = smtplib.SMTP(os.getenv("SERVER"), os.getenv("PORT"))
smtp.ehlo()
smtp.starttls()
smtp.login(send, pw)

# send mail function
def sendMail(subject, text): 
    msg = MIMEMultipart()
    msg['Subject'] = subject
    part = MIMEText(text)
    msg.attach(part)
    msg["To"] = receive
    smtp.sendmail(send, receive, msg.as_string())