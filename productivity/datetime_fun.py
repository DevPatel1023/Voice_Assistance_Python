from datetime import datetime

def get_time():
    t = datetime.now()
    formated_time = f"{t:%I:%M %p}"
    # if formated_time
    return formated_time
    