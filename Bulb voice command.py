from Speech_Bulb_Ctrl import *
from time import sleep
r = sr.Recognizer()
mic = sr.Microphone()
def main():
    while True:
        Speech = Recog(mic,r)
        if "BLINK" in Speech.upper():
            repSpeech()

        #On_Off(Speech)
        sleep(2)




#print(__name__)

if __name__ == "__main__":
    main()
