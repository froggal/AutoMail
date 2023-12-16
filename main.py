import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv
import os
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

pw = os.environ("PASSWORD")
send = os.environ("SENDER")
receive = os.environ("RECEIVER")