import serial
import time
ser = serial.Serial("COM4", baudrate = 250000)
a = 0
while True:
    #a = input("enviar por serial:\n> ")
    if a < 179:
        a = a + 60
    else: 
        a = 0
    ser.write((str(a)+ '\r\n').encode())
    print(a)
    time.sleep(.05)