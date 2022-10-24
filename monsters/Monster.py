from abc import abstractmethod, ABCMeta
import random
import math
import game_parser
from colorama import Fore

import player


class Monster:
    __metaclass__ = ABCMeta

    def __init__(self, name, max_hp, max_damage, min_damage, miss_chance):
        self.name = name
        self.health = max_hp
        self.max_hp = max_hp
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.miss_chance = miss_chance
        self.phase = 1
        self.isSpare = False

    def __init__(self, name, max_hp, max_damage, miss_chance):
        self.__init__(self, name, max_hp, max_damage, max_damage, miss_chance)

    # Returns damage value dealt by entity
    def attack(self):
        damage = 0 if random.random < self.miss_chance else random.randint(self.min_damage, self.max_damage)
        if damage == 0:
            print(f"{self.name} tried to attack you, but missed!")
        else:
            print(f"{self.name} attacked you for {damage} hit points!")
            player.player_health -= damage

    # Damages this entity by whatever amount
    def damage(self, damage):
        self.health -= damage

    # Returns if the monster is still alive
    def isAlive(self):
        return self.health > 0

    # Sets the current battle phase
    def setPhase(self, phase):
        self.phase = phase

    def getPhase(self):
        return self.phase

    def setSpare(self, sparede):
        self.isSpare = True

    # Displays a health bar which can vary in size depending on monster's max Hp
    def display_health(self, health):
        healthBar = (Fore.GREEN if health > 40 else Fore.YELLOW if health > 20 else Fore.RED) + "Health: ["
        for i in range(0, (math.floor(self.health) + 1)):
            healthBar += " " if i == 0 and health == 0 else "#" if i <= math.floor(health / 2) else " "
        healthBar += f"] {health}/100" + Fore.RESET
        return healthBar

    # Takes in inputs from user
    def command_reader(self):
        command = input(f"ATTACK {self.name}\nTALK to {self.name}\nuse an Action on {self.name}\nSPARE {self.name}")
        self.execute_command(game_parser.normalise_input(command))

    # Command parser
    def execute_command(self, command):
        if 0 == len(command):
            return
        if command[0] == "spare":
            self.execute_spare()
        elif command[0] == "talk":
                self.execute_talk()
        elif command[0] == "attack":
                self.execute_attack()
        elif command[0] == "action":
                self.execute_action()
        else:
            print(f"'{command[0]}' -> Makes no sense.")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)

    @abstractmethod
    def execute_spare(self):
        pass

    @abstractmethod
    def execute_talk(self):
        pass

    @abstractmethod
    def execute_attack(self):
        pass

    @abstractmethod
    def execute_action(self):
        pass

    # Battle Phases
    @abstractmethod
    def phase1(self):
        pass

    @abstractmethod
    def phase2(self):
        pass

    @abstractmethod
    def phase3(self):
        pass

    @abstractmethod
    def spare(self):
        pass