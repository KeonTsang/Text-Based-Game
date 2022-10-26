from colorama import Fore, Style, Back
import time, os, sys, math, random

import final_boss
import game_parser
import player
import health
import screens

finalBoss = False
current_health = 500
max_health = 500
name = "The Ooze"
phase = 1
skip_attack = False

boss_colour = Fore.LIGHTBLUE_EX

title = """
 _____                    _     _____         _   _              ______         _ _ _ _         
/  ___|                  | |   |_   _|       | | (_)             |  ___|       (_) (_) |        
\ `--.  ___  ___ _ __ ___| |_    | | ___  ___| |_ _ _ __   __ _  | |_ __ _  ___ _| |_| |_ _   _ 
 `--. \/ _ \/ __| '__/ _ \ __|   | |/ _ \/ __| __| | '_ \ / _` | |  _/ _` |/ __| | | | __| | | |
/\__/ /  __/ (__| | |  __/ |_    | |  __/\__ \ |_| | | | | (_| | | || (_| | (__| | | | |_| |_| |
\____/ \___|\___|_|  \___|\__|   \_/\___||___/\__|_|_| |_|\__, | \_| \__,_|\___|_|_|_|\__|\__, |
                                                           __/ |                           __/ |
                                                          |___/                           |___/ """
text1 = """
You continue down the lab, and find yourself inside a strange room.
The tall walls are dripping with a strange black goo, sort of like tar.
In the middle of the room is a shattered glass chamber hooked up to heavy machinery.
The container is filled with more of the black goo, above the chamber on a metal rim reads:
"""
text2 = "'Subject 001'"
text3 = """
On the other side of the room you see a fire door!
A means of escape!
You make a bolt for it but suddenly the facility begins rumbling.
Something grabs your leg and you turn around to see what it is.
A tentacle of black ooze pulls you back . . . . .
"""

lose = """
You black out onto the floor, swallowed by the ooze....
                                                        
                                                        
Confused, you awake from a slumber, bruised and battered.
Your name is unknown to you, but you know that you are someone of importance.
You find yourself in a room, with an odd sense of familiarity.

The gentle ring of a PA system chimes:
"Good morning sir, at your service."

The PA system chimes once more - it's a slogan:
"A helping hand - for a better tomorrow."
"""

the_end = """
▄▄▄█████▓  ██░ ██  ▓█████    ▓█████   ███▄    █  ▓█████▄ 
▓  ██▒ ▓▒ ▓██░ ██▒ ▓█   ▀    ▓█   ▀   ██ ▀█   █  ▒██▀ ██▌
▒ ▓██░ ▒░ ▒██▀▀██░ ▒███      ▒███    ▓██  ▀█ ██▒ ░██   █▌
░ ▓██▓ ░  ░▓█ ░██  ▒▓█  ▄    ▒▓█  ▄  ▓██▒  ▐▌██▒ ░▓█▄   ▌
  ▒██▒ ░  ░▓█▒░██▓ ░▒████▒   ░▒████▒ ▒██░   ▓██░ ░▒████▓ 
  ▒ ░░     ▒ ░░▒░▒ ░░ ▒░ ░   ░░ ▒░ ░ ▓ ▒░   ▒ ▒   ▒▒▓  ▒ 
    ░      ▒ ░▒░ ░  ░ ░  ░    ░ ░  ░ ░ ░░   ░ ▒░  ░ ▒  ▒ 
  ░        ░  ░░ ░    ░         ░      ░   ░ ░   ░ ░  ░ 
           ░  ░  ░    ░  ░      ░   ░         ░     ░    
                                               ░      
"""

the_end_question = """
▄▄▄█████ ▓ ██░ ██  ▓█████    ▓█████   ███▄    █  ▓█████▄   ▄████████▓ 
▓  ██▒ ▓ ▒▓██░ ██▒ ▓█   ▀    ▓█   ▀   ██ ▀█   █  ▒██▀ ██▌ ░▓▀▓░  ░▓██░
▒ ▓██░ ▒ ░▒██▀▀██░ ▒███      ▒███    ▓██  ▀█ ██▒ ░██   █▌   ░ ▄████▓▒░
░ ▓██▓ ░  ░▓█ ░██  ▒▓█  ▄    ▒▓█  ▄  ▓██▒  ▐▌██▒ ░▓█▄   ▌    ░▓▓░   ░
  ▒██▒ ░  ░▓█▒░██▓ ░▒████▒   ░▒████▒ ▒██░   ▓██░ ░▒████▓    ░▓██░░
  ▒ ░░     ▒ ░░▒░▒ ░░ ▒░ ░   ░░ ▒░ ░ ▓ ▒░   ▒ ▒   ▒▒▓  ▒    ▒░░▓░▒
    ░      ▒ ░▒░ ░  ░ ░  ░    ░ ░  ░ ░ ░░   ░ ▒░  ░ ▒  ▒    ░  ▒  ░
  ░        ░  ░░ ░    ░         ░       ░   ░ ░   ░ ░  ░   ░  ░   ░
           ░  ░  ░    ░  ░      ░  ░          ░     ░          ░
                                              ░      
"""

