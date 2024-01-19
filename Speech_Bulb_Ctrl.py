import time
import serial
import speech_recognition as sr
import re
r = sr.Recognizer()
mic = sr.Microphone()
integer = re.compile(r'\d(\d)?(\d)?') 

def Recog(mic,r):
    while True:    
        try:    
            print("######".center(20,"=")+"\n")
            print("On/Off/stop?/blink?")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                
            
            speech = r.recognize_google(audio)
            print("You said: ",speech)
            return speech
        except sr.exceptions.UnknownValueError:
            print("sorry didnt get that\n")

            continue

Led = serial.Serial('com3',9600)
time.sleep(1)

def repSpeech():

    while True:
        pass
        try:

            print("speak!\n")
            speech = Recog(mic,r)
            time.sleep(0.5)

            if "stop" in speech.lower():
                break

            String = speech.lower()  
            Storage = String.split()
            keyword1 = Storage.pop(Storage.index('blink'))

            if keyword1.lower() == "blink":
                mo = integer.search(String)
                Reps =int(mo.group()) #number of blinks
                counter = 0
                while(counter < Reps):
                    Led.write("ON".encode("utf-8"))
                    time.sleep(1)
                    Led.write("OFF".encode("utf-8"))
                    time.sleep(1)
                    counter+=1

                
                
                #print(keyword1)
                #print(keyword2)
                #Led.write(keyword1.encode("utf-8"))
                #time.sleep(1)
                #Led.write(int(keyword2.encode("utf-8")))

        
        except sr.RequestError:
            print("internet issues try again\n")
            continue
        except sr.UnknownValueError:
            print("uh- uh i didn't get that try again\n")    
            continue
        except ValueError:
            print("Don't take too long now, Speak!\n")
            continue
        except TypeError:
            print("(for the Dev) You messed up the code some where brudda(TypeError!) \n")
        except serial.SerialException:
            print("Setup your COM port or connect your arduino") 
            continue      

     




def On_Off(speech):

    pass

    try:
        On = speech
        time.sleep(1)
        if "stop" in On.lower():
            print("Exiting program...")
            time.sleep(0.5)
            Led.write("OFF".encode("utf-8"))
            time.sleep(0.5)
            print("Alright Done! Thanks!")
            exit()
            


        elif "ON" in On.upper():
            
            print("turning Bulb on...")
            time.sleep(0.5)
            Led.write("ON".encode("utf-8"))
            time.sleep(0.5)
            print("ON")

        elif "OFF" in On.upper():
            print("turning Bulb off...")
            time.sleep(0.5)
            Led.write("OFF".encode("utf-8"))
            time.sleep(0.5)
            print("OFF")
        
        
        
    except ValueError:
        print("Don't take too long now, Speak!\n")
    except TypeError:
        print("(for the Dev) You messed up the code some where brudda(TypeError!) \n")
    except serial.SerialException:
        print("Setup your COM port or connect your arduino") 