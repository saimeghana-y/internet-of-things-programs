import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)
while True:
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(10,GPIO.LOW)
    sleep(1)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(10,GPIO.HIGH)
    sleep(1)
