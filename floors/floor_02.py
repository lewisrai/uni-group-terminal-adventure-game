#first floor of ABACWS
#Should be 4 rooms:
#
#   e  
#   |  
#   c--a--b
#         |
#         d
#
# a: Comp lab, b: Dungeon, c: Hall of comp, d: Balcony (secret), e: transition
# enter to a

#from items import *

from items.item_class import Item as ItemClass
from items.items import *

from minigames.minigames import *

def get_map_ascii(current_room): #current_room here should just be the name for the rooms dict
    a = " " #comp lab
    b = " " #dungeon
    c = " " #hall of comp
    d = " " #balcony (locked)
    match current_room:
        case "Computer Science Lab":
            a = "X"
        case "Dungeon of Theodosius":
            b = "X"
        case "Hall of Computing":
            c = "X"
        case "Lecture Room Balcony":
            d = "X"
        case _:
            pass
        #if current_room is "Transition", the map will be closed

    return[ #10 down, 20 across, https://www.w3.org/TR/xml-entity-names/025.html
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#1
        [" "," "," ","┌","┐"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#2
        [" "," ","┌"," ","|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#3
        [" ","┌","_","_","|"," "," "," "," "," "," "," "," "," "," "," ","_","_","_"," "],#4
        [" "," ","|"," "," "," "," "," "," "," "," "," "," "," "," ","|"," "," "," ","|"],#5
        [" ","_","⊥","_"," "," "," "," ","_","_","_"," "," ","|","-","|"," ", b ," ","|"],#6
        ["|"," "," "," ","|"," "," ","|"," "," "," ","|"," ","|"," ","|","_","_","_","|"],#7
        ["|"," ", c ," ","|","-","-","|"," ", a ," ","|","-","|"," "," ","_","I","_"," "],#8
        ["|","_","_","_","|"," "," ","|","_","_","_","|"," "," "," ","|"," ", d ," ","|"],#9
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|","_","_","_","|"]#10
       #["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K"] 
    ]

room_lab = {
    "name": "Computer Science Lab",
    "short_name": "Lab",
    "description":
    """The confusing misnomer of 'computer Science' shows best in a computer science lab.
Despite trying your best to inspect and understand the arcane machines surrounding you,
You can come to no conclusion other than magic.""",

    "top_of_stairs": True,#only for start room

    "exits": {"west": "Hall"},

    "locked_exits": [["east", "Dungeon", ItemClass(item_key_card), "A heavy door with a keycard reader lies to the "]],

    "puzzle": [riddle,
               2,
               ItemClass(item_key_card),
               "You find a safe stowed behind the lecturer's desk...",
               False], #the minigame, index(leave as 0 unless riddle), item reward, completetion status

    "items": [ItemClass(item_advanced_shield)]
}

room_dungeon = {
    "name": "Dungeon of Theodosius",
    "short_name": "Dungeon",
    "description":
    """A dark and musty chamber, where Theodosius is rumored to haunt the magical chains. 
It's a crypt of brooms, mops, and mysterious stains.""",

    "exits": {"west": "Lab"},

    "locked_exits": [["south", "Balcony", ItemClass(item_balcony_key), "A door leading to the balcony lies to the "]],

    "puzzle": [],

    "items": [ItemClass(item_idol)]
}

room_hall = {
    "name": "Hall of Computing",
    "short_name": "Hall",
    "description":
    """A extravagant hall lays before you, full with statues of great magical artifacts of computing.
Theres 4 machines that have numbers imposed onto their bases, maybe a sequence can be made from this?
Could you have to order them from oldest to newest for some arcane reason?

The Pascaline: 6
ENIAC: 4
The Stepped Reckoner: 2
The Abacus: 7""",#7624

    "exits": {"east": "Lab"},

    "locked_exits": [["north", "Transition", ItemClass(item_idol), "An empty pedestal linked to the exit "]],

    "puzzle": [rock_paper_scissors,
               0,
               ItemClass(item_firewall),
               "A magical terminal on one of the aging machines comes to life...",
               False], #the minigame, index(leave as 0 unless riddle), item reward, completetion status

    "items": []
}

room_balcony = {
    "name": "Lecture Room Balcony",
    "short_name": "Balcony",
    "description":
    """You find yourself atop the balcony overlooking the lecture hall a floor below.""",

    "exits": {"north": "Dungeon"},

    "locked_exits": [],

    "puzzle": [],

    "items": [ItemClass(item_chair), ItemClass(item_backpack)]
}

room_transition = {
    "name": "Transition to Second Floor",#update later?
    "short_name": "Stairs",
    "description":
    """You take a deep breath, before bravely climbing the stairs to the second floor""",

    "exits": {}, #no exits, code in main.py should move to the next floor

    "locked_exits": [],

    "puzzle": [],

    "items": [] #no items, none needed in a transition room
}

rooms = { #put the first room the player will enter on a floor at the top of this list
    "Lab": room_lab,
    "Dungeon": room_dungeon,
    "Hall": room_hall,
    "Balcony": room_balcony,
    "Transition": room_transition
}
