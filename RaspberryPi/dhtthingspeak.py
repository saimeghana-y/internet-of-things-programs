import urllib.request
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

writeAPIKey = "YKGTGZAAC3PP227V" # enter write API key here
baseURL = "https://api.thingspeak.com/update?api_key={}".format(writeAPIKey)
sensor = Adafruit_DHT.DHT11
sensorPin = 26
GPIO.setmode(GPIO.BCM)  # Using BCM numbering

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensorPin)
        if humidity is not None and temperature is not None:
            # Format the readings to two decimal places
            humidity = '%.2f' % humidity
            temperature = '%.2f' % temperature

            # Sending the readings to thingspeak
            conn = urllib.request.urlopen(
                baseURL + '&field1={}&field2={}'.format(humidity, temperature))
            print(conn.read())

            # Closing the connection
            conn.close()

        time.sleep(5)  # wait 20 seconds before uploading next reading
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()