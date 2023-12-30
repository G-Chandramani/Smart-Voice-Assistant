import os
from gtts import gTTS
from playsound import playsound

num = 1


def gspeak(audio):
    global num
    num += 1
    print(" ", audio)
    tts = gTTS(text=audio, lang='en', slow=False)
    file = str(num) + ".mp3"
    tts.save(file)
    playsound(file, True)
    os.remove(file)
