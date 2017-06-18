#!/usr/bin/python

import smtplib
import base64

filename = '/root/Pythonfiles/ac.txt'

fo = open('abc.txt', "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent) #base64

TO = 'chandrasekharlsetty@gmail.com'
SUBJECT = 'SENDING TEST SMTP EMAIL'
TEXT = 'Here is the test message'

#GMAIL. 

gmail_sender = 'chandradevops86@gmail.com'
gmail_passwd = 'cs9s909powe'

server = smtplib.SMTP('smtp.gmail.com' , 587)
server.ehlo()
server.starttls()
server.ehlo
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n' .join([
        'To: %s' % TO,
         'From: %s' % gmail_sender,
         'Subject: %s' % SUBJECT,
         '',
         TEXT
         ])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print('Email sent')
except:
    print("Cannot send Email")

server.quit()

