import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(10,IO.OUT)
IO.setup(11,IO.OUT)
IO.setup(12,IO.OUT)
p=IO.PWM(10,100)
p.start(20)
q=IO.PWM(11,100)
r=IO.PWM(12,100)
q.start(100)
r.start(50)
while 1:
    for x in range(65):
        p.ChangeDutyCycle(x+25)
        time.sleep(1)
        q.ChangeDutyCycle(x+25)
        time.sleep(1)
        r.ChangeDutyCycle(x+25)
        time.sleep(1)
        p.ChangeDutyCycle(25-x)
        time.sleep(1)
        q.ChangeDutyCycle(25-x)
        time.sleep(1)
        r.ChangeDutyCycle(25-x)
       
        
