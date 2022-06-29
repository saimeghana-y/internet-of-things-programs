import RPi.GPIO as GPIO
import time

print("=== RGB LED TEST ===")
print("Connect 10 11 12 13 to G R Gr B of RGB LED")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
commonCathode = 10
red = 11
green = 12
blue = 13
def ledColour(colour="none"):
    for x in range(10, 11):
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.LOW)
    if(colour == "red"):
        GPIO.output(red, GPIO.HIGH)
    elif(colour == "green"):
        GPIO.output(green, GPIO.HIGH)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    elif(colour == "blue"):
        GPIO.output(blue, GPIO.HIGH)

while True:
   ledColour("green")
   time.sleep(1)
   ledColour("red")
   time.sleep(1)
   ledColour("blue")
   time.sleep(1)

#GPIO.output(red, GPIO.LOW)
#GPIO.output(green, GPIO.LOW)
#GPIO.output(blue, GPIO.LOW)