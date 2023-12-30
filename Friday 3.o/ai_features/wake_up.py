def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        # 'Hello Friday'
        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass

    return False
