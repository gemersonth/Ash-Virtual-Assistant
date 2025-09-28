from voice_recognition import Recognize
from speaker import Speaker
from datetime import datetime
import time
import os
import sys


class Assistant:
    def __init__(self):
        self.recognize = Recognize()
        self.speaker = Speaker()

        if ( sys.platform == "linux" or sys.platform == "darwin"):
            os.system("clear")
        elif ( sys.platform == "win32" ):
            os.system("cls")

    def listen(self):
        textIgnore = {
            None, '!', '@', '#',
            '$', '%', '¨', '&', '*',
            '(', ')', '_', '-', '=',
            '+', '[', ']', '{', '}',
            ',', '.', '<', '>', ';',
            ':', '/', '?', '°', '®'
        }

        cap = self.recognize.capture()
        if not ( cap in textIgnore ):
            return cap
            

    def speak(self, text):
        timeNow = datetime.now()
        time = timeNow.strftime("%H:%M:%S")
        print(f"[{time}] ASH >> {text}")
        self.speaker.say(text)


ash = Assistant()
ash.speak("INICIANDO...")
time.sleep(3)
ash.speak("CARREGANDO MODELO DE RECONHECIMENTO DE VOZ")
time.sleep(3)
ash.speak("OLÁ MESTRE")

print("OUVINDO...")
while True:
    captureResult = ash.listen()    
    if ( captureResult ):
        ash.speak(captureResult)
        print("OUVINDO...")

sys.exit(1)