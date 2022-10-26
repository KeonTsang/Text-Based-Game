import health
import rooms
from items import item_init

inventory = []
player_health = 100
max_health = 100
karma = 0
current_weapon = item_init.raygun
has_unlocked_nuclear_room = False
has_unlocked_boss = False

# Start game at the reception
current_room = rooms.rooms["Hyperbaric Chamber"]

def display_health():
    print(health.genHealthBar(player_health, False))

def display_inverse_health():
    print(health.genHealthBar(player_health, True))