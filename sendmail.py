#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['receive@gmail.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = str(sys.argv[1])
msg['From'] = 'aaaa@gmail.com'
msg['Reply-to'] = 'aaa@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Hi, please find the attached file")
msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
msg.attach(part)
 

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("aaa@gmail.com", "mypassword")
 
server.sendmail(msg['From'], emaillist , msg.as_string())
