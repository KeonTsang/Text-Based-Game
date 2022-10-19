#Import modules / files.
import time
from colorama import Fore
import title_screen as ts
import music as music
import health as health
import map as map
import os as os

#Prints the title screen and plays the title screen music.
ts.print_title()

#Plays the main game music.
music.play_main_game_music()

#Prints the health bar. Use 'health.health_bar_x' to change the health bar.
for i in health.health_bar_init(range(100), "Health: ", 50, Fore.GREEN):
    time.sleep(0.01)

#Flushes screen in preperation for the map & health bar.
os.system('cls' if os.name == 'nt' else 'clear')

#Prints the health bar.
print(health.health_bar_100)

#Prints the map.
print(map.map)



