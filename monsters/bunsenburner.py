import player
from monsters.monster import Monster
from items import item_init
from colorama import Fore
import random


class BunsenBurner(Monster):

    def __init__(self):
        super(BunsenBurner, self).__init__("Mr Burns", 20, 12, 1, 0.05, Fore.RED, item_init.bunsen)

    def attack(self):
        if not self.isSpared():
            damage = 0 if random.random() < self.miss_chance else random.randint(self.min_damage, self.max_damage)
            if damage == 0:
                print(f"\n{self.name} blew fire at you but missed!")
            else:
                print(f"\n{self.name} burned you with fire for {damage} hit points!")
                player.player_health -= damage

    def execute_talk(self):
        if (self.getPhase() == 1):
            print(f"\nYou told {self.name} that he is a hot head!")
            print(f"{self.name}: " + self.colour + " 'Now you're firing me up!'" + Fore.RESET)
            self.setPhase(2)
        else:
            print(f"\nYou told {self.name} that he is a hot head!")
            print(f"{self.name}: " + self.colour + " 'You're not firing me up anymore!'" + Fore.RESET)
    def execute_action(self):
        print(f"\n You try to pour water on him")
        print(f"{self.name}: " + self.colour + "'Fires beats water, DUH!'" + Fore.RESET)

    def execute_attack(self):
        if (self.getPhase() == 2):
            weapon = player.current_weapon
            damage = weapon.attack()
            print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
            print(f"{self.name}: " + self.colour + "'WOAHHHH now thats what I call fired up!'" + Fore.RESET)
            self.damage(damage)
            self.setPhase(3)
        else:
            weapon = player.current_weapon
            damage = weapon.attack()
            print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
            print(f"{self.name}: " + self.colour + "'That hurt, only a bit.'" + Fore.RESET)
            self.damage(damage)
            self.setPhase(3)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: " + self.colour + "'That battle was as intense as my flames!'" + Fore.RESET)
        self.setSpared()
        player.karma += 1

    def print_description(self):
        description = f"\n{self.name} the Bunsen Burner appeared!\n\n{self.name}: " + self.colour + \
                      f"'I'm {self.name} and you're going to burn'\n" + Fore.RESET
        image = """              
                         ~~~     
                        ~~~~~     
                        ~~~~~      
                         | |      
                         | |      
                         | |      
                         | |      
                         | |      
                         | |      
                         | |      
                         | |      
                        /===\     
                   [=============] """

        print(description, image)
        self.display_health()
        print("\nWhat will you do?")