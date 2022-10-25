import time
from colorama import Fore

import game
import player
import health
import os
from monsters.stethoscope import Stethoscope
from monsters.testtuberack import TestTubeRack

stephy = Stethoscope()
sgtripper = TestTubeRack()


def end_phase():
    input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    os.system('cls' if os.name == 'nt' else 'clear')


def battleMonster(monster):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in health.health_bar_init(range(player.player_health), "Your Health: ", 50, Fore.GREEN):
        time.sleep(0.01)
    os.system('cls' if os.name == 'nt' else 'clear')

    while not monster.isSpared() and monster.isAlive():

        if monster.getPhase() == 1:
            player.display_health()
            monster.print_description()
            monster.phase1()
            end_phase()
        elif monster.getPhase() == 2:
            player.display_health()
            monster.print_description()
            monster.phase2()
            end_phase()
        elif monster.getPhase() == 3:
            player.display_health()
            monster.print_description()
            monster.phase3()
            end_phase()
        if player.player_health < 1:
            print("Game Over\nYou died!")
            game.end_game()
            break
