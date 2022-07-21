import Adafruit_DHT
import time
sensor = Adafruit_DHT.DHT11

pin = 4
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print("Humidity: ", humidity, "Temperature: ", temperature)
        time.sleep(0.25)
    else :
        print('Failed to get reading. Try again!')
