import pyttsx3
import serial
import os
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://*:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

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
    #delay = input("Delay between readings (s)? (if too short can clog the system)\n> ")
    os.startfile("detect_mask_video.py")
    try:
        ser = serial.Serial("COM" + comNumber, baudrate = 345600)
    except:
        print("Error while opening Serial: COM" + str(comNumber))
    while True:
        try:
            message = socket.recv_string()
            ser.write((str(message)+ '\r\n').encode())
            print(message)

        except:
            pass
        if message == "quit":
            break
