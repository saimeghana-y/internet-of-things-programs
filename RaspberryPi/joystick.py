import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
ser.reset_input_buffer()

while True:
    if ser.in_waiting > 0:
        X = ser.readline().decode('utf-8').rstrip()
        print(X)