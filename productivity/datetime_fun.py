from datetime import datetime

#GET TIME
def get_time():
    t = datetime.now()
    formated_time = f"{t:%I:%M %p}"
    
    #hour
    hour = t.hour

    # if formated_time
    if hour < 12 :
        return f"Good Morning Sir, the time is {formated_time}"
    elif 12 < hour <= 18 :
        return f"Good Afternoon {formated_time}"
    else :
        return f"Good Night Sir, the time is {formated_time}"

#GET_DATE

def get_date():
    pass
#     date = datetime.date()
#     print(date)

# get_date()