import math

class Weapon:

    def __init__(self, name, max_damage, min_damage, crit_chance, description):
        self.name = name
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.crit_chance = crit_chance
        self.desciription = description

    def attack(self):
        if math.random < self.crit_chance:
            damage = math.randInt(self.min_damage, self.max_damage) * 2
        else:
            damage = math.randInt(self.min_damage, self.max_damage) * 2
        return damage