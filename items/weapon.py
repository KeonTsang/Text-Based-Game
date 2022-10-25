import random
from colorama import Fore

from items.item import Item


class Weapon(Item):

    def __init__(self, name, max_damage, min_damage, crit_chance, description):
        super(Weapon, self).__init__(name, description)
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.crit_chance = crit_chance

    # Returns damage dealt by weapon
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        if random.random() < self.crit_chance:
            damage = damage * 2
            print(Fore.LIGHTRED_EX + "Critical Hit!")
        return damage

    # Prints weapon stats
    def get_description(self):
        return (f"""Weapon Name: {self.name}
        Weapon Max Damage: {self.max_damage}
        Weapon Min Damage: {self.min_damage}
        Weapon Critical Hit Chance: """ + (self.crit_chance * 100) + f"""%
        Weapon Description: {self.description}""")
