from items.weapon import Weapon
from items.item import Item

# Weapons

fist = Weapon("Fist", 5, 4, 0.05, """Your bare fists.
Fists have a higher chance of dealing a critical blow.""")
axe = Weapon("Axe", 10, 7, 0.025, """A heft axe with a sharp, pointy edge capable of dealing high damage.""")

# Items

map = Item("map", """This seems to be a map of the facility. It's a bit worn and tattered, but it's still readable.""")
keycard = Item("keycard", """This is a keycard. It seems to be a standard issue keycard for the facility.""")