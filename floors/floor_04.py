#floor 4 - Fprth playable floor enter in tech support
#
#
#                  e
#                  |
#                  d
#                  |
#              b---a---c
#
#a Tech support
#b kirill statue
#c cleaning room
#d pre boss
#e boss

from items.item_class import Item as ItemClass
from items.items import *

from minigames.minigames import *

def get_map_ascii(current_room): #current_room here should just be the name for the rooms dict
    a = " "
    b = " "
    c = " "
    d = " "
    e = " "

    match current_room:
        case "Technology Support Office":
            a = "X"
        case "The Great Kirill Statue":
            b = "X"
        case "The Dungeon of Cleaning":
            c = "X"
        case "Utility Cupboard":
            d = "X"
        case "Kirill's Waiting Room":
            e = "X"
        case _:
            pass
        #if current_room is "Transition", the map will be closed

    return[ #10 down, 20 across, https://www.w3.org/TR/xml-entity-names/025.html
        [" "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],#1
        [" "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," "," "," "],#2
        [" "," "," "," "," "," "," "," "," ","⊥"," "," "," "," "," "," ","_"," "," "," "],#3
        [" "," "," "," "," "," "," "," ","|", e ,"|"," "," "," "," ","|", d ,"|"," "," "],#4
        [" "," "," "," "," "," "," "," ","|","_","|"," "," "," "," ","|","_","|"," "," "],#5
        [" ","_","_","_"," "," "," "," ","_","⊥","_"," "," "," "," ","_","⊥","_"," "," "],#6
        ["|"," "," "," ","|"," "," ","|"," "," "," ","|"," "," ","|"," "," "," ","|"," "],#7
        ["|"," ", b ," ","|","-","-","|"," ", a ," ","|","-","-","|"," ", c ," ","|"," "],#8
        ["|","_","_","_","|"," "," ","|","_","_","_","|"," "," ","|","_","_","_","|"," "],#9
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]#10
       #["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K"] 
    ]


room_tech_support = {
    "name": "Technology Support Office",
    "short_name": "Tech",
    "description":
    """Deep in the heart of a the tower, the "Dark Office of Enchanted Support",
is a haven where even evil wizards turn to resolve their magical tech troubles.
The two tech support wizards, MJ and Simon are here.""",

    "top_of_stairs": True,#only for start room

    "exits": {"east": "Cleaning", "west": "Statue"},

    "locked_exits": [["north", "Waiting Room", ItemClass(item_antifreeze), "The tech support wizards are encased in ice to the "]],

    "puzzle": [],

    "items": [] #discuss with team
}

room_kirill_statue = {
    "name": "The Great Kirill Statue",
    "short_name": "Statue",
    "description":
    """An imposing statue stands tall, depicting the formidable dark wizard, Kirill.
It seems to made from a material that radiates with dark power,
theatening to corrupt even the purest minds: Kirillium...

Was this how the once pure and just wizard fell to the darkness?""",

    "exits": {"east": "Tech"},

    "locked_exits": [],

    "puzzle": [riddle,
               1,
               ItemClass(item_kirillium_sword),
               "There is a (magical) tablet at the base of the statue, inviting you to investigate...",
               False], #the minigame, index(leave as 0 unless riddle), item reward, completetion status

    "items": [] #change to puzzle
}

room_dungeon_of_cleaning = {
    "name": "The Dungeon of Cleaning",
    "short_name": "Cleaning",
    "description":
    """The cleaning room harbors an array of enchanted brooms, mops, and sentient feather dusters.
Glistening crystals cast a shimmering light upon the artifacts of tidiness,
revealing a treasure trove of tools for vanquishing grime and dirt.""",

    "exits": {"west": "Tech"},

    "locked_exits": [["north", "Cupboard", ItemClass(item_boots), "There is a (flimsy) locked utility cupboard to the "]],

    "puzzle": [],

    "items": [ItemClass(item_antifreeze)] #discuss with team
}

room_utility_cupboard = {
    "name": "Utility Cupboard",
    "short_name": "Cupboard",
    "description":
    """The utility cupboard contains a wide variaty of useless items...
...
But out of the corner of you eye, you see a trinket of much value to your quest!""",

    "exits": {"south": "Cleaning"},

    "locked_exits": [],

    "puzzle": [],

    "items": [ItemClass(item_batteries), ItemClass(item_box_set)] #discuss with team
}

room_pre_boss = {    #check with group
    "name": "Kirill's Waiting Room",#update later?
    "short_name": "Waiting Room",
    "description":
    """The dark wizards waiting room...
    
It contains a shield, and a shoe locker...?""",

    "exits": {"south": "Tech"}, #room to go to kirill

    "locked_exits": [["north", "Transition", ItemClass(item_batteries), "There is an automatic door with no power to the "]],

    "puzzle": [],

    "items": [ItemClass(item_boots)]
}

room_transition = {    #check with group
    "name": "Kirill...",#update later?
    "short_name": "Boss Transition",
    "description":
    """.""",

    "exits": {}, #room to go to kirill

    "locked_exits": [],

    "puzzle": [],

    "items": [] #no items, none needed in a transition room
}
rooms = {
    "Tech" : room_tech_support,
    "Statue" : room_kirill_statue,
    "Cleaning" : room_dungeon_of_cleaning,
    "Cupboard" : room_utility_cupboard,
    "Waiting Room" : room_pre_boss,
    "Transition": room_transition
}
