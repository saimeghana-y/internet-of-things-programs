import smtplib
from time
import sleep
import RPi.GPIO as GPIO
from sys
import exit
from_email = '<my-email>'
receipients_list = ['<receipient-email>']
cc_list = []
subject = 'Hello: Message from Raspberry Pi'
message = 'Input given by the user'
username = '<Gmail-username>'
password = '<password>'
server = 'smtp.gmail.com:587'
inp = int(input())

def sendmail(from_addr, to_addr_list, cc_addr_list, subject, message,login, password,smtpserver):
    header = 'From: %s \n' % from_ addr
    header += 'To: %s \n' % ','.join(to_addr_list)
    header += 'Cc: %s \n' % ','.join(cc_addr_list)
    header += 'Subject: %s \n \n' % subject
    message = header + message
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    
while True:
    try:
      if(inp == 1):
          sendmail(from_email, receipients_list, cc_list, subject,message, username, password,server)
          sleep(.01)
    except KeyboardInterrupt:
        exit()
