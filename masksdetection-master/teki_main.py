import pyttsx3
import serial
import os
exec(open(os.getcwd + "\\detect_mask_video.py").read())
def begin():
    print("Choose a language: ")
    print("╔═════════════╦════════════════╦═════════════╗")
    print("║ English [1] ║ Castellano [2] ║ Euskera [3] ║")
    print("╚═════════════╩════════════════╩═════════════╝\n")
    a = input("> ")
    return a

languageSelected = False
while languageSelected == False:
    b = begin()
    if b == "1":
        print("English selected!")
        languageSelected = True
    if b == "2":
        print("¡Castellano seleccionado!")
        languageSelected = True
    if b == "3":
        print("Euskera aukeratuta!")
        languageSelected = True

print("blablabla código")