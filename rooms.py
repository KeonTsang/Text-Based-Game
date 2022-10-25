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

    "exits": {"west": "Med Bay"},

    "items": [item_init.map],

    "monsters": [],

    "discovered" : False
}

MED_BAY = {
    "name": "Med Bay",

    "description":
    """
    This seems to be the medical bay for the facility.
    Although it seems void of human life, there is the undeniable stench of death.
    """,

    "exits": {"east": "Hyperbaric Chamber", "west": "Testing Area"},

    "items": [],

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

    "exits": {"east": "Med Bay"},

    "items": [item_init.keycard],

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

    "exits": {"south": "Med Bay", "west": "Pyrotechnics Lab"},

    "items": [],

    "monsters": [],

    "discovered" : False
}

PYROTECHNICS_LAB = {
    "name": "Pyrotechnics Lab",

    "description":
    """
    This is the pyrotechnics lab. There are a few shelves with various chemicals on them.
    There is a large, red, button on the wall. It is labelled: "In case of sentient fire - press".
    """,

    "exits": {"east": "Reception Area"},

    "items": [],

    "monsters": [],

    "discovered" : False
}

NUCLEAR_TESTING_SITE = {
    "name": "Nuclear Testing Site",

    "description":
    """
    This seems to be a nuclear testing site. The room is filled with various nuclear devices.
    They seem to resemble weapons, but you're unsure of their purpose.
    There is a hazmat suit on behind a glass case.
    """,

    "exits": {"south": "Reception Area"},

    "items": [],

    "monsters": [],

    "discovered" : False
}

rooms = {
    "Hyperbaric Chamber": HYPERBARIC_CHAMBER,
    "Med Bay": MED_BAY,
    "Testing Area": TESTING_AREA,
    "Reception Area": RECEPTION_AREA,
    "Pyrotechnics Lab": PYROTECHNICS_LAB,
    "Nuclear Testing Site": NUCLEAR_TESTING_SITE
}

