import random
from colorama import Fore
import math

from items.item import Item


class Weapon(Item):

    def __init__(self, name, id, max_damage, min_damage, crit_chance, description):
        super(Weapon, self).__init__(name, id, description)
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.crit_chance = crit_chance

    # Returns damage dealt by weapon
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        if random.random() < self.crit_chance:
            damage = damage * 2
            print(Fore.LIGHTRED_EX + "\nCritical Hit!" + Fore.RESET)
        return damage

    # Prints weapon stats
    def get_description(self):
        return ("Weapon Name: " + Fore.LIGHTWHITE_EX + self.name + "\n" + Fore.RESET +
        "Weapon Max Damage: " + Fore.LIGHTWHITE_EX + str(self.max_damage) + "\n" + Fore.RESET +
        "Weapon Min Damage: " + Fore.LIGHTWHITE_EX + str(self.min_damage) + "\n" + Fore.RESET +
        "Weapon Critical Hit Chance: " + Fore.LIGHTWHITE_EX + str(math.floor(self.crit_chance * 100)) + "%\n" + Fore.RESET +
        "Weapon Description: " + Fore.LIGHTWHITE_EX + self.description + Fore.RESET)
