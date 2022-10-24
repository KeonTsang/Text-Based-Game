import player
import health
from monsters.stethoscope import Stethoscope

stephy = Stethoscope()


def battleMonster(monster):
    phase1 = True
    phase2 = True
    phase3 = True
    while not monster.isSpared() and monster.isAlive():
        while phase1 and monster.isAlive():
            print(health.genHealthBar(player.player_health))
            monster.display_health()
            phase1 = monster.phase1()
            if player.player_health < 1:
                print("Game Over\nYou died!")
        while phase2 and monster.isAlive():
            print(health.genHealthBar(player.player_health))
            monster.display_health()
            phase2 = monster.phase2()
            if player.player_health < 1:
                print("Game Over\nYou died!")
        while phase3 and monster.isAlive():
            print(health.genHealthBar(player.player_health))
            monster.display_health()
            phase3 = monster.phase3()
            if player.player_health < 1:
                print("Game Over\nYou died!")
