
from colorama import Fore, Style
import time, os, sys, math, random
import player
import health

finalBoss = False

title = """
 _____                    _     _____         _   _              ______         _ _ _ _         
/  ___|                  | |   |_   _|       | | (_)             |  ___|       (_) (_) |        
\ `--.  ___  ___ _ __ ___| |_    | | ___  ___| |_ _ _ __   __ _  | |_ __ _  ___ _| |_| |_ _   _ 
 `--. \/ _ \/ __| '__/ _ \ __|   | |/ _ \/ __| __| | '_ \ / _` | |  _/ _` |/ __| | | | __| | | |
/\__/ /  __/ (__| | |  __/ |_    | |  __/\__ \ |_| | | | | (_| | | || (_| | (__| | | | |_| |_| |
\____/ \___|\___|_|  \___|\__|   \_/\___||___/\__|_|_| |_|\__, | \_| \__,_|\___|_|_|_|\__|\__, |
                                                           __/ |                           __/ |
                                                          |___/                           |___/ 
"""
text1 = """
You continue down the lab, and find yourself inside a strange room.
The tall walls are dripping with a strange black goo, sort of like tar.
In the middle of the room is a shattered glass chamber hooked up to heavy machinery.
The container is filled with more of the black goo, above the chamber on a metal rim reads:

"""
text2 = "'Subject 001'"
text3 = """On the other side of the room you see a fire door!
A means of escape!
You make a bolt for it but suddenly the facility begins rumbling.
Something grabs your leg and you turn around to see what it is.
A tentacle of black ooze pulls you back . . . . .
"""

def type_text(text, colour, speed=0.0001):
    for char in text:
        sys.stdout.write(colour + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Style.RESET_ALL)

def initiate():
    finalBoss = True
    os.system('cls' if os.name == 'nt' else 'clear')

    type_text(title, Fore.YELLOW, 0.000001)
    type_text(text1, Fore.CYAN)
    type_text(text2, Fore.MAGENTA)
    type_text(text3, Fore.CYAN)


initiate()