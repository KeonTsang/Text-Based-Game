import sys
from colorama import Fore, Style
 
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
        print("\n", flush=False, file=out)
        print(Style.RESET_ALL, flush=False, file=out)


