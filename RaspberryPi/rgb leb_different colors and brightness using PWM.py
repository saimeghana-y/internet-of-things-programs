import time
import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(23,IO.OUT)
IO.setup(32,IO.OUT)
IO.setup(33,IO.OUT)
p=IO.PWM(23,100)
p.start(0)
q=IO.PWM(32,100)
r=IO.PWM(33,100)
q.start(100)
r.start(50)
while 1:
    for x in range(50):
        p.ChangeDutyCycle(x)
        q.ChangeDutyCycle(x)
        r.ChangeDutyCycle(x)
        time.sleep(1)
    for x in range(50):
        p.ChangeDutyCycle(50-x)
        q.ChangeDutyCycle(50-x)
        r.ChangeDutyCycle(50-x)
        time.sleep(1)
