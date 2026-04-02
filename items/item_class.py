# This is the items class it takes the items from the items.py and acts as a blueprint to build those items 
class Item:
    def __init__(self, dict_in):
        self.name = dict_in["name"]
        self.description = dict_in["description"]
        self.damage = dict_in["damage"]
        self.defense = dict_in["defense"]
        self.uses = dict_in["uses"]
        self.heal = dict_in["heal"]
