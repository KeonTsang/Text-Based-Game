import player
from monsters.monster import Monster
from colorama import Fore
import random
import rooms
from items import item_init


class NuclearRayGun(Monster):

    def __init__(self, health):
        super(NuclearRayGun, self).__init__("Raymond", health, 30, 15, 0.5, Fore.LIGHTGREEN_EX, item_init.raygun)

    def attack(self):
        if not self.isSpared():
            damage = 0 if random.random() < self.miss_chance else random.randint(self.min_damage, self.max_damage)
            if damage == 0:
                print(f"\n{self.name} Shot a nuclear laser at you but missed!")
            else:
                print(f"\n{self.name} Shot a nuclear laser at you for {damage} hit points!")
                player.player_health -= damage

    def damage(self, damage):
        super().damage(damage)
        if self.health < 1:
            rooms.RECEPTION_AREA["exits"]["east"] = "Secret Testing Facility"
            player.has_unlocked_boss = True

    def execute_talk(self):
        print(f"\nYou told {self.name} that he is radioactive!")
        print(f"{self.name}: " + self.colour + " 'Woaoaoh, I'm RADIOACTIVE, RADIOACTIVE!'" + Fore.RESET)

    def execute_action(self):
        if (self.getPhase() == 1):
            print(f"\nYou put on the hazmat suit!")
            print(f"{self.name}: " + self.colour + " 'You think that will stop my radiation?'" + Fore.RESET)
            self.setPhase(2)
        elif (self.getPhase() == 2):
            print(f"\nYou embrace {self.name}!")
            print(f"{self.name}: " + self.colour + " 'Thanks pal!'" + Fore.RESET)
            self.setPhase(3)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: " + self.colour + "'Careful there! You'll make me have a meltdown!'" + Fore.RESET)
        self.damage(damage)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: " + self.colour + "'See you around, man!'" + Fore.RESET)
        self.setSpared()
        player.karma += 1
        rooms.RECEPTION_AREA["exits"]["east"] = "Secret Testing Facility"
        player.has_unlocked_boss = True

    def print_description(self):
        description = f"\n{self.name} the Nuclear Ray Gun appeared!\n\n{self.name}: " + self.colour + \
                      f"'I'm going to ionise you to oblivion!'\n" + Fore.RESET
        image = """                         
                                     ____    __     
                                 ___/    \__/ /      
  |\                         ___/   ^    ^   /       
  | ========================/       0    0   )       
  |                          |         >      )       
  | ========================______  \____/   )       
  |/                     |     / /\_________/        
                         \   /_/  |        |        
                           \______|        |        
                                  |        |        
                                  \________/        
                         """

        print(description, image)
        self.display_health()
        print("\nWhat will you do?")