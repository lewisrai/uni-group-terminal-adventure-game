#first floor of ABACWS
#Should be 4 rooms:
#
#   d  e
#   |  |
#   c--a--b
#
# a: lobby, b: lecture theatre, c: mathematical amusements, d: social room (empty?), e: transition
# enter to a

from items.item_class import Item as ItemClass
from items.items import *

from minigames.minigames import *


def get_map_ascii(current_room): #current_room here should just be the name for the rooms dict
    a = " "
    b = " "
    c = " "
    d = " "

    w1 = " "
    w2 = " "
    x1 = " "
    x2 = " "
    y = " "
    match current_room:
        case "The Shadowed Lobby of Abacws":
            a = "X"
        case "The Lecture Hall of Arcane Wisdom":
            b = "X"
        case "The Chamber of Mathematical amusements":
            c = "X"
        case "Room of Social Conundrums":
            d = "X"
        case "The Secret Chamber":
            w1 = "_"
            w2 = "_"
            x1 = "X"
            x2 = "|"
            y = "▔"
        case _:
            pass
        #if current_room is "Transition", the map will be closed

    return[ #10 down, 20 across, https://www.w3.org/TR/xml-entity-names/025.html
        [" ","_","_","_",w1 ,w2 ," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#1
        ["|"," "," "," ","|",x1 ,x2 ," "," "," ","┌","┐"," "," "," "," "," "," "," "," "],#2
        ["|"," ", d ," ","|", y ," "," "," ","┌"," ","|"," "," "," "," "," "," "," "," "],#3
        ["|","_","_","_","|"," "," "," ","┌","_","_","|"," "," "," "," "," "," "," "," "],#4
        [" "," ","|"," "," "," "," "," "," ","|"," "," "," "," "," ","_"," "," "," "," "],#5
        [" ","_","⊥","_"," "," "," "," ","_","⊥","_"," "," "," ","|","_","|","_"," "," "],#6
        ["|"," "," "," ","|"," "," ","|"," "," "," ","|"," "," ","|"," "," "," ","|"," "],#7
        ["|"," ", c ," ","|","-","-","|"," ", a ," ","|","-","-","|"," ", b ," ","|"," "],#8
        ["|","_","_","_","|"," "," ","|","_","_","_","|"," "," ","|","_","_","_","|"," "],#9
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]#10
       #["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K"] 
    ]


room_lobby = {
    "name": "The Shadowed Lobby of Abacws",
    "short_name": "Lobby of ABACWS",
    "description":
    """Welcome to the Abacws Lobby, where secrets pulse in the air
and enigmatic puzzles await around every corner.
Neon-lit signs cast an otherworldly glow, and cryptic artifacts decorate the space.
It's a place of intrigue and mystery, challenging you to unravel its enigmas
and step into the tower's mysterious world.""",

    "top_of_stairs": True,

    "exits": {"east": "Lecture", "west": "Amusements"},

    "locked_exits": [["north", "Transition", ItemClass(item_deodrant), "There is a forth year mage blocking the stairs, "]],

    "puzzle": [],

    "items": []
}

room_lecture = {
    "name": "The Lecture Hall of Arcane Wisdom",
    "short_name": "Lecture Hall",
    "description":
    """Step into the heart of the tower's knowledge, where secrets are unveiled,
and arcane wisdom is passed down through the ages. 
This hallowed hall is a realm of enlightenment, shrouded in mystery,
where seekers of hidden truths gather to unlock the secrets of Abacws Tower.""",

    "exits": {"west": "Lobby"},

    "locked_exits": [],

    "puzzle": [higher_lower,
               0,
               ItemClass(item_sledgehammer),
               "A python program seems to be running from the lecturers' laptop...",
               False], #the minigame, index(leave as 0 unless riddle), item reward, completetion status

    "items": [ItemClass(item_advanced_sword)]
}

room_amusements = {
    "name": "The Chamber of Mathematical amusements",
    "short_name": "Math Amuse",
    "description":
    """You enter the Chamber of Mathematical Amusements,
you scratch your head as you look around the room,
the walls are adorned with arcane symbols, this room exudes an air of mystery.""",

    "exits": {"north": "Social", "east": "Lobby"},

    "locked_exits": [],

    "puzzle": [riddle,
               0,
               ItemClass(item_deodrant),
               "On the magical blackboard at the front of the room is an interesting conundrum,\nfit for an adventurer...",
               False], #the minigame, index(leave as 0 unless riddle), item reward, completetion status

    "items": []
}

room_social = {                                 #INCOMPLETE
    "name": "Room of Social Conundrums",
    "short_name": "Social Room",
    "description":
    """Welcome to the room of Social Conundrums!
Thats what the sign on the door says at least, the room itself is completly empty.""",

    "exits": {"south": "Amusements"},

    "locked_exits": [["east", "Secret", ItemClass(item_sledgehammer), "There is a crumbling wall to the "]],

    "puzzle": [],

    "items": []
}

room_transition = { #this room should be in every floor, used for the movement up to the next floor
    "name": "Transition to First Floor",#update later?
    "short_name": "Stairs",
    "description":
    """You take a deep breath, before bravely climbing the stairs to the first floor""",

    "exits": {}, #no exits, code in main.py should move to the next floor

    "locked_exits": [],

    "puzzle": [],

    "items": [] #no items, none needed in a transition room
}

room_secret = {
    "name": "The Secret Chamber",
    "short_name": "Secret Chamber",
    "description": "You've discovered the hidden Secret Chamber. It's filled with treasures and ancient artifacts.",

    "exits": {"west": "Social"},  # You can specify the exit to the Lobby or any other room.

    "locked_exits": [],

    "puzzle": [],

    "items": [ItemClass(item_healing), ItemClass(item_balcony_key)]
}

rooms = { #put the first room the player will enter on a floor at the top of this list
    "Lobby": room_lobby,
    "Lecture": room_lecture,
    "Amusements": room_amusements,
    "Social": room_social,
    "Secret": room_secret,
    "Transition": room_transition
}
