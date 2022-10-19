#Import modules.
import sys, time, os
import music as music
from colorama import Fore, Style

title = """
  ██████▓██   ██▓ ███▄ ▄███▓ ▄▄▄▄    ██▓ ▒█████    ██████  ██▓  ██████ 
▒██    ▒ ▒██  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒▒██▒  ██▒▒██    ▒ ▓██▒▒██    ▒ 
░ ▓██▄    ▒██ ██░▓██    ▓██░▒██▒ ▄██▒██▒▒██░  ██▒░ ▓██▄   ▒██▒░ ▓██▄   
  ▒   ██▒ ░ ▐██▓░▒██    ▒██ ▒██░█▀  ░██░▒██   ██░  ▒   ██▒░██░  ▒   ██▒
▒██████▒▒ ░ ██▒▓░▒██▒   ░██▒░▓█  ▀█▓░██░░ ████▓▒░▒██████▒▒░██░▒██████▒▒
▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░▓██ ░▒░ ░  ░      ░▒░▒   ░  ▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
░  ░  ░  ▒ ▒ ░░  ░      ░    ░    ░  ▒ ░░ ░ ░ ▒  ░  ░  ░   ▒ ░░  ░  ░  
      ░  ░ ░            ░    ░       ░      ░ ░        ░   ░        ░  
         ░ ░                      ░                                                                                                                                                   
  """

text_under_title = """
Confused, you awake from a slumber.

Your name is unknown to you, but you know that you are someone of importance.

You find yourself in a room, with no memory of how you got there.

The gentle ring of a PA chimes:

"Test subject #1, please report to the testing area."

You have no choice but to follow the instructions.
"""

scrambled_title = """
  ██████▓██   ██▓ ███▄ ▄███▓ ▄▄▄▄    ██▓ ▒█████    ██████  ██▓   ██████ 
▒█   ▒ ▒██  ██▒▓██▒▀█▀██▒▓█████▄ ▓██▒▒██▒  ██▒▒██   ▒ ▓██▒▒██    ▒ 
░ ▓█▄    ▒██ ██░▓██    ▓██░▒██▒ ▄██▒██▒▒██░  ██▒░ ▓██▄   ▒██▒░ ▓██▄   
  ▒ ██▒ ▐██▓░▒██    ▒██ ▒██░█▀  ░██░▒██   ██░  ▒   ██▒░██░  ▒    ██▒
▒██████▒▒ ░ ██▒▓░▒██▒   ░██▒░▓█ ▀█▓░██░░ ████▓▒░▒██████▒▒░██░▒██████▒▒
▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░▓██ ░▒░ ░  ░     ░▒░▒   ░  ▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
░  ░  ░  ▒ ▒ ░░  ░      ░    ░    ░  ▒ ░░ ░ ░  ▒  ░  ░  ░   ▒ ░░  ░   ░  
      ░  ░ ░            ░    ░       ░      ░ ░        ░   ░        ░  
         ░ ░                      ░                                     
"""

def print_title():

    #Plays the title screen music.
    music.play_title_screen_music()

    #Clears screen in prep for the title screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    #Prints the title screen.
    for char in title:
        sys.stdout.write(Fore.YELLOW + char)
        sys.stdout.flush()
        time.sleep(0.0001)
    print(Style.RESET_ALL)

    #Prints the text under the title.
    for char in text_under_title:
        sys.stdout.write(Fore.LIGHTBLUE_EX + char)
        sys.stdout.flush()
        time.sleep(0.0001)
    print(Style.RESET_ALL)

    #Prints the "Press any key to continue..." text.  
    input("Press ENTER to continue...")
    
    #Re-prints the title screen.
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + scrambled_title + Style.RESET_ALL)
    print(Fore.YELLOW + text_under_title)
    print(Fore.RED + Style.DIM + "Please wait..." + Style.RESET_ALL)

    #Plays confirming sound after ENTER is pressed and removed.
    music.play_click_music()
    time.sleep(2)

    #Clears screen in prep for the game.
    os.system('cls' if os.name == 'nt' else 'clear')

    
  


    

    

        
