import RPi.GPIO as GPIO
import time
def distance(TRIG,ECHO):
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        p_start=time.time()
    while GPIO.input(ECHO)==1:
        p_end=time.time()
    try:
        p_duration=p_end-p_start
    except:
        return -1
    distance=p_duration*17150
    return distance
GPIO.setmode(GPIO.BCM)
TRIG=24
ECHO=25
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    dis=distance(TRIG,ECHO)
    print("Measured distance={} cm".format(dis))
    time.sleep(0.25)
    
