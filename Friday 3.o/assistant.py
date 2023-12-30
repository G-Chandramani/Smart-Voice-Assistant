import ctypes
import os
import smtplib
import subprocess
import time
import webbrowser
import pyjokes
import wikipedia
import winshell as winshell
from playsound import playsound
from ai_features import wake_up
from googletrans import Translator
from ai_features import translators
from ai_features import google_search
from ai_features import mp3_player
import nltk
from nltk.stem import WordNetLemmatizer
from ai_features import mic
from ai_features import speech_engine

lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model

model = load_model('chatbot_model.h5')
import json
import random
import train_chatbot

mp3_dir = 'response_list/'
invoke = [mp3_dir + 'invoke.mp3']
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which'}
browse_dict = {'search': 'search', 'google': 'google', 'browse': 'browse'}
trans_dict = {'translate': 'translate'}
greeting_dict = {'friday': 'friday'}
mp3_thank_you_list = [mp3_dir + 'my pleasure.mp3', mp3_dir + 'ur welcome.mp3']
mp3_network_problem = {mp3_dir + 'network1.mp3', mp3_dir + 'network2.mp3'}
mp3_listening_problem_list = [mp3_dir + 'problem.mp3', mp3_dir + 'problem2.mp3']
mp3_struggling_list = [mp3_dir + 'struggling_1.mp3']
mp3_google_search = [mp3_dir + 'i found something for u.mp3', mp3_dir + 'got it.mp3', mp3_dir + 'web_search.mp3']
mp3_greeting_list = [mp3_dir + 'greeting.mp3', mp3_dir + 'greeting2.mp3']
mp3_open_launch_list = [mp3_dir + 'ok.mp3', mp3_dir + 'launching.mp3', mp3_dir + 'sure.mp3']

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


# TensorFlow
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def send():
    msg = data

    if msg != '':
        res = chatbot_response(msg)
        speech_engine.gspeak(res)


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    playsound(mp3_dir + 'Initializing.mp3')
    time.sleep(2)
    playsound(mp3_dir + 'launching (2).mp3')
    time.sleep(2)
    # sub = subprocess.Popen("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
    os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
    speech_engine.gspeak("Hey I am your personal assistant, how can I help you.")

    while True:
        try:
            res = mic.invoke_mic().lower()
            if wake_up.is_valid_note(greeting_dict, res):
                print('Hey...')
                play_sound(invoke)

                while True:
                    data = mic.mic().lower()
                    translator = Translator()
                    print('Key is : ' + data)
                    translated = translator.translate(data, dest='en')
                    trans_text = translated.text
                    print(trans_text)

                    if translators.trans(trans_dict, trans_text):
                        translator = Translator()
                        key = data.replace('translate ', ' ')
                        print('Key is : ' + key)
                        lang_input = translator.detect(key)
                        print(lang_input)
                        speech_engine.gspeak('In which language do you want to translate: ')
                        lang_output = mic.mic().lower()
                        translated = translator.translate(key, dest=lang_output)
                        trans_text = translated.text
                        speech_engine.gspeak(trans_text)
                        continue

                    elif 'good morning' in trans_text:
                        translator = Translator()
                        translated = translator.translate(trans_text, dest='en')
                        trans_text = translated.text
                        speech_engine.gspeak(trans_text)
                        continue

                    elif 'good afternoon' in trans_text:
                        translator = Translator()
                        translated = translator.translate(trans_text, dest='en')
                        trans_text = translated.text
                        speech_engine.gspeak(trans_text)
                        continue

                    elif 'good evening' in trans_text:
                        translator = Translator()
                        translated = translator.translate(trans_text, dest='en')
                        trans_text = translated.text
                        speech_engine.gspeak(trans_text)
                        continue

                    elif 'good night' in trans_text:
                        translator = Translator()
                        translated = translator.translate(trans_text, dest='en')
                        trans_text = translated.text
                        speech_engine.gspeak(trans_text)
                        continue

                    elif google_search.is_valid_google_search(browse_dict, data):
                        playsound(mp3_dir + 'let me search for u.mp3')
                        webbrowser.open('https://www.google.co.in/search?q={}'.format(data))
                        continue

                    elif 'wikipedia' in data:
                        speech_engine.gspeak('Searching in Wikipedia...')
                        query = data.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speech_engine.gspeak("According to Wikipedia")
                        print(results)
                        speech_engine.gspeak(results)
                        continue

                    elif 'joke' in data:
                        joke = pyjokes.get_joke()
                        print(joke)
                        speech_engine.gspeak(joke)
                        playsound(mp3_dir + 'funny-Laugh.mp3')
                        continue

                    elif 'send a mail' in trans_text:
                        try:
                            # Mailing info
                            s = smtplib.SMTP('smtp.gmail.com', 587)
                            s.starttls()
                            s.login("gajbharechandramani@gmail.com", "wdsvidypfamcqdpm")
                            speech_engine.gspeak("What should I say?")
                            content = data.lower()
                            speech_engine.gspeak("whom should i send?")
                            speech_engine.gspeak("please enter the correct email address in the screen")
                            to = input("Enter sender email hear:")
                            s.sendmail("gajbharechandramani@gmail.com", to, content)
                            s.quit()
                            speech_engine.gspeak("Email has been sent !")
                        except Exception as e:
                            print(e)
                            speech_engine.gspeak("I am not able to send this email")
                        continue

                    elif 'lock' in data:
                        speech_engine.gspeak('Sure sir')
                        for value in ['pc', 'system', 'windows']:
                            ctypes.windll.user32.LockWorkStation()
                        speech_engine.gspeak('Your system is locked.')
                        os._exit(0)

                    elif 'shutdown system' in data:
                        speech_engine.gspeak("Hold On a Sec ! Your system is on its way to shut down")
                        subprocess.call('shutdown / p /f')
                        os._exit(0)

                    elif 'empty recycle bin' in trans_text:
                        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                        speech_engine.gspeak("Recycle Bin Recycled")
                        continue

                    elif 'music' in data:
                        while True:
                            try:
                                event, values = mp3_player.window.Read()
                                if event is None or event == 'Exit':
                                    break

                                elif event == "Load":
                                    list_of_files = mp3_player.get_list_of_files(values['_foldernm_'])

                                    att = mp3_player.get_music_attributes(list_of_files)

                                    data1 = []
                                    for key, value in att.items():
                                        data1.append(
                                            [key, value["Album"], value["Title"], value["Duration"], value["Artist"],
                                             value["Year"]])
                                    mp3_player.window.FindElement('_table_').Update(values=data1)

                                elif event == '_playbut_':
                                    v_pause = False
                                    indexarr = values['_table_']
                                    legthofsong = len(indexarr)
                                    if (legthofsong == 0):
                                        print('please make a selection')
                                        mp3_player.sg.Popup('Hello ,',
                                                            'please make a selection before click the play button')
                                    else:
                                        indexsong = indexarr[0]
                                        mp3_player.pygame.mixer.init()
                                        mp3_player.pygame.mixer.music.load((att[indexsong])["Path"])
                                        mp3_player.pygame.mixer.music.play()

                                elif event == '_stop_':
                                    mp3_player.pygame.mixer.music.stop()
                                    break

                                print(event, values)
                            except Exception as e:
                                print(e)
                        mp3_player.window.Close()

                    else:
                        send()
                        continue
            else:
                continue

        except Exception as e:
            print(e)
            continue
