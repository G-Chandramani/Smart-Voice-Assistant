import random
import speech_recognition as sr
from playsound import playsound


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def invoke_mic():
    voice_text = ''

    global error_occurrence

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            # listen for 1 seconds and create the ambient noise energy level
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 2000
            r.dynamic_energy_threshold = False  # depends on adjust_for_ambient_noise
            r.dynamic_energy_adjustment_damping = 0.15  # depends on dynamic_energy_threshold
            # r.dynamic_energy_ratio = 1.5  # depends on dynamic_energy_threshold
            r.pause_threshold = 0.5

            print('Listening...')
            audio = r.listen(source=source)
            print('Recognizing...')
            voice_text = r.recognize_google(audio, language='en-in')
    except sr.UnknownValueError:
        pass
        # if error_occurrence == 0:
        #     play_sound(mp3_listening_problem_list)
        #     error_occurrence += 1
        # elif error_occurrence == 1:
        #     play_sound(mp3_struggling_list)
        #     error_occurrence += 1

    except sr.RequestError as e:
        print('Network error.')
    except sr.WaitTimeoutError:
        pass
        # if error_occurrence == 0:
        #     play_sound(mp3_listening_problem_list)
        #     error_occurrence += 1
        # elif error_occurrence == 1:
        #     play_sound(mp3_struggling_list)
        #     error_occurrence += 1

    return voice_text


def mic():
    voice_text = ''

    global error_occurrence

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            # listen for 1 seconds and create the ambient noise energy level
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 2000
            r.dynamic_energy_threshold = False  # depends on adjust_for_ambient_noise
            r.dynamic_energy_adjustment_damping = 0.15  # depends on dynamic_energy_threshold
            # r.dynamic_energy_ratio = 1.5  # depends on dynamic_energy_threshold
            r.pause_threshold = 0.5

            print('Listening...')
            audio = r.listen(source=source)
            print('Recognizing...')
            voice_text = r.recognize_google(audio, language='en-in')
    except sr.UnknownValueError:
        pass
        # if error_occurrence == 0:
        #     play_sound(mp3_listening_problem_list)
        #     error_occurrence += 1
        # elif error_occurrence == 1:
        #     play_sound(mp3_struggling_list)
        #     error_occurrence += 1

    except sr.RequestError as e:
        print('Network error.')
    except sr.WaitTimeoutError:
        pass
        # if error_occurrence == 0:
        #     play_sound(mp3_listening_problem_list)
        #     error_occurrence += 1
        # elif error_occurrence == 1:
        #     play_sound(mp3_struggling_list)
        #     error_occurrence += 1

    return voice_text