picture = """                         
                   ____________________        
                  |                    |        
                  |____________________|        
                   |                  |         
                   |\_              __|         
                   | |              \ |         
                   | |              | |         
                   | \             /  |         
                   | |#############|  |         
                   |  \__#######__/   |         
                   |     |########|   |         
                   |    /#########|   |         
    _______________|   /###########\  |_______________ 
       ############|  |############|  |##############   
    ###############|__|# \ ##### / |__|#################  
  ###################### O ##### O #######################  
   ########################################################  
     ################### \-------/ ########################  
    #################### \-^---^-/ ###################   
        ###############################################   
            #####################################     
"""

description = f"\n{name}, a strange black goo, has attacked you!\n" +\
              name + ": " + boss_colour + f"'I am {name} and now you will meet your demise!'" + Fore.RESET +\
              picture

def type_text(text, colour, speed=0.0001):
    for char in text:
        sys.stdout.write(colour + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Style.RESET_ALL)


def display_health(inverse):
    colour1 = Fore.RED if inverse else Fore.GREEN
    colour2 = Fore.MAGENTA if inverse else Fore.YELLOW
    colour3 = Fore.BLUE if inverse else Fore.RED
    health_bar = (colour1 if current_health > (max_health * 0.4) else colour2 if current_health > (
            max_health * 0.2) else colour3) + f"{name}'s Health: ["
    for i in range(0, (math.floor(max_health / 2) + 1)):
        health_bar += " " if i == 0 and health == 0 else "#" if i <= math.floor(current_health / 2) else " "
    health_bar += f"] {current_health}/{max_health}" + Fore.RESET
    print(health_bar)


def command_reader():
    notValidCommand = True
    while notValidCommand:
        command = input(Fore.RED + "\n(!)" + Fore.RESET + f" ATTACK {name}\n" +
                        Fore.CYAN + "(?)" + Fore.RESET + f" TALK to {name}\n" +
                        Fore.YELLOW + "(*)" + Fore.RESET + f" use an ACTION on {name}\n" +
                        Fore.GREEN + "(~)" + Fore.RESET + f" SPARE {name}\n\n")
        notValidCommand = execute_command(game_parser.normalise_input(command))


def execute_spare():
    print("You cannot spare " + name + "! It is in a rage!")


def execute_talk():
    print("You tell the ooze it looks beautiful!")
    print(name + ": " + boss_colour + "'Die scum!'" + Fore.RESET)


def execute_attack(boss_phase):
    weapon = player.current_weapon
    damage = weapon.attack()

    if final_boss.current_health <= damage:
        damage = final_boss.current_health - 1
    final_boss.current_health -= damage
    print(f"\nYou dealt {damage} to {name} using your {weapon.name}!")
    if final_boss.current_health == 1:
        print(f"{name}: " + boss_colour + "'YOU THOUGHT YOU COULD DEFEAT ME?!?!?!?! WELL WATCH THIS!'" + Fore.RESET)
        input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
        recover()
        final_boss.skip_attack = True
    else:
        if boss_phase % 2 == 0:
            print(f"{name}: " + boss_colour + "'HAHAHA you think you can hurt me puny human?!'" + Fore.RESET)
        else:
            print(f"{name}: " + boss_colour + "'HAHAHA what are you trying to accomplish?!'" + Fore.RESET)
        final_boss.phase = boss_phase + 1


def recover():
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_health()
    print(description)
    display_health(False)
    time.sleep(1)
    final_boss.current_health = final_boss.max_health

def attack():
    damage = math.floor(player.max_health * (random.randint(5, 15) / 100))
    if player.player_health <= damage:
        damage = player.player_health - 1
    player.player_health -= damage
    print(f"\n{name} struck you with black goo for {damage} hit points!")
    input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

def execute_action():
    print(f"You do a dance for {name}!")
    print(name + ": " + boss_colour + "'Die scum!'" + Fore.RESET)

