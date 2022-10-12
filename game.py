#Import modules / files.
import time
from colorama import Fore
import title_screen as ts
import music as music
import health as health

#Prints the title screen and plays the title screen music.
ts.print_title()

#Plays the main game music.
music.play_main_game_music()

#Prints the health bar.
for i in health.health_bar_init(range(100), "Health: ", 40, Fore.GREEN):
    time.sleep(0.01)

#Prints the sanity bar.
for i in health.health_bar_init(range(50), "Sanity: ", 40, Fore.YELLOW):
    time.sleep(0.01)

#Displays the "Still in development" message. 
print()
input("Game is still in development!" + Fore.BLUE + " Please check back later! " + Fore.RESET)