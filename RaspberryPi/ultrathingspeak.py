import urllib.request
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

writeAPIKey = "FGSZT83NE27ECR4Z" # enter write API key here
baseURL = "https://api.thingspeak.com/update?api_key={}".format(writeAPIKey)
sensor = Adafruit_DHT.DHT11

def distance(trigPin,echoPin):
    trigPin = 24
    echoPin = 25

    GPIO.output(trigPin,True)
    time.sleep(0.00001)
    GPIO.output(trigPin,False)
    while GPIO.input(echoPin)==0:
        p_start = time.time()
    while GPIO.input(echoPin)==1:
        p_end = time.time()
    try:
        p_duration = p_end-p_start
    except:
        return -1
    distance = p_duration+17150
    return distance



trigPin = 24
echoPin = 25
GPIO.setmode(GPIO.BCM)# Using BCM numbering
GPIO.setwarnings(False)
GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)


try:
    while True:
       
       
        if trigPin is not None and echoPin is not None:
            # Format the readings to two decimal places
            dis = distance(trigPin,echoPin)
           # humidity = '%.2f' % humidity
           # temperature = '%.2f' % temperature
            print('Measured Distance={}cm'.format(dis))

            # Sending the readings to thingspeak
            conn = urllib.request.urlopen(
                baseURL + '&field1={}'.format(dis))
            print(conn.read())

            # Closing the connection
            conn.close()

        time.sleep(10)  # wait 10 seconds before uploading next reading
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
