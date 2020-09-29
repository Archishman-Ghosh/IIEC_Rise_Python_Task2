import speech_recognition as sr
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Listening.....')
    audio = r.listen(source)
    print('\nCommand received.')

cmd = r.recognize_google(audio)
print("\nYou said : '{}'".format(cmd))

if 'my' in cmd and 'API' in cmd:
    os.system('start msedge 192.168.1.7/IIEC_Task2.html')

print("\nCOMMAND EXECUTED!!!")