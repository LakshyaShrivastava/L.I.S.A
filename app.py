# main app entrypoint
import os
import eel


from engine.speak import *
from engine.features import *   
from engine.commands import *

if __name__ == "__main__":
    eel.init("webUI")

    # playStartsSound()
    greet()
    
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)

