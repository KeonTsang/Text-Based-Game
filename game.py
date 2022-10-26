#Import modules / files.
import time
import math
from colorama import Fore

import player
import screens
import title_screen as ts
import music as music
import health as health
import map as map
import os as os
import rooms as rooms
from game_parser import *
from items import item_init
from items.weapon import Weapon
from monsters import monster_init

#Prints the title screen and plays the title screen music.
ts.print_title()

#Plays the main game music.
music.play_main_game_music()

#Prints the health bar. Use 'health.health_bar_x' to change the health bar.
for i in health.health_bar_init(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5)):
    time.sleep(0.01)

#Flushes screen in preperation for the health bar.
os.system('cls' if os.name == 'nt' else 'clear')

#####################################################################################################################

endGame = False
def end_game():
    endGame = True

def list_of_items(items):
    return ", ".join([item.name for item in items])


def print_room_items(room):
    if room["items"] != []:
        print(Fore.RED + "(!) " + Fore.RESET + "There is a " + list_of_items(room["items"]) + " here.")
        print()

def print_inventory_items(items):
    if [item.id for item in items] != []:
        print(Fore.LIGHTMAGENTA_EX + "(!) " + Fore.RESET + "You have a " + list_of_items(items) + ".")
    else:
        print(Fore.LIGHTMAGENTA_EX + "(!) " + Fore.RESET + "You have a nothing in your inventory.")

def print_current_weapon():
    print(Fore.LIGHTCYAN_EX + "(!) " + Fore.RESET + "Your current weapon is a " + player.current_weapon.name + ".\n")

def print_room(room):
    # Display room name
    print()
    print(Fore.YELLOW + room["name"].upper() + " " + "(" + room["name"][0] + ")" + Fore.RESET )
    print()
    # Display room description
    print(Fore.BLUE + room["description"] + Fore.RESET)
    print()
    # Display list of items in the room
    print_room_items(room)

def exit_leads_to(exits, direction):
    ref = rooms.rooms[exits[direction]]
    return ref["name"]


def print_exit(direction, leads_to):
    print(Fore.GREEN + "(★) " + Fore.RESET + "GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    # Iterate over items in the room
    for item in room_items:
        # Print the item name and description
        print(Fore.GREEN + "(★) " + Fore.RESET + "TAKE " + item.id.upper() + " to take " + item.name + ".")
    # Iterate over items in the inventory
    for item in inv_items:
        # Print the item name and description
        print(Fore.RED + "(★) " + Fore.RESET + "DROP " + item.id.upper() + " to drop " + item.name + ".")

    if player.current_room == rooms.rooms["Reception Area"]:
        print(Fore.RED + "(★) " + Fore.RESET + "USE KEYPAD" + " to use the keypad to the north.")

    print()
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    if is_valid_exit(player.current_room["exits"], direction):
        player.current_room = move(player.current_room["exits"], direction)
        print_room(player.current_room)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    for item in player.current_room["items"]:
        if item.id == item_id:
            if isinstance(item, Weapon):
                print(Fore.LIGHTRED_EX + "\n(!) " + Fore.RESET + "You replaced your current weapon, " +
                      Fore.LIGHTWHITE_EX + player.current_weapon.name + Fore.RESET + " with " + Fore.LIGHTWHITE_EX +
                      item.name + Fore.RESET + ".")
                player.current_weapon = item
            else:
                player.inventory.append(item)
                print(Fore.LIGHTRED_EX + "\n(!) " + Fore.RESET + "You took " + item.name + ".")
            player.current_room["items"].remove(item)
            print(Fore.LIGHTCYAN_EX + "\n(↳) " + Fore.RESET + item.get_description())
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return
    print("You cannot take that.")


def execute_drop(item_id):
    for item in player.inventory:
        if item.id == item_id:
            player.inventory.remove(item)
            player.current_room["items"].append(item)
            print(Fore.LIGHTRED_EX + "\n(!) " + Fore.RESET + "You drop the " + item.name + ".")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return
    print("You cannot drop that.")

def execute_look(item_id):
    for item in player.inventory:
        if item.id == item_id:
            print(Fore.LIGHTRED_EX + "\n(!) " + Fore.RESET + item.get_description())
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return
    if player.current_weapon.id == item_id:
        print("\n" + player.current_weapon.get_description() + "\n")
        input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
        return
    print("You cannot look at that.")

def execute_use(item_to_use):
    if item_to_use == "keypad" and player.current_room == rooms.rooms["Reception Area"]:
        if player.has_unlocked_nuclear_room == False:
            user_input = input(Fore.LIGHTRED_EX + "(!) " + Fore.RESET + "ENTER KEYCODE: ")
            if user_input == "NUcL3@R":
                print(Fore.LIGHTRED_EX + "(!) " + Fore.RESET + "You hear a click and the door opens.")
                input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
                player.current_room["exits"]["north"] = "Nuclear Testing Site"
                player.has_unlocked_nuclear_room = True
                return 
            else:
                print(Fore.LIGHTRED_EX + "(!) " + Fore.RESET + "The keypad beeps and flashes red.")
                input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
                return 
        else:
            print(Fore.LIGHTGREEN_EX + "(!) " + Fore.RESET + "The door is already unlocked.")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return 
    else:
        print(Fore.LIGHTBLUE_EX + "(!) " + Fore.RESET + "There is not a keypad in this room you can use.")
        input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")

    elif command[0] == "look" or command[0] == "inspect" or command[0] == "observe" or command[0] == "examine": 
        if len(command) > 1:
            execute_look(command[1])
        else:
            print("Look at what?")

    elif command[0] == "help":
        print()
        print("Commands:")
        print(Fore.LIGHTBLUE_EX + "(!) " + Fore.RESET + "GO [direction] - Moves you in the direction you choose.")
        print(Fore.LIGHTBLUE_EX+ "(!) " + Fore.RESET + "TAKE [item] - Takes the item you choose.")
        print(Fore.LIGHTBLUE_EX + "(!) " + Fore.RESET + "DROP [item] - Drops the item you choose.")
        print(Fore.LIGHTBLUE_EX + "(!) " + Fore.RESET + "LOOK [item] - Looks at the item you choose.")
        input(Fore.LIGHTBLUE_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
        
    else:
        print(f"'{command[0]}' -> Makes no sense.")
        input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms.rooms[exits[direction]]

def monster_check():
    monsters = player.current_room["monsters"]
    if len(monsters) > 0:
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
        monster_init.battle_monster(monsters[0])

def main():

    # Main game loop
    while not endGame:
        #Clears screen
        os.system('cls' if os.name == 'nt' else 'clear')

        #Sets discovery to True.
        player.current_room["discovered"] = True

        monster_check()

        # Prints the health bar (no animation).
        player.display_health()

        #Checks if player has map in inventory. If so, print map.
        if item_init.map in player.inventory:
            print(map.print_map())

        # Display game status (room description, inventory etc.)
        print_room(player.current_room)
        print_inventory_items(player.inventory)
        print_current_weapon()

        # Show the menu with possible actions and ask the player
        command = menu(player.current_room["exits"], player.current_room["items"], player.inventory)

        # Execute the player's command
        execute_command(command)

# Start the game
if __name__ == "__main__":
    main()





