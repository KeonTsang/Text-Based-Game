from weapons.weapon import Weapon

fistDescription = """Your bare fists.
Fists have a higher chance of dealing a critical blow."""
axeDescription = """A heft axe with a sharp, pointy edge capable of dealing high damage."""

fist = Weapon("Fist", 5, 4, 0.05, fistDescription)
axe = Weapon("Axe", 10, 7, 0.025, axeDescription)

