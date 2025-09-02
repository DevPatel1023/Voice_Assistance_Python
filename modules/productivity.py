import os
from productivity.datetime_fun import get_date

NOTES_PATH = 'data/notes.json'

#add notes
def add_notes(note : str):
    #give path to store in notes and write
    with open(NOTES_PATH,"a",encoding='utf-8') as f:
        f.write(note +"\n")
    current_date = get_date()
    return f"{current_date:}Note added successfully"


#read notes
def read_notes():
    if not os.path.exists(NOTES_PATH):
        return "No Notes found"
    with open(NOTES_PATH,"r",encoding='utf-8') as f:
        return f.read().strip() or "No notes available"
    
#clear notes
def clear_notes():
    open(NOTES_PATH,"w").close()
    return "All notes clear"