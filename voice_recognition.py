import sys
from vosk import Model, KaldiRecognizer
import pyaudio
import os
import json

class Recognize():
    def __init__(self):

        # Verificar se a pasta 'pacote-br' existe
        if not os.path.exists("model_br"):
            raise FileNotFoundError("ARQUIVO 'model_br' NÃO ENCONTRADO")
            print("NÃO FOI POSSÍVEL ENCONTRAR: model_br")
            sys.exit(1)
        
        # Ler e executa o modelo em pt-BR
        self.model = Model("model_br")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
      
    
    def ignore_arguments(self):
        arguments = ('', 'none', 'None', ' ', None,
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
        'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
        return arguments
    
    def capture(self):
        self.rec.pause_threshold = 2
        self.data = self.stream.read(40000)
        self.rec.AcceptWaveform(self.data)
        try:
            result = self.rec.Result()
            readJson = json.loads(result)
            text = readJson["text"]
        except:
            return None
        return text
    
    def run(self):
        ignore = self.ignore_arguments()
        while True:
            I = self.capture().lower()
            print(I)
                    
            
            
if __name__ == '__main__':
    a = Recognize()
    a.run()