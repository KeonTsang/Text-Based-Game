from colorama import Fore 
import rooms as rooms
import player as player
from items import item_init


def print_map():

    ROOM_1 = '?'
    ROOM_2 = '?'
    BARRIER_1 = '*'
    BARRIER = '*'
    BARRIER_TO_RECEPTION = '*'

    if item_init.keycard in player.inventory:
        rooms.MED_BAY["exits"]["north"] = "Reception Area" #Then opens barrier to reception.
        BARRIER_TO_RECEPTION = Fore.WHITE + '.'
    


    #Sets the correct icon for HYPERBARIC CHAMBER:
    if rooms.HYPERBARIC_CHAMBER["discovered"] == True: 
        HC_ICON = Fore.LIGHTYELLOW_EX + 'H'
    else:
        HC_ICON = '?'

    #Sets the correct icon for MAIN FLOOR:
    if rooms.MED_BAY["discovered"] == True:
        MF_ICON = Fore.LIGHTYELLOW_EX + 'M'
    else:
        MF_ICON = '?'

    #Sets the correct icon for TESTING_AREA:
    if rooms.TESTING_AREA["discovered"] == True: 
        TA_ICON = Fore.LIGHTYELLOW_EX + 'T'
    else:
        TA_ICON = '?'

    #Sets the correct icon for RECEPTION AREA:
    if rooms.RECEPTION_AREA["discovered"] == True:
        RA_ICON = Fore.LIGHTYELLOW_EX + 'R'
    else:
        RA_ICON = '?'

    if rooms.PYROTECHNICS_LAB["discovered"] == True:
        PL_ICON = Fore.LIGHTYELLOW_EX + 'P'
    else:
        PL_ICON = '?'

    if rooms.NUCLEAR_TESTING_SITE["discovered"] == True:
        NT_ICON = Fore.LIGHTYELLOW_EX + 'N'
    else:
        NT_ICON = '?'


    map =(f"""
    ==================================================
    |~~~~~~~~~~~~~~~~~~~~~~|.................|~~~~~~~|
    |~~~~~~~~~~~~~~~~~~~~~~|.................|~~~~~~~|
    |___________________~~~|........{Fore.YELLOW + NT_ICON + Fore.RESET}........|~~~~~~~|
    |..................|~~~|.................|~~~~~~~|
    |..................|~~~|_______..._______|~~~~~~~|
    |..................|~~~~~~~~~~|...|~~~~~~~~~~~~~~|
    |..................|~~~~~~~~~~|...|~~~~~~~~~~~~~~|
    |..................|~~~~______|{Fore.CYAN + BARRIER + BARRIER + BARRIER + Fore.RESET}|______.~~~~~~~|
    |.........{Fore.YELLOW + PL_ICON + Fore.RESET}........|~~~|.................|~~~~~~~|
    |..................|___|.................|_______|
    |........................................{Fore.CYAN + BARRIER_1 + Fore.RESET}........
    |...............................{Fore.YELLOW + RA_ICON + Fore.RESET}........{Fore.CYAN + BARRIER + Fore.RESET}........
    |........................................{Fore.CYAN + BARRIER_1 + Fore.RESET}........
    |...................___..................{Fore.CYAN + BARRIER_1 + Fore.RESET}________
    |__________________|~~~|_______..._______|~~~~~~~|
    |______________________~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~~~|...|~~~~~~~~~~~~~~|
    |.....................|~~~~~__|{Fore.CYAN + BARRIER_TO_RECEPTION + BARRIER_TO_RECEPTION + BARRIER_TO_RECEPTION + Fore.RESET}|__~~~~________|
    |.....................|~~~~~|.......|~~~~|.......|
    |..........{Fore.YELLOW + TA_ICON + Fore.RESET}..........|_____|.......|____|.......|
    |................................................|
    |...............................{Fore.YELLOW + MF_ICON + Fore.RESET}............{Fore.YELLOW + HC_ICON + Fore.RESET}...|
    |................................................|
    |......................_____.........____........|
    |.....................|~~~~~|.......|~~~~|.......|
    ==================================================
    """)

    return map

    

