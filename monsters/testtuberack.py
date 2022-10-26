import player
from monsters.monster import Monster
from colorama import Fore
import random
from items import item_init
class TestTubeRack(Monster):

    def __init__(self, health):
        super(TestTubeRack, self).__init__("Sgt Ripper", health, 12, 6, 0.10, Fore.LIGHTRED_EX, item_init.testtube)

    # Overidden from super
    def attack(self):
        if not self.isSpared():
            damage = 0 if random.random() < self.miss_chance else random.randint(self.min_damage, self.max_damage)
            if damage == 0:
                print(f"\n{self.name} fired a test tube but it missed!")
            else:
                print(f"\n{self.name} launched a test tube at you for {damage} hit points!")
                player.player_health -= damage

    def execute_talk(self):
        print(f"\nYou told {self.name} it shoots cool rockets!")
        print(f"{self.name}: " + self.colour + " 'Flattery won't save you soldier!'" + Fore.RESET)

    def execute_action(self):
        if self.getPhase() == 1:
            print(f"\nYou launch a test tube into the air!")
            print(f"{self.name}: " + self.colour + "'Nice shot soldier, but you'll never beat this!'" + Fore.RESET)
            self.setPhase(2)
        else:
            print(f"\nYou launch another test tube even higher than {self.name} !")
            print(f"{self.name}: " + self.colour + "'Alright son, you got me! I can't beat that.'" + Fore.RESET)
            self.setPhase(3)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: " + self.colour + "'You're risking court martial trooper!'" + Fore.RESET)
        self.damage(damage)
        self.setPhase(1)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: " + self.colour + "'Thanks for having a thrilling battle with your old sergeant.'" + Fore.RESET)
        self.setSpared()
        player.karma += 1

    def print_description(self):
        description = f"\n{self.name} the Test Tube Rack appeared!\n\n{self.name}: " + self.colour + f"'{self.name} here reporting for duty!'\n" + Fore.RESET
        image = """
                         
       \ / \ / \ /          
      _| |_| |_| |_________        
     / | | | | | |  <==>  /        
    /____________________/|        
    |  | | | | | |  \ /  ||        
    |  | | | | | |  0 0  ||        
    |  | | | | | | \_^_/ ||        
    |  \_/ \_/ \_/ \___/ |/        
    |____________________/         
                         
                         """
        print(description, image)
        self.display_health()
        print("\nWhat will you do?")