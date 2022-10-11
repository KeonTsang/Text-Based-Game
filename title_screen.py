import sys, time, os
import music as music
from colorama import Fore, Style

title = """
   ___   _   __  __ ___   _  _   _   __  __ ___   _  _ ___ ___ ___ 
  / __| /_\ |  \/  | __| | \| | /_\ |  \/  | __| | || | __| _ \ __|
 | (_ |/ _ \| |\/| | _|  | .` |/ _ \| |\/| | _|  | __ | _||   / _| 
  \___/_/ \_\_|  |_|___| |_|\_/_/ \_\_|  |_|___| |_||_|___|_|_\___|                                               
    """

text_under_title = """
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat.
  
  Duis aute irure dolor in reprehenderit in voluptate velit esse 
  cillum dolore eu fugiat nulla pariatur...
  
  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
  deserunt mollit anim id est laborum!"
"""

def print_title():

    #Plays the title screen music.
    music.play_title_screen_music()

    #Clears screen in prep for the title screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    #Prints the title screen.
    for char in title:
        sys.stdout.write(Fore.RED + char)
        sys.stdout.flush()
        time.sleep(0.01)
    print(Style.RESET_ALL)

    #Prints the text under the title.
    for char in text_under_title:
        sys.stdout.write(Fore.YELLOW + char)
        sys.stdout.flush()
        time.sleep(0.01)
    print(Style.RESET_ALL)

    #Prints the "Press any key to continue..." text.  
    for char in input("Press ENTER to continue..."):
        sys.stdout.write(Fore.WHITE + char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Style.RESET_ALL)

    #Plays confirming sound after ENTER is pressed.
    music.play_click_music()
    time.sleep(1)
    
    #Clears screen in prep for the game.
    os.system('cls' if os.name == 'nt' else 'clear')

    
  


    

    

        
