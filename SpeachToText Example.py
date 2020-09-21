import speech_recognition as sr

r = sr.Recognizer()

''' Euskera --> "eu-ES"  ----   English --> "en-US"  ----  Castellano --> "es-ES" '''
print("Speak you CrackHead")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=3)
    print("Analizando")
    try:
        text = r.recognize_google(data, language="eu-ES")
        print(text)
    except:
        print("No se ha detectado nada")