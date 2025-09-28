import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)
        self.engine.setProperty("voice", 'pt')
    
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == '__main__':
    s = Speaker()
    s.say("Olá")