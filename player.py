import health
from items import *
from rooms import rooms
from items import item_init

inventory = []
player_health = 100
karma = 0
current_weapon = item_init.fist

# Start game at the reception
current_room = rooms["Hyperbaric Chamber"]

def display_health():
    print(health.genHealthBar(player_health))
