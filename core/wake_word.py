#starting the system

def wake_word(command : str) -> bool : 
    if "hey jarvis" in command :
        print("work")
        return True
    return False 