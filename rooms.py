from items import *
from map import *
from items import item_init

HYPERBARIC_CHAMBER = {
    "name": "Hyperbaric Chamber",

    "description":
    """
    This is where you awoke - there appears to be a chamber of some sort in the centre of the room.
    It's cold and damp in here, and you can hear the sound of water dripping from somewhere.
    Although nearly barren, there in an odd, life-like, pulse in the air.
    """,

    "exits": {"west": "Main Floor"},

    "items": [item_init.map],

    "monsters": [],

    "discovered" : False
}

MAIN_FLOOR = {
    "name": "Main Floor",

    "description":
    """
    This is the main floor of the facility. It is in pristine condition.
    There are a few doors leading off in different directions. There is no sign of human life.
    The eery silence frightens you.
    """,

    "exits": {"east": "Hyperbaric Chamber", "west": "Testing Area"},

    "items": [item_init.keycard],

    "monsters": [],

    "discovered" : False
}

TESTING_AREA = {
    "name": "Testing Area",

    "description":
    """
    This seems to be the place where experiments take place.
    The nature of these experiements is unknown to you.
    """,

    "exits": {"east": "Main Floor"},

    "items": [],

    "monsters": [],

    "discovered" : False
}

RECEPTION_AREA = {
    "name": "Reception Area",

    "description":
    """
    This is the reception area. There is a desk with a computer on it.
    There is a sign on the desk that reads: "Welcome to the facility. Please sign in."
    """,

    "exits": {"south": "Main Floor"},

    "items": [],

    "monsters": [],

    "discovered" : False
}


rooms = {
    "Hyperbaric Chamber": HYPERBARIC_CHAMBER,
    "Main Floor": MAIN_FLOOR,
    "Testing Area": TESTING_AREA,
    "Reception Area": RECEPTION_AREA
}

