import player
from monsters.monster import Monster


class Stethoscope(Monster):

    def __init__(self):
        super(Stethoscope, self).__init__("Stephy", 20, 7, 5, 0.05)

    def phase1(self):
        self.command_reader()
        self.attack()
        return False if self.getPhase() > 1 else True

    def phase2(self):
        self.command_reader()
        self.attack()
        return False if self.getPhase() > 2 else True

    def phase3(self):
        self.command_reader()
        self.attack()
        return False if self.isSpared() else True

    def execute_spare(self):
        if self.getPhase() == 3:
            self.spare()
        else:
            print(f"You cannot spare {self.name} yet!")

    def execute_talk(self):
        if self.getPhase() == 1:
            print("\nYou told the stethoscope it is great at listening to hearts!")
            print(f"{self.name}: 'Thank you! Maybe I could try listening to yours!'")
            self.setPhase(2)
        else:
            print(f"\nYou complement {self.name} again!")
            print(f"{self.name}: 'Thanks friend!'")

    def execute_action(self):
        if self.getPhase() == 1:
            print(f"\nYou try to get {self.name} to measure your heart beat!")
            print(f"{self.name}: 'Woah I barely know you!'")
        else:
            print("\nYou let the stethoscope measure your heart beat!")
            print(f"{self.name}: 'You have a great beat partner!'")
            self.setPhase(3)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        self.damage(damage)
        print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: 'Owww!!! That hurts!'\n")
        self.setPhase(1)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: That was fun! We should do this again sometime! Bye now!")
        self.setSpared()