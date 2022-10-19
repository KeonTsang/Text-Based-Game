#Import modules / files.
import time
from colorama import Fore
import title_screen as ts
import music as music
import health as health
import map as map
import os as os
import rooms as rooms
import items as items
from game_parser import *
from player import *

#Prints the title screen and plays the title screen music.
ts.print_title()

#Plays the main game music.
music.play_main_game_music()

#Prints the health bar. Use 'health.health_bar_x' to change the health bar.
for i in health.health_bar_init(range(100), "Health: ", 50, Fore.GREEN):
    time.sleep(0.01)

#Flushes screen in preperation for the health bar.
os.system('cls' if os.name == 'nt' else 'clear')

#Prints the health bar (no animation).
print(health.health_bar_100)

#####################################################################################################################

def list_of_items(items):
    return ", ".join([item["name"] for item in items])


def print_room_items(room):
    if room["items"] != []:
        print("There is a " + list_of_items(room["items"]) + " here.")
        print()

def print_inventory_items(items):
    if [item["name"] for item in items] != []:
        print("You have a " + list_of_items(items) + ".")
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
    print("GO " + direction.upper() + " to " + leads_to + "." + Fore.GREEN + "()" + Fore.RESET)


def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    # Iterate over items in the room
    for item in room_items:
        # Print the item name and description
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + "." + Fore.GREEN + "()" + Fore.RESET)
    # Iterate over items in the inventory
    for item in inv_items:
        # Print the item name and description
        print("DROP " + item["id"].upper() + " to drop " + item["name"] + "." + Fore.RED + "()" + Fore.RESET)
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
        if item["id"] == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            print("You took " + item["name"] + ".")
            return
    print("You cannot take that.")


def execute_drop(item_id):
    global current_room
    global inventory
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            print("You drop the " + item["name"] + ".")
            return
    print("You cannot drop that.")
    

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

    else:
        print("This makes no sense.")


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

    
# This is the entry point of our program
def main():
    # Main game loop
    while True:
        #Clears screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #Prints the health bar (no animation).
        print(health.health_bar_100)

        
        #Sets discovery to True.
        current_room["discovered"] = True

        #Checks if player has map in inventory. If so, print map.
        if item_map in inventory:
            print(map.print_map())


        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

if __name__ == "__main__":
    main()





