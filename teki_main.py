import pyttsx3
import serial
import os
import time


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
    import detect_mask_video
    ser = serial.Serial("COM4", baudrate = 250000)
    while True:
        a = ser.read()
        ser.write((str(a)+ '\r\n').encode())
        print("aaaa" + str(detect_mask_video.averageX))
        time.sleep(.05)