from playsound import playsound
import eel

@eel.expose
def playStartsSound():
    playsound("webUI\\assets\\audio\\start_sound.mp3")
