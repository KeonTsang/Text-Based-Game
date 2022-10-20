from colorama import Fore 
import rooms as rooms

ROOM_1 = '?'
ROOM_2 = '?'
ROOM_3 = '?'
BARRIER = '*'

def print_map():
    if rooms.HYPERBARIC_CHAMBER["discovered"] == True:
        ROOM_6 = 'H'
    else:
        ROOM_6 = '?'

    if rooms.MAIN_FLOOR["discovered"] == True:
        ROOM_5 = 'M'
    else:
        ROOM_5 = '?'

    if rooms.TESTING_AREA["discovered"] == True:
        ROOM_4 = 'T'
    else:
        ROOM_4 = '?'


    map =(f"""
    ==================================================
    |~~~~~~~~~~~~~~~~~~~~~~|.................|~~~~~~~|
    |~~~~~~~~~~~~~~~~~~~~~~|.................|~~~~~~~|
    |___________________~~~|........{Fore.YELLOW + ROOM_1 + Fore.RESET}........|~~~~~~~|
    |..................|~~~|.................|~~~~~~~|
    |..................|~~~|_______..._______|~~~~~~~|
    |..................|~~~~~~~~~~|...|~~~~~~~~~~~~~~|
    |..................|~~~~~~~~~~|...|~~~~~~~~~~~~~~|
    |..................|~~~~______|{Fore.CYAN + BARRIER + BARRIER + BARRIER + Fore.RESET}|______.~~~~~~~|
    |.........{Fore.YELLOW + ROOM_2 + Fore.RESET}........|~~~|.................|~~~~~~~|
    |..................|___|.................|_______|
    |........................................{Fore.CYAN + BARRIER + Fore.RESET}........
    |...............................{Fore.YELLOW + ROOM_3 + Fore.RESET}........{Fore.CYAN + BARRIER + Fore.RESET}........
    |........................................{Fore.CYAN + BARRIER + Fore.RESET}........
    |...................___..................{Fore.CYAN + BARRIER + Fore.RESET}________
    |__________________|~~~|_______..._______|~~~~~~~|
    |______________________~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~__|...|__~~~~________|
    |.....................|~~~~~|.......|~~~~|.......|
    |..........{Fore.YELLOW + ROOM_4 + Fore.RESET}..........|_____|.......|____|.......|
    |................................................|
    |...............................{Fore.YELLOW + ROOM_5 + Fore.RESET}............{Fore.YELLOW + ROOM_6 + Fore.RESET}...|
    |................................................|
    |......................_____.........____........|
    |.....................|~~~~~|.......|~~~~|.......|
    ==================================================
    """)

    return map

    

