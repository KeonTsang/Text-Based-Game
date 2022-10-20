#Import modules.
import sys
from colorama import Fore, Style
import math
 
#Prints the 'INSERT NAME HERE' bar. Takes the following arguments:
def health_bar_init(it, prefix="", size=60, colour=Fore.WHITE, out=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            print(colour + "{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                    end='\r', file=out, flush=True)
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        print(flush=False, file=out)
        print(Style.RESET_ALL, flush=False, file=out)

def genHealthBar(health):
    healthBar = (Fore.GREEN if health > 40 else Fore.YELLOW if health > 20 else Fore.RED) + "Health: ["
    for i in range(0, 51):
        healthBar += " " if i == 0 and health == 0 else "#" if i <= math.floor(health / 2) else " "
    healthBar += f"] {health}/100" + Fore.RESET
    return healthBar

health_bar_100 = Fore.GREEN + "Health: [##################################################] 100/100" + Fore.RESET
health_bar_80 = "Health: [####################################              ] 80/100"
health_bar_60 = "Health: [############################                      ] 60/100"
health_bar_40 = "Health: [####################                              ] 40/100"
health_bar_20 = "Health: [########                                          ] 20/100"
