import player
from monsters.monster import Monster
from colorama import Fore


class Bunsen_Burner(Monster):

    def __init__(self):
        super(Bunsen_Burner, self).__init__("Mr Burns", 15, 15, 1, 0.25, Fore.RED)

    def phase1(self):
        self.command_reader()
        if not self.isAlive():
            return
        self.attack()

    def phase2(self):
        self.command_reader()
        if not self.isAlive():
            return
        self.attack()

    def phase3(self):
        self.command_reader()
        if not self.isAlive():
            return
        self.attack()

    def execute_spare(self):
        if self.getPhase() == 3:
            self.spare()
        else:
            print(f"You cannot spare {self.name} yet!")

    def execute_talk(self):
        print(f"\nYou told {self.name} You're on fire!")
        print(f"{self.name}: " + self.colour + " 'Oh no..., anyways.'" + Fore.RESET)

    def execute_action(self):
        if self.getPhase() == 1:
            print(f"\n You try to pour water on him")
            print(f"{self.name}: " + self.colour + "'Fires beats water, DUH!'" + Fore.RESET)
        else:
            print(f"\nYou pour an enormous amount of water onto {self.name} ")
            print(f"{self.name}: " + self.colour + "'Not bad, but its not over!'" + Fore.RESET)
            self.setPhase(3)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: " + self.colour + "'That hurt, only a bit.'" + Fore.RESET)
        self.damage(damage)
        self.setPhase(1)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: " + self.colour + "'Thanks, that was very cool of you.'" + Fore.RESET)
        self.setSpared()
        player.karma += 1

    def print_description(self):
        description = f"\n{self.name} Mr Burns appeared!\n\n{self.name}: " + self.colour + "'I'm Mr Burns and you're going to burn'\n" + Fore.RESET
        image = """......~~......
                   ......~~......
                   ......~~......
                   ......||......
                   ......||......
                   ......||......
                   ......||......
                   ......||......
                   ......||......
                   ......||......
                   ......||......
                   ......||......
                   ...../==\.....
                   .============."""

        print(description, image)
        self.display_health()
        print("\nWhat will you do?")