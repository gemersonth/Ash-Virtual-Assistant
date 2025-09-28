import sys
from vosk import Model, KaldiRecognizer
import pyaudio
import os
import json

PATH = "vosk_model_br"

class Recognize():
    def __init__(self):
        # Verificar se a pasta 'pacote-br' existe
        if not os.path.exists(PATH):
            raise FileNotFoundError("ARQUIVO 'model_br' NÃO ENCONTRADO")
            print("NÃO FOI POSSÍVEL ENCONTRAR: model_br")
            sys.exit(1)
        
        # Carregar o modelo em pt-BR
        self.model = Model(PATH)
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
      
    
    def capture(self):
        self.rec.pause_threshold = 2
        self.data = self.stream.read(40000, exception_on_overflow=False)
        self.rec.AcceptWaveform(self.data)
        try:
            result = self.rec.Result()
            readJson = json.loads(result)
            text = readJson["text"]
        except:
            return None
        return text
            
            
if __name__ == '__main__':
    r = Recognize()
    while True:
        I = r.capture().lower()
        print(I)