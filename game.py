import time
from colorama import Fore

import title_screen as ts
import music as music
import health as health

ts.print_title()

music.play_main_game_music()

for i in health.health_bar_init(range(100), "Health: ", 40, Fore.GREEN):
    time.sleep(0.01)

for i in health.health_bar_init(range(100), "Sanity: ", 40, Fore.YELLOW):
    time.sleep(0.01)

print()
input("Game is still in development." + Fore.BLUE + " Please check back later! " + Fore.RESET)