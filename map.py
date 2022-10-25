from colorama import Fore 
import rooms as rooms
import player as player


def print_map():

    ROOM_1 = '?'
    ROOM_2 = '?'
    BARRIER = '*'
    BARRIER_TO_RECEPTION = '*'

    #Sets the correct icon for HYPERBARIC CHAMBER:
    if rooms.HYPERBARIC_CHAMBER["discovered"] == True: 
        HC_ICON = Fore.LIGHTYELLOW_EX + 'H'
    else:
        HC_ICON = '?'

    #Sets the correct icon for MAIN FLOOR:
    if rooms.MAIN_FLOOR["discovered"] == True:
        MF_ICON = Fore.LIGHTYELLOW_EX + 'M'
    else:
        MF_ICON = '?'

    #Sets the correct icon for TESTING_AREA:
    if rooms.TESTING_AREA["discovered"] == True: #Checks if testing area has been visited. 
        TA_ICON = Fore.LIGHTYELLOW_EX + 'T'
        rooms.MAIN_FLOOR["exits"]["north"] = "Reception Area" #Then opens barrier to reception.
        BARRIER_TO_RECEPTION = Fore.WHITE + '.'
    else:
        TA_ICON = '?'

    #Sets the correct icon for RECEPTION AREA:
    if rooms.RECEPTION_AREA["discovered"] == True:
        RA_ICON = Fore.LIGHTYELLOW_EX + 'R'
    else:
        RA_ICON = '?'


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
    |...............................{Fore.YELLOW + RA_ICON + Fore.RESET}........{Fore.CYAN + BARRIER + Fore.RESET}........
    |........................................{Fore.CYAN + BARRIER + Fore.RESET}........
    |...................___..................{Fore.CYAN + BARRIER + Fore.RESET}________
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

    

