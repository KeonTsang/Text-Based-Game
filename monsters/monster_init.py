import time
import math
from colorama import Fore, Style

# import game
import player
import health
import os
import screens
import final_boss
from monsters.stethoscope import Stethoscope
from monsters.testtuberack import TestTubeRack
from monsters.centrifuge import Centrifuge
from monsters.bunsenburner import BunsenBurner
from monsters.nuclearraygun import NuclearRayGun

stephy = Stethoscope(15)
c3nti = Centrifuge(35)
sgtripper = TestTubeRack(50)
mrburns = BunsenBurner(65)
raymond = NuclearRayGun(90)


def end_phase():
    input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
    os.system('cls' if os.name == 'nt' else 'clear')


def battle_monster(monster):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Style.BRIGHT)
    for i in health.health_bar_init(range(player.player_health), "Your Health: ", math.floor(player.max_health * 0.5),
                                    player.max_health):
        time.sleep(0.01)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Style.RESET_ALL)

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
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in final_boss.count_down_health(range(player.player_health), "Your Health: ",
                                                  math.floor(player.max_health * 0.5), player.max_health):
                time.sleep(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')
            final_boss.type_text(screens.you_died, Fore.CYAN)
            final_boss.type_text(screens.game_over, Fore.YELLOW)
            time.sleep(5)
            input(Fore.LIGHTBLUE_EX + "\n(•) " + Fore.LIGHTYELLOW_EX + "Press enter to exit" + Fore.RESET)
            quit()
