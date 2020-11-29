import pyttsx3
import serial
import os
import time
import zmq
import asyncio

context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.setsockopt_string(zmq.SUBSCRIBE, '')
sub.setsockopt(zmq.CONFLATE, 1)
sub.connect('tcp://localhost:5555')

def begin():
    print("Choose a language: ")
    print("╔═════════════╦════════════════╦═════════════╗")
    print("║ English [1] ║ Castellano [2] ║ Euskera [3] ║")
    print("╚═════════════╩════════════════╩═════════════╝\n")
    a = input("> ")
    return a

languageSelected = False
time.sleep(.5)
while languageSelected == False:
    lambda: os.system('cls')() #clear
    a = begin()
    if a == "1":
        print("English selected!")
        languageSelected = True
    if a == "2":
        print("¡Castellano seleccionado!")
        languageSelected = True
    if a == "3":
        print("Euskera aukeratuta!")
        languageSelected = True



if languageSelected == True:
    comNumber = input("Please enter the com number (for COM2 type 2, for example)\n> ")
    #delay = input("Delay between readings (ms)? (if too short can clog the system)\n> ")
    os.startfile("detect_mask_video.py")
    try:
        ser = serial.Serial("COM" + comNumber, baudrate = 1000000)
    except:
        print("Error while opening Serial: COM" + str(comNumber))
    while True:
        msg = sub.recv_string()
        ser.write((str(msg)+ '\r\n').encode())
        print(msg)
        #time.sleep(float(delay))
        if msg == "quit":
            break
