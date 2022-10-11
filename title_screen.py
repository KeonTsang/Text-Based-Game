import sys, time, os
from colorama import Fore, Style


title = """
   ___   _   __  __ ___   _  _   _   __  __ ___   _  _ ___ ___ ___ 
  / __| /_\ |  \/  | __| | \| | /_\ |  \/  | __| | || | __| _ \ __|
 | (_ |/ _ \| |\/| | _|  | .` |/ _ \| |\/| | _|  | __ | _||   / _| 
  \___/_/ \_\_|  |_|___| |_|\_/_/ \_\_|  |_|___| |_||_|___|_|_\___|                                               
    """

text_under_title = """
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
"""

def print_title():
    
    #Clears screen in prep for the title screen.
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,2):
        print()

    #Prints the title screen.
    for char in title:
        sys.stdout.write(Fore.RED + char)
        sys.stdout.flush()
        time.sleep(0.0001)
    print(Style.RESET_ALL)

    #Prints the text under the title.
    for char in text_under_title:
        sys.stdout.write(Fore.YELLOW + char)
        sys.stdout.flush()
        time.sleep(0.0001)
    print(Style.RESET_ALL)

    #Prints the "Press any key to continue..." text.  
    for char in input("Press ENTER to continue..."):
        sys.stdout.write(Fore.WHITE + char)
        sys.stdout.flush()
        time.sleep(0.0000000001)
    print(Style.RESET_ALL)
    print()
    

    

        
