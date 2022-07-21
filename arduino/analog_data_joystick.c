# ## On Arduino
int VRx = A0;
int VRy = A1;
int xposition = 0;
int yposition = 0;
int mapx = 0
int mapy = 0;
void setup() {
Serial.begin(9600);
pinMode(VRx, INPUT);
pinMode(VRy, INPUT);
}
void loop()
{
xposition = analogRead(VRx);
yposition = analogRead(VRy);
mapx = map(xposition, 0, 1023, -512, 512);
mapy = map(yposition, 0, 1023, -512, 512);
Serial.print("X:");
Serial.print(mapx);
Serial.print("Y:");
Serial.print(mapy);
delay(100);
}


# ON Raspberry pi
import serial
import time
if _name_ == "_main_":
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()
while True:
if ser.in_waiting>0:
line = ser.readline().decode('utf-8').rstrip()
print(line)
