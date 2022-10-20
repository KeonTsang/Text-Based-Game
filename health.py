#Import modules.
import sys
from colorama import Fore, Style
 
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



health_bar_100 = Fore.GREEN + "Health: [##################################################] 100/100" + Fore.RESET
health_bar_80 = "Health: [####################################              ] 80/100"
health_bar_60 = "Health: [############################                      ] 60/100"
health_bar_40 = "Health: [####################                              ] 40/100"
health_bar_20 = "Health: [########                                          ] 20/100"
