#outside the dark tower of ABACWS
#Should be one room, contains the fallen grand wizard, CHRIS, who gives the player the quest (Chris should be in another file, not created yet (as of 3pm on the 16th))

from items.item_class import Item as ItemClass
from items.items import *

def get_map_ascii(current_room): #current_room here should just be the name for the rooms dict
    a = " "
    match current_room:
        case "ABACWS Entrance":
            a = "X"
        case _:
            pass
        #if current_room is "Transition", the map will be closed

    return[ #10 down, 20 across, https://www.w3.org/TR/xml-entity-names/025.html
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#1
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#2
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#3
        ["_","_","_","_","_","_","_","_","_","O","_","_","_","_","_","_","_","_","_","_"],#4
        [" "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],#5
        [" "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],#6
        [" "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],#7
        [" "," "," "," "," "," "," "," "," ", a ," "," "," "," "," "," "," "," "," "," "],#8
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#9
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]#10
       #["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K"] 
    ]

room_outside = {
    "name": "ABACWS Entrance",
    "short_name": "ABACWS Entrance",

    "description":
    """You approach the looming entrance of the Dark Tower of ABACWS,
you can hear the screams of the damned souls within, doomed to a sleepless existance.
The quest Chris gave you leads to here, and as promised, he left some starting items...""",

    "exits": {},

    "locked_exits": [["north", "Transition", ItemClass(item_abacws_key), "There is a locked exit to the "]], #"direction from this room", "rooms name", "item needed / boss or whatever"
    #"locked_exits": [],

    "puzzle": [],

    "items": [ItemClass(item_basic_sword), ItemClass(item_basic_shield), ItemClass(item_abacws_key)]
}

room_transition = { #this room should be in every floor, used for the movement up to the next floor
    "name": "Front Door of ABACWS",#update later?
    "short_name": "ABACWS Enterance",

    "description":
    """You take a deep breath, before bravely entering through the (very inefficient) revolving doors""",

    "exits": {}, #no exits, code in main.py should move to the next floor

    "locked_exits": [],

    "puzzle": [],

    "items": [] #no items, none needed in a transition room
}

rooms = { #put the first room the player will enter on a floor at the top of this list
    "Entrance": room_outside,
    "Transition": room_transition
}
