import google
from ai_features.speech_engine import gspeak


def google_search_result(query):
    search_result = google.search(query)

    for result in search_result:
        print(result.description.replace('...', '').rsplit('.', 3)[0])
        if result.description != '':
            gspeak(result.description.replace('...', '').rsplit('.', 3)[0])
            break


def is_valid_google_search(google_searches_dict, phrase):
    for key, value in google_searches_dict.items():
        try:
            if value == phrase.split(' ')[0]:
                return True

            elif key == phrase.split(' '):
                return True
        except IndexError:
            pass
    return False
