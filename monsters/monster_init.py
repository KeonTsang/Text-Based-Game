import time
from colorama import Fore
import player
import health
import os
from monsters.stethoscope import Stethoscope

stephy = Stethoscope()


def battleMonster(monster):

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in health.health_bar_init(range(player.player_health), "Health: ", 50, Fore.GREEN):
        time.sleep(0.01)
    os.system('cls' if os.name == 'nt' else 'clear')

    while not monster.isSpared() and monster.isAlive():

        if monster.getPhase() == 1:
            player.displayHealth()
            print("\n" + monster.image)
            monster.display_health()
            monster.phase1()
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif monster.getPhase() == 2:
            player.displayHealth()
            monster.display_health()
            monster.phase2()
        elif monster.getPhase() == 3:
            player.displayHealth()
            monster.display_health()
            monster.phase3()

        if player.player_health < 1:
            print("Game Over\nYou died!")
            break