from abc import abstractmethod, ABCMeta
import random
import math
import game_parser
from colorama import Fore

import player


class Monster:
    __metaclass__ = ABCMeta

    description = ""

    def __init__(self, name, max_hp, max_damage, min_damage, miss_chance, colour, item):
        self.name = name
        self.health = max_hp
        self.max_hp = max_hp
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.miss_chance = miss_chance
        self.phase = 1
        self.isSpare = False
        self.colour = colour
        self.item = item

    # Returns damage value dealt by entity
    def attack(self):
        if not self.isSpared():
            damage = 0 if random.random() < self.miss_chance else random.randint(self.min_damage, self.max_damage)
            if damage == 0:
                print(f"\n{self.name} tried to attack you, but missed!")
            else:
                print(f"\n{self.name} attacked you for {damage} hit points!")
                player.player_health -= damage

    # Damages this entity by whatever amount
    def damage(self, damage):
        self.health -= damage
        if self.health < 1:
            print(f"\nYou killed {self.name}")
            player.karma -= 1
            print("Your max health increased by " + str(math.floor(player.max_health * 0.1)) + "!")
            player.max_health = math.floor(player.max_health * 1.1)
            player.player_health = player.max_health
            player.current_room["items"].append(self.item)
            player.current_room["monsters"].remove(self)

    # Returns if the monster is still alive
    def isAlive(self):
        return self.health > 0

    # Sets the current battle phase
    def setPhase(self, phase):
        self.phase = phase

    def getPhase(self):
        return self.phase

    def setSpared(self):
        self.isSpare = True

    def isSpared(self):
        return self.isSpare

    # Displays a health bar which can vary in size depending on monster's max Hp
    def display_health(self):
        health = self.health
        health_bar = (Fore.GREEN if health > (self.max_hp * 0.4) else Fore.YELLOW if health > (
                    self.max_hp * 0.2) else Fore.RED) + f"{self.name}'s Health: ["
        for i in range(0, (math.floor(self.max_hp / 2) + 1)):
            health_bar += " " if i == 0 and health == 0 else "#" if i <= math.floor(health / 2) else " "
        health_bar += f"] {health}/{self.max_hp}" + Fore.RESET
        print(health_bar)

    # Takes in inputs from user
    def command_reader(self):
        notValidCommand = True
        while notValidCommand:
            command = input(Fore.RED + "\n(!)" + Fore.RESET + f" ATTACK {self.name}\n" +
                            Fore.CYAN + "(?)" + Fore.RESET + f" TALK to {self.name}\n" +
                            Fore.YELLOW + "(*)" + Fore.RESET + f" use an ACTION on {self.name}\n" +
                            Fore.GREEN + "(~)" + Fore.RESET + f" SPARE {self.name}\n\n")
            notValidCommand = self.execute_command(game_parser.normalise_input(command))

    # Command parser
    def execute_command(self, command):

        if 0 == len(command):
            print("Sorry I didn't understand that!\n")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return True
        if command[0] == "spare":
            self.execute_spare()
            return False
        elif command[0] == "talk":
            self.execute_talk()
            return False
        elif command[0] == "attack":
            self.execute_attack()
            return False
        elif command[0] == "action":
            self.execute_action()
            return False
        else:
            print(f"'{command[0]}' -> Makes no sense.")
            input(Fore.LIGHTRED_EX + "(•) " + Fore.LIGHTYELLOW_EX + "Press enter to continue..." + Fore.RESET)
            return True


    # Battle Phases
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
            player.player_health = player.max_health
        else:
            print(f"You cannot spare {self.name} yet!")

    @abstractmethod
    def execute_talk(self):
        pass

    @abstractmethod
    def execute_attack(self):
        pass

    @abstractmethod
    def execute_action(self):
        pass

    @abstractmethod
    def spare(self):
        pass

    @abstractmethod
    def print_description(self):
        pass