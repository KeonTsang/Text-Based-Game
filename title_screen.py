#Import modules.
import sys, time, os
import music as music
from colorama import Fore, Style

title = """
  ██████    ▓██   ██▓    ███▄ ▄███▓    ▄▄▄▄       ██▓    ▒█████       ██████     ██▓     ██████ 
▒██    ▒     ▒██  ██▒   ▓██▒▀█▀ ██▒   ▓█████▄    ▓██▒   ▒██▒  ██▒   ▒██    ▒    ▓██▒   ▒██    ▒ 
░ ▓██▄        ▒██ ██░   ▓██    ▓██░   ▒██▒ ▄██   ▒██▒   ▒██░  ██▒   ░ ▓██▄      ▒██▒   ░ ▓██▄   
  ▒   ██▒     ░ ▐██▓░   ▒██    ▒██    ▒██░█▀     ░██░   ▒██   ██░     ▒   ██▒   ░██░     ▒   ██▒
▒██████▒▒     ░ ██▒▓░   ▒██▒   ░██▒   ░▓█  ▀█▓   ░██░   ░ ████▓▒░   ▒██████▒▒   ░██░   ▒██████▒▒
▒ ▒▓▒ ▒ ░      ██▒▒▒    ░ ▒░   ░  ░   ░▒▓███▀▒   ░▓     ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░   ░▓     ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░    ▓██ ░▒░    ░  ░      ░   ▒░▒   ░     ▒ ░     ░ ▒ ▒░    ░ ░▒  ░ ░    ▒ ░   ░ ░▒  ░ ░
░  ░  ░      ▒ ▒ ░░     ░      ░       ░    ░     ▒ ░   ░ ░ ░ ▒     ░  ░  ░      ▒ ░   ░  ░  ░  
      ░      ░ ░               ░       ░          ░         ░ ░           ░      ░           ░  
             ░ ░                            ░                                                                                                                                                            
  """

text_under_title = """
Confused, you awake from a slumber, bruised and battered.

Your name is unknown to you, but you know that you are someone of importance.


You find yourself in a room, with an odd sense of familiarity.


The gentle ring of a PA system chimes:

"Good morning sir, at your service."


The PA system chimes once more - it's a slogan:

"A helping hand - for a better tomorrow."

"""

scrambled_title = """
  ██████▓██   ██▓ ███▄ ▄███▓    ▄▄▄▄      ██▓   ▒█████    ██████  ██▓   ██████ 
▒█   ▒ ▒██  ██▒▓██▒▀█▀██▒▓██ ███▄   ▓██▒▒██   ▒  ██▒▒██   ▒ ▓██▒▒██    ▒ 
░ ▓█▄    ▒██ ██░▓██    ▓██  ░▒██▒   ▄██▒██▒▒█  █░  ██▒░  ▓██▄   ▒██▒░ ▓██▄   
  ▒ ██▒ ▐██▓░▒██    ▒██ ▒█ █░█▀   ░ ██░▒██    ██░  ▒    ██▒░██░  ▒    ██▒
▒██████▒▒ ░ ██▒▓░▒██▒   ░█ █▒░▓█ ▀█▓░██░░ ████▓▒░ ▒██████▒▒░██░▒██████▒▒
▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░▓██ ░▒░ ░  ░     ░▒░▒   ░  ▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
░  ░  ░  ▒ ▒ ░░  ░      ░    ░    ░  ▒ ░░ ░ ░  ▒  ░  ░  ░   ▒ ░░  ░   ░  
      ░  ░ ░            ░    ░       ░      ░ ░        ░   ░        ░  
         ░ ░                      ░                                     
"""

text_under_title_2 = f"""
{Fore.LIGHTBLUE_EX}Confused, you awake from a slumber, bruised and battered.
                                                 {Fore.BLACK}why am i important? ➘ {Fore.LIGHTBLUE_EX}
Your name is unknown to you, but you know that you are someone of importance.


You find yourself in a room, with an odd sense of familiarity.
                            {Fore.BLACK}have i been here before? ➚ {Fore.LIGHTBLUE_EX}

The gentle ring of a PA system chimes:

"Good morning sir, at your service."
    {Fore.BLACK}⬆ who am i? {Fore.LIGHTBLUE_EX}

The PA system chimes a slogan:

"A helping hand - for a better tomorrow."


You have no choice but to follow the instructions.{Style.RESET_ALL}
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
    print(text_under_title_2)
    print(Fore.WHITE + Style.BRIGHT + "Loading... " + Style.RESET_ALL)

    #Plays confirming sound after ENTER is pressed and removed.
    music.play_click_music()
    time.sleep(3)

    #Clears screen in prep for the game.
    os.system('cls' if os.name == 'nt' else 'clear')

    
  


    

    

        
