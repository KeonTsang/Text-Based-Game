import player
from monsters import Stethoscope

stephy = Stethoscope()

def battleMonster(monster):
    phase1 = True
    phase2 = True
    phase3 = True
    while monster.isAlive() or monster:
        while phase1:
            phase1 = monster.phase1()
            if player.player_health < 1:
                print("Game Over\nYou died!")
        while phase2:
            phase2 = monster.phase2()
            if player.player_health < 1:
                print("Game Over\nYou died!")
        while phase3:
            phase3 =monster.phase3()
            if player.player_health < 1:
                print("Game Over\nYouDied!")

battleMonster(stephy)