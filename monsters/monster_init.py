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

    #for i in range(0, player.player_health, 10):
    #    os.system('cls' if os.name == 'nt' else 'clear')
    #    print(health.genHealthBar(i))
    #    time.sleep(0.01)
    #os.system('cls' if os.name == 'nt' else 'clear')

    phase1 = True
    phase2 = True
    phase3 = True
    while not monster.isSpared() and monster.isAlive():

        if monster.getPhase() == 1:
            player.displayHealth()
            print(monster.image)
            monster.display_health()
            monster.phase1()
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