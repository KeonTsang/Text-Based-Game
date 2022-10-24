import random


class Weapon:

    def __init__(self, name, max_damage, min_damage, crit_chance, description):
        self.name = name
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.crit_chance = crit_chance
        self.description = description

    # Returns damage dealt by weapon
    def attack(self):
        if random.random() < self.crit_chance:
            damage = random.randint(self.min_damage, self.max_damage) * 2
        else:
            damage = random.randint(self.min_damage, self.max_damage) * 2
        return damage

    # Prints weapon stats
    def stats(self):
        print(f"""Weapon Name: {self.name}
        Weapon Max Damage: {self.max_damage}
        Weapon Min Damage: {self.min_damage}
        Weapon Critical Hit Chance: """ + (self.crit_chance * 100) + f"""%
        Weapon Description: {self.description}""")
