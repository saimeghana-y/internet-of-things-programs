import RPi.GPIO as g
import time
g.setmode(g.BCM)
g.setwarnings(False)
ground = 10
red = 11
green = 12
blue = 13
g.setup(red, g.OUT)
g.setup(green, g.OUT)
g.setup(blue, g.OUT)
g.setup(ground, g.OUT)
g.OUTPUT(ground, g.LOW)
p = g.PWM(11, 100)
q = g.PWM(12, 100)
r = g.PWM(13, 100)
p.start(0)
q.start(0)
r.start(0)
while True:
    color = input()
    if color == 'red':
        for x in range(100):
            p.ChangeDutyCycle(x)
            time.sleep(0.05)
        for x in range(100):
            p.ChangeDutyCycle(100 - x)
            time.sleep(0.05)
    elif color == 'green':
        for x in range(100):
            q.ChangeDutyCycle(x)
            time.sleep(0.05)
        for x in range(100):
            q.ChangeDutyCycle(100 - x)
            time.sleep(0.05)
    elif color == 'blue':
        for x in range(100):
            r.ChangeDutyCycle(x)
            time.sleep(0.05)
        for x in range(100):
            r.ChangeDutyCycle(100 - x)
            time.sleep(0.05)
