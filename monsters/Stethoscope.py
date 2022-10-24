import player
from monsters import Monster
import game_parser


class stethoscope(Monster):

    def __init__(self):
        super().__init__(self, "Stephy", 20, 7, 0.05)

    def phase1(self):
        self.command_reader()
        return False if self.getPhase() > 1 else True

    def phase2(self):
        self.command_reader()
        return False if self.getPhase() > 2 else True

    def phase3(self):
        self.command_reader()
        return False if self.getPhase() > 3 else True

    def execute_spare(self):
        if self.getPhase() == 3:
            self.spare()
        else:
            print(f"You cannot spare {self.name} yet!")

    def execute_talk(self):
        if self.getPhase() == 1:
            print("You told the stethoscope it is great at listening to hearts!")
            print(f"{self.name}: 'Thank you! Maybe I could try listening to yours!'")
            self.setPhase(2)
        else:
            print(f"You complement {self.name} again!")
            print(f"{self.name}: 'Thanks friend!'")

    def execute_action(self):
        if self.getPhase() == 1:
            print(f"You try to get {self.name} to measure your heart beat!")
            print(f"{self.name}: 'Woah I barely know you!'")
        else:
            print("You let the stethoscope measure your heart beat!")
            print(f"{self.name}: 'You have a great beat partner!'")
            self.setPhase(3)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        self.damage(damage)
        print(f"You dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: 'Owww!!! That hurts!'")

    def spare(self):
        print(f"You spared {self.name}")
        print(f"{self.name}: That was fun! We should do this again sometime! Bye now!")
        self.setSpare()