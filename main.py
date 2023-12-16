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
pw = os.environ(["PASSWORD"])
send = os.environ(["SENDER"])
receive = os.environ(["RECEIVER"])

# set up SMTP
smtp = smtplib.SMTP(os.environ["SERVER"], os.environ["PORT"])
smtp.ehlo()
smtp.starttls()
smtp.login(send, pw)