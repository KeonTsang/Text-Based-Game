#Import modules / files.
import time
from colorama import Fore

import random
import player
import title_screen as ts
import music as music
import health as health
import map as map
import os as os
import rooms as rooms
import items as items
from game_parser import *
from player import *
from items import item_init

#Prints the title screen and plays the title screen music.
ts.print_title()

#Plays the main game music.
music.play_main_game_music()

#Prints the health bar. Use 'health.health_bar_x' to change the health bar.
for i in health.health_bar_init(range(player.player_health), "Health: ", 50, Fore.GREEN):
    time.sleep(0.01)

#Flushes screen in preperation for the health bar.
os.system('cls' if os.name == 'nt' else 'clear')

#####################################################################################################################

def list_of_items(items):
    return ", ".join([item.name for item in items])


def print_room_items(room):
    if room["items"] != []:
        print(Fore.RED + "(!) " + Fore.RESET + "There is a " + list_of_items(room["items"]) + " here.")
        print()

def print_inventory_items(items):
    if [item.name for item in items] != []:
        print(Fore.LIGHTMAGENTA_EX + "(!) " + Fore.RESET + "You have a " + list_of_items(items) + ".")
        print()
    else:
        print("You have nothing in your inventory.")
        print()

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
    return rooms[exits[direction]]["name"]


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
        print(Fore.GREEN + "(★) " + Fore.RESET + "TAKE " + item.name.upper() + " to take " + item.name + ".")
    # Iterate over items in the inventory
    for item in inv_items:
        # Print the item name and description
        print(Fore.RED + "(★) " + Fore.RESET + "DROP " + item.name.upper() + " to drop " + item.name + ".")
    print()
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        current_room = move(current_room["exits"], direction)
        print_room(current_room)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    global current_room
    global inventory
    for item in current_room["items"]:
        if item.name == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            print(Fore.LIGHTRED_EX + "(!) " + Fore.RESET + "You took " + item.name + ".")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return
    print("You cannot take that.")


def execute_drop(item_id):
    global current_room
    global inventory
    for item in inventory:
        if item.name == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            print(Fore.LIGHTRED_EX + "(!) " + Fore.RESET + "You drop the " + item.name + ".")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return
    print("You cannot drop that.")

def execute_look(item_id):
    global current_room
    global inventory
    for item in inventory:
        if item.name == item_id:
            print(Fore.LIGHTRED_EX + "(!) " + Fore.RESET + item["description"])
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return
    print("You cannot look at that.")
    

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

    elif command[0] == "look":
        if len(command) > 1:
            execute_look(command[1])
        else:
            print("Look at what?")

    elif command[0] == "damage":
        player.player_health -= random.randint(0, 10)

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
    return rooms[exits[direction]]

    

def main():
    # Main game loop
    while True:
        #Clears screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #Prints the health bar (no animation).
        player.displayHealth()

        #Sets discovery to True.
        current_room["discovered"] = True

        #Checks if player has map in inventory. If so, print map.
        if item_init.map in inventory:
            print(map.print_map())

        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

# Start the game
if __name__ == "__main__":
    main()





