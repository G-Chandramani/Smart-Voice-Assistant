def trans(trans_dict, voice_note):
    for key, value in trans_dict.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' '):
                return True

        except IndexError:
            pass
    return False