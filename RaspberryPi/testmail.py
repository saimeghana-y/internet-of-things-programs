import smtplib
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 
GMAIL_USERNAME = '20135a0508@gvpce.ac.in' 
GMAIL_PASSWORD = '8688202060'
sensor = Adafruit_DHT.DHT11
sensorPin = 26
h,t= Adafruit_DHT.read_retry(sensor, sensorPin)
if h is not None and t is not None:
    h = '%.2f' % h
    t= '%.2f' % t

GPIO.setmode(GPIO.BCM)
class Emailer:
    def sendmail(self, recipient, subject, content):

      
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.starttls()
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()
sendTo = 'siddardha2001@gmail.com'
emailSubject = "Temparature mail"
emailContent = "Temparature ="+t+"  Humidity ="+h
sender.sendmail(sendTo, emailSubject, emailContent)
print("Email Sent")
