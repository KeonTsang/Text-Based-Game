from abc import abstractmethod, ABCMeta
import random
import math
from colorama import Fore

class Monster:
    __metaclass__ = ABCMeta

    def __init__(self, name, max_hp, max_damage, min_damage):
        self.name = name
        self.health = max_hp
        self.max_hp = max_hp
        self.max_damage = max_damage
        self.min_damage = min_damage

    def __init__(self, name, max_hp, max_damage):
        self.name = name
        self.health = max_hp
        self.max_hp = max_hp
        self.max_damage = max_damage
        self.min_damage = 0

    # Returns damage value dealt by entity
    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

    # Damages this entity by whatever amount
    def damage(self, damage):
        self.health -= damage

    # Displays a health bar which can vary in size depending on monster's max Hp
    def display_health(self, health):
        healthBar = (Fore.GREEN if health > 40 else Fore.YELLOW if health > 20 else Fore.RED) + "Health: ["
        for i in range(0, (math.floor(self.health) + 1)):
            healthBar += " " if i == 0 and health == 0 else "#" if i <= math.floor(health / 2) else " "
        healthBar += f"] {health}/100" + Fore.RESET
        return healthBar