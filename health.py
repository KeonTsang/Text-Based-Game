# Import modules.
import sys
from colorama import Fore, Style
import math

import player


# Prints the 'INSERT NAME HERE' bar. Takes the following arguments:
def health_bar_init(it, prefix="", size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / player.max_health)
        if j < (player.max_health * 0.2):
            colour = Fore.RED
        elif j < (player.max_health * 0.4):
            colour = Fore.YELLOW
        else:
            colour = Fore.GREEN
        print(colour + "{}[{}{}] {}/{}".format(prefix, "#" * x, " " * (size - x), j, player.max_health),
              end='\r', file=out, flush=True)

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print(flush=False, file=out)
    print(Style.RESET_ALL, flush=False, file=out)


def genHealthBar(health):
    healthBar = (Fore.GREEN if health > (player.max_health * 0.4) else Fore.YELLOW if health > (player.max_health * 0.2) else Fore.RED) + "Your Health: ["
    for i in range(0, math.floor(player.max_health / 2) + 1):
        healthBar += " " if i == 0 and health == 0 else "#" if i <= math.floor(health / 2) else " "
    healthBar += f"] {math.floor(health)}/{player.max_health}" + Fore.RESET
    return healthBar
