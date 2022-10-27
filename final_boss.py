from colorama import Fore, Style, Back
import time, os, sys, math, random

import final_boss
import game_parser
import player
import health
from monsters import monster_init
import screens
import music as music

finalBoss = False
current_health = 500
max_health = 500
name = "The Ooze"
phase = 1
skip_attack = False
goodEnding = 0
trueEnding = False

#music.play_ending_music()

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

def type_text(text, colour, speed=0.01):
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
    if final_boss.goodEnding == 6:
        trigger_true_ending()
    else:
        print("You cannot spare " + name + "! It is in a rage!")

def execute_talk():
    print("You tell the ooze it looks beautiful!")
    print(name + ": " + boss_colour + "'Die scum!'" + Fore.RESET)


def execute_attack(boss_phase):
    if final_boss.goodEnding < 1:
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
    else:
        if final_boss.goodEnding == 1:
            help = monster_init.stephy
            damage = math.floor(final_boss.max_health * 0.10)
            print(help.colour + help.name + Fore.RESET + f" dealt {str(damage)} damage to {name}!")
            print(f"{name}: " + boss_colour + "'Hey! Watch it that hurts!'" + Fore.RESET)
            final_boss.current_health -= damage
            final_boss.goodEnding += 1
        elif final_boss.goodEnding == 2:
            help = monster_init.c3nti
            damage = math.floor(final_boss.max_health * 0.15)
            print(help.colour + help.name + Fore.RESET + f" dealt {str(damage)} damage to {name}!")
            print(f"{name}: " + boss_colour + "'What do you think you are doing!'" + Fore.RESET)
            final_boss.current_health -= damage
            final_boss.goodEnding += 1
        elif final_boss.goodEnding == 3:
            help = monster_init.sgtripper
            damage = math.floor(final_boss.max_health * 0.20)
            print(help.colour + help.name + Fore.RESET + f" dealt {str(damage)} damage to {name}!")
            print(f"{name}: " + boss_colour + "'AGGGGHHHHHHhhhhh how is this possible!'" + Fore.RESET)
            final_boss.current_health -= damage
            final_boss.goodEnding += 1
        elif final_boss.goodEnding == 4:
            help = monster_init.mrburns
            damage = math.floor(final_boss.max_health * 0.25)
            print(help.colour + help.name + Fore.RESET + f" dealt {str(damage)} damage to {name}!")
            print(f"{name}: " + boss_colour + "'WAHHH!!! that's hot!!!!'" + Fore.RESET)
            final_boss.current_health -= damage
            final_boss.goodEnding += 1
        elif final_boss.goodEnding == 5:
            help = monster_init.raymond
            damage = math.floor(final_boss.current_health - 1)
            print(help.colour + help.name + Fore.RESET + f" dealt {str(damage)} damage to {name}!")
            print(f"{name}: " + boss_colour + "'NOOOOOOOOOOoooooooooooo!!!'" + Fore.RESET)
            final_boss.current_health -= damage
            final_boss.goodEnding += 1
        elif final_boss.goodEnding == 6:
            damage = 999999999999999999999999999999
            print(f"\nYou dealt {str(damage)} damage to {name}!")
            final_boss.current_health = 0
            input(Fore.LIGHTRED_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            trigger_good_ending()

def trigger_good_ending():
    music.play_ending_music()
    os.system('cls' if os.name == 'nt' else 'clear')
    type_text("\n'What, how can this be?'", boss_colour)
    time.sleep(0.5)
    type_text("\n'I can't lose, I was made to be the greatest...'", boss_colour)
    time.sleep(0.5)
    type_text("\n'I guess they do say don't meet your maker'", boss_colour)
    time.sleep(0.5)
    type_text("\n\nYou and all of your new friends leave together", Fore.RESET)
    time.sleep(0.5)
    input(Fore.LIGHTRED_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

    os.system('cls' if os.name == 'nt' else 'clear')
    type_text(screens.good_ending, Fore.CYAN)
    type_text(screens.the_end_question, Fore.YELLOW)
    time.sleep(5)
    input(boss_colour + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to exit" + Fore.RESET)
    quit()

def trigger_true_ending():
    music.play_ending_music()
    os.system('cls' if os.name == 'nt' else 'clear')
    type_text("\n'What, even after all that? You choose to spare me?'", boss_colour)
    time.sleep(0.5)
    type_text("\n'Even though I'm a failed creation?'", boss_colour)
    time.sleep(0.5)
    type_text("\n'Even though I've not lived up to your hopes and dreams?'", boss_colour)
    time.sleep(0.5)
    type_text("\n\nThe Ooze then tells you the whole story from start.", Fore.RESET)
    time.sleep(0.5)
    input(Fore.LIGHTRED_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

    os.system('cls' if os.name == 'nt' else 'clear')
    type_text(screens.true_ending1, Fore.LIGHTBLUE_EX, 0.01)
    type_text(screens.true_ending2, Fore.CYAN, 0.01)
    type_text(screens.the_end, Fore.YELLOW)
    time.sleep(5)
    input(boss_colour + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to exit" + Fore.RESET)
    quit()

def recover():
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_health()
    print(description)
    display_health(False)
    time.sleep(1)
    final_boss.max_health = final_boss.max_health * 2
    final_boss.current_health = final_boss.max_health

def attack():
    if final_boss.goodEnding > 0:
        print(f"\n{name} struck you with black goo for 0 hit points!\nYou are immune!")
    else:
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

def killAttempt(sleep, text1, text2="", firstBit=True, override=0.01, wait=False):
    if firstBit:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.player_health = 100
        player.display_health()
        type_text("\n\n\n\n\n\n" + text2, Fore.LIGHTBLUE_EX)
        time.sleep(sleep)

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in count_down_health(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5),
                               player.max_health):
        time.sleep(override)
    player.player_health = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_health()
    if wait:
        time.sleep(sleep)
    type_text("\n\n\n\n\n\n" + text1, Fore.LIGHTBLUE_EX)
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

    print(Back.RESET, Fore.RESET)
    final_boss.finalBoss = True
    os.system('cls' if os.name == 'nt' else 'clear')

    type_text(title, Fore.YELLOW, 0)
    type_text(text1, Fore.CYAN)
    type_text(text2, Fore.MAGENTA)
    type_text(text3, Fore.CYAN)
    input(boss_colour + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(screens.battle_screen_dim)
    print(screens.there_are_enemies)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(screens.battle_screen_bright)
    print(screens.there_are_enemies)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(screens.battle_screen_dim)
    print(screens.there_are_enemies)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(screens.battle_screen_bright)
    print(screens.there_are_enemies)
    time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')

    music.play_boss_music()
    
    for i in health.health_bar_init(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5), player.max_health):
        time.sleep(0.01)
    os.system('cls' if os.name == 'nt' else 'clear')

    haveHp = True
    while haveHp:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.display_health()
        print(description)
        display_health(False)
        command_reader()
        if not final_boss.skip_attack:
            attack()
        else:
            final_boss.skip_attack = False
        if player.player_health == 1:
            haveHp = False

    final_boss.current_health = final_boss.max_health
    os.system('cls' if os.name == 'nt' else 'clear')
    print(picture + "\n" + name + boss_colour + "'You really thought you could beat me?'"
                                                      "\n'Let me show you just how far apart we both really are!'\n\n")
    input(boss_colour + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    print(Back.WHITE)
    os.system('cls' if os.name == 'nt' else 'clear')
    final_boss.boss_colour = Fore.LIGHTYELLOW_EX
    inverseSequence(2)
    inverseSequence(1)
    inverseSequence(0.5)
    inverseSequence(0.3)
    inverseSequence(0.2)
    inverseSequence(0.1)
    inverseSequence(0.05)
    print(Back.RESET)
    final_boss.boss_colour = Fore.LIGHTBLUE_EX
    player.player_health = player.max_health
    os.system('cls' if os.name == 'nt' else 'clear')
    player.display_health()
    print(picture)
    display_health(False)
    print("\n" + name + ": ")
    type_text("Now do you finally get it? The difference between you and I?", boss_colour)
    time.sleep(1)
    type_text("\nYou still don't know who you are. Your purpose.", boss_colour)
    time.sleep(1)
    type_text("\nAnd you shall die that way.", boss_colour)
    music.play_ending_music()
    input(Fore.LIGHTRED_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    os.system('cls' if os.name == 'nt' else 'clear')

    if player.karma < 5:
        for i in count_down_health(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5), player.max_health):
            time.sleep(0.05)
        player.player_health = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        player.display_health()
        type_text("\n\n\n\n\n\n'MWAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA'", Fore.LIGHTBLUE_EX)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        type_text(screens.bad_ending, Fore.CYAN)
        type_text(screens.the_end_question, Fore.YELLOW)
        time.sleep(5)
        input(boss_colour + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to exit..." + Fore.RESET)
        quit()
    else:
        final_boss.goodEnding = 1
        music.play_good_ending()
        killAttempt(3, "'HUH? You're supposed to be DEAD!'", "", False, 0.05, True)
        killAttempt(3, "'WHAT! How? What's happening?!", "Lets try that again.'")
        killAttempt(1, "'WHAT!'")
        killAttempt(0.5, "'IS!'")
        killAttempt(0.2, "'GOING!'")
        killAttempt(0.1, "'ON!'")
        type_text("\n'What have you done!'", boss_colour)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        type_text("\nYou hear a noise behind you and turn around", Fore.RESET)
        type_text("\nAll of your new friends who you spared in the facility appeared!", Fore.RESET)
        type_text(f"\nThey lend you strength to withstand {name}'s attacks!", Fore.RESET)
        input(Fore.LIGHTRED_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            player.display_health()
            print(description)
            display_health(False)
            command_reader()
            attack()