def inverseSequence(sleep):
    print(Back.WHITE)
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_inverse_health()
    print(Fore.BLACK + picture + Fore.RESET)
    display_health(True)
    type_text("\nYou restored All your HP!", Fore.BLACK)
    player.player_health = player.max_health
    time.sleep(sleep)

    print(Back.WHITE)
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_inverse_health()
    print(Fore.BLACK + picture + Fore.RESET)
    display_health(True)
    type_text("\n" + final_boss.name + " dealt " + str(player.max_health - 1) + " damage to you!", Fore.BLACK)
    player.player_health = 1
    time.sleep(sleep)
    
def count_down_health(it, prefix="", size=50, max_hp=100, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size * j / max_hp)
        if j < (max_hp * 0.2):
            colour = Fore.RED
        elif j < (max_hp * 0.4):
            colour = Fore.YELLOW
        else:
            colour = Fore.GREEN
        print(colour + "{}[{}{}] {}/{}  ".format(prefix, "#" * x, " " * (size - x), j, max_hp),
              end='\r', file=out, flush=True)

    show(0)
    for i, item in enumerate(it):
        yield item
        show(count - i)
    print(flush=False, file=out)
    print(Style.RESET_ALL, flush=False, file=out)

def execute_command(command):
    if 0 == len(command):
        print("Sorry I didn't understand that!\n")
        input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
        return True
    if command[0] == "spare":
        execute_spare()
        return False
    elif command[0] == "talk":
        execute_talk()
        return False
    elif command[0] == "attack":
        execute_attack(phase)
        return False
    elif command[0] == "action":
        execute_action()
        return False
    else:
        print(f"'{command[0]}' -> Makes no sense.")
        input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
        return True

def initiate():
    # print(Back.RESET, Fore.RESET)
    # final_boss.finalBoss = True
    # os.system('cls' if os.name == 'nt' else 'clear')
    #
    # type_text(title, Fore.YELLOW, 0)
    # type_text(text1, Fore.CYAN)
    # type_text(text2, Fore.MAGENTA)
    # type_text(text3, Fore.CYAN)
    # input(boss_colour + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    #
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(screens.battle_screen_dim)
    # print(screens.there_are_enemies)
    # time.sleep(0.5)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(screens.battle_screen_bright)
    # print(screens.there_are_enemies)
    # time.sleep(0.5)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(screens.battle_screen_dim)
    # print(screens.there_are_enemies)
    # time.sleep(0.5)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(screens.battle_screen_bright)
    # print(screens.there_are_enemies)
    # time.sleep(0.5)
    #
    # os.system('cls' if os.name == 'nt' else 'clear')
    # for i in health.health_bar_init(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5), player.max_health):
    #     time.sleep(0.01)
    # os.system('cls' if os.name == 'nt' else 'clear')
    #
    # haveHp = True
    # while haveHp:
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     player.display_health()
    #     print(description)
    #     display_health(False)
    #     command_reader()
    #     if not final_boss.skip_attack:
    #         attack()
    #     else:
    #         final_boss.skip_attack = False
    #     if player.player_health == 1:
    #         haveHp = False
    #
    # final_boss.current_health = final_boss.max_health
    # print(picture + "\n" + name + boss_colour + "'You really thought you could beat me?'"
    #                                                   "\n'Let me show you just how far apart we both really are!'\n\n")
    # input(boss_colour + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    # print(Back.WHITE)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # final_boss.boss_colour = Fore.LIGHTYELLOW_EX
    # inverseSequence(1)
    # inverseSequence(0.5)
    # inverseSequence(0.3)
    # inverseSequence(0.2)
    # inverseSequence(0.1)
    # inverseSequence(0.05)
    # inverseSequence(0.05)
    print(Back.RESET)
    final_boss.boss_colour = Fore.LIGHTBLUE_EX
    player.player_health = player.max_health
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_health()
    print(picture)
    display_health(False)
    print("\n" + name + ": ")
    type_text("Now do you finally get it?, The difference between me and you?", boss_colour)
    time.sleep(1)
    type_text("\nIf still no well let me show you!", boss_colour)
    time.sleep(1)
    type_text("\nNOW DIE!!!!", boss_colour)
    input(Fore.LIGHTRED_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    os.system('cls' if os.name == 'nt' else 'clear')

    if player.karma < 5:
        for i in count_down_health(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5), player.max_health):
            time.sleep(0.01)
        player.player_health = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        player.display_health()
        type_text("\n\n\n\n\n\nMWAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA", Fore.LIGHTBLUE_EX)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        type_text(lose, Fore.CYAN)
        type_text(the_end_question, Fore.YELLOW)
        time.sleep(5)
        quit()
    else:
        pass

