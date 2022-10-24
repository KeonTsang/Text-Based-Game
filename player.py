from items import *
from rooms import rooms
from weapons import weapon_init

inventory = []
player_health = 100
karma = 0
current_weapon = weapon_init.fist

# Start game at the reception
current_room = rooms["Hyperbaric Chamber"]

