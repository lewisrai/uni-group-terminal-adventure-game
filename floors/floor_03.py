def get_map_ascii(current_room): #current_room here should just be the name for the rooms dict
    a = " " #Landing
    match current_room:
        case "Maths Floor Landing":
            a = "X"
        case _:
            pass
        #if current_room is "Transition", the map will be closed

    return[ #10 down, 20 across, https://www.w3.org/TR/xml-entity-names/025.html
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],#1
        [" "," "," "," "," "," "," "," "," "," ","┌","┐"," "," "," "," "," "," "," "," "],#2
        [" ","!"," ","!"," ","!"," "," "," ","┌"," ","|"," ","!"," ","!"," ","!"," "," "],#3
        [" "," "," "," "," "," "," "," ","┌","_","_","|"," "," "," "," "," "," "," "," "],#4
        [" ","!"," ","!"," ","!"," "," "," ","|"," "," "," ","!"," ","!"," ","!"," "," "],#5
        [" "," "," "," "," "," "," "," ","_","⊥","_"," "," "," "," "," "," "," "," "," "],#6
        [" ","!"," ","!"," ","!"," ","|"," "," "," ","|"," ","!"," ","!"," ","!"," "," "],#7
        [" "," "," "," "," "," "," ","|"," ", a ," ","|"," "," "," "," "," "," "," "," "],#8
        [" ","!"," ","!"," ","!"," ","|","_","_","_","|"," ","!"," ","!"," ","!"," "," "],#9
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]#10
       #["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K"] 
    ]

room_landing = {
    "name": "Maths Floor Landing",
    "short_name": "Landing",
    "description":
    """You arrive on the maths floor, leave as soon as you can...""",

    "top_of_stairs": True,#only for start room

    "exits": {"north": "Stairs"},

    "locked_exits": [],

    "puzzle": [],

    "items": []
}

room_transition = {
    "name": "Stairs to 3rd Floor",
    "short_name": "Stairs",
    "description":
    """You take a deep breath, before bravely climbing the stairs to the third floor""",

    "exits": {},

    "locked_exits": [],

    "puzzle": [],

    "items": []
}


rooms = { #put the first room the player will enter on a floor at the top of this list
    "Landing": room_landing,
    "Stairs": room_transition
}
