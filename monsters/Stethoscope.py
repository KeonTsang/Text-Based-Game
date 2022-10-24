import player
from monsters import Monster
import game_parser


class stethoscope(Monster):

    def __init__(self):
        Monster.__init__(self, "Stephy", 20, 7)
        self.phase = 1

    def phase1(self):
        command = input(f"ATTACK {self.name}\nTALK to {self.name}\nSPARE {self.name}")
        self.execute_command(game_parser.normalise_input(command))
        return True

    def execute_spare(self):
        if self.phase == 3:
            print(f"You spared {self.name}")
        else:
            print(f"You cannot spare {self.name} yet!")

    def execute_talk(self):
        if self.phase == 1:
            print("You told the stethoscope it is great at listening to hearts!")
            print(f"{self.name}: 'Thank you! Maybe I could try listening to yours!'")
        else:
            print(f"You complement {self.name} again!")
            print(f"{self.name}: 'Thanks friend!'")

    def execute_action(self):
        if self.phase == 1:
            print(f"You try to get {self.name} to measure your heart beat!")
            print(f"{self.name}: 'Woah I barely know you!'")
        else:
            print("You let the stethoscope measure your heart beat!")
            print(f"{self.name}: 'You have a great beat partner!'")

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        self.health -= damage
        print(f"You dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: 'Owww!!! That hurts!'")