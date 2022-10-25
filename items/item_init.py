from items.weapon import Weapon
from items.item import Item

# Weapons

fist = Weapon("Fist", 4, 2, 0.20, """Your bare fists.\nFists have a higher chance of dealing a critical blow.""")
stethoscope = Weapon("Stethoscope", 8, 4, 0.10,"A bunsen burner that can shoot fire, capable of dealing considerable damage")
centrifuge = Weapon("Centrifuge", 10, 7, 0.05,"A bunsen burner that can shoot fire, capable of dealing considerable damage")
testtube = Weapon("Test Tube Rocket", 12, 10, 0.05,"A bunsen burner that can shoot fire, capable of dealing considerable damage")
bunsen = Weapon("Bunsen burner", 15, 8, 0.15,"A bunsen burner that can shoot fire, capable of dealing considerable damage")

# Items

map = Item("map", "This seems to be a map of the facility. It's a bit worn and tattered, but it's still readable.")
keycard = Item("keycard", "This is a keycard. It seems to be a standard issue keycard for the facility.")
