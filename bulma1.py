import speech_recognition as sr
import os
import time

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for background noise...")
    r.adjust_for_ambient_noise(source, duration=1)
    
    print("Say your command bro")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    command=text.lower().strip()
    print("You said:", text)
    if command=="open chrome":
        os.system("start chrome")
        #time.sleep(2)
    elif command=="play song":
        song="https://youtu.be/2qCpY38ompo?si=x6ohrUOnLJiY03SV"
        os.system(f"start {song}")
    else:
        print("enna la neenga sonna app pa kandu pudika mudiyala")
except sr.UnknownValueError:
    print("Sorry da, un voice puriyala.")

except sr.RequestError:
    print("Network problem da.")
#input("\nPress Enter in this window to exit the script...")
