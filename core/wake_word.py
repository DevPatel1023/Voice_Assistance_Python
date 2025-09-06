#starting the system

def wake_word(command : str) -> bool : 
    if "hey jarvis" in command :
        return True
    return False 