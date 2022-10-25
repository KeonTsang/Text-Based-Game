from items.weapon import Weapon
from items.item import Item

# Weapons

fist = Weapon("fist", "fist", 4, 2, 0.35, """Your bare fists.\nFists have a higher chance of dealing a critical blow.""")
stethoscope = Weapon("stethoscope", "stethoscope", 6, 4, 0.20, "A small stethoscope, which is capable of dealing some minor damage to enemeies")
centrifuge = Weapon("centrifuge", "centrifuge", 10, 7, 0.10, "A hefty centrifuge that could potentially be used to whack someone round the head with")
testtube = Weapon("testtube", "test tube rocket", 12, 10, 0.05, "A set of Test Tubes that can be fired much like a missile at whoever stands in your way")
bunsen = Weapon("bunsen", "bunsen burner", 17, 10, 0.15, "A bunsen burner that spews endless amounts of fire, despite not having a fuel tank")
raygun = Weapon("raygun", "nuclear raygun", 50, 30, 0.30, "The test weapon from this secret facility, it appears to fire some sort of nuclear laser beam")

# Items

map = Item("map", "map", "This seems to be a map of the facility. It's a bit worn and tattered, but it's still readable.")
keycard = Item("keycard", "keycard", "This is a keycard. It seems to be a standard issue keycard for the facility. A door in the medical bay could be opened with it.")
