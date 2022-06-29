import bluetooth
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
trigPin = 24
echoPin = 25
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)


host =""
port=1
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
try:
    server.bind((host,port))
    print("bluetooth binding successful")
except:
    print("bluetooth binding unsuccessful")
server.listen(1) # enables the server to listen for incoming connections
client, address= server.accept()#waits for a client to connect to bluetooth and returns the handle object and address of the connected client
print("connection received from",address)
print("Client:", client)
print("=== ULTRASONIC TEST ===")
print("Connect G 5V 24 25 to G V T E of Ultrasonic")

def distance(trigPin, echoPin):
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)

    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()

    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()

    try:
        pulse_duration = pulse_end - pulse_start
    except:
        print("Calibrating")
        return -1

    distance = pulse_duration * 17150
    distance = round(distance+1.15, 2)
    return distance


while True:
    dist = distance(trigPin, echoPin)
    print("Measured Distance = {} cm".format(dist))
    client.send( "\nMeasured Distance : ")
    client.send(str(dist))
    client.send("cm")
    time.sleep(2)