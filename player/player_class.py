# bm stands for boss mode where the player is fighting Kirill
#player class used to create the instance of a player object, and used to carry out actions to and from the player class

class Player:
    def __init__(self):
        self.max_health = 99
        self.health = 99
        self.defense = 3
        self.bass_defense = 3
        self.inventory = []
        self.max_inventory_slots = 4
        self.corrupted = False

        self.bm_position_x = 2
        self.bm_position_y = 4
        self.bm_previous_move = ""
        self.bm_block_next_attack = False

    def add_to_inventory(self, item):
        # Check if there is a space left and return if it was successful
        if item.name == "Backpack":
            self.max_inventory_slots = 6
            return True
        elif len(self.inventory) < self.max_inventory_slots:
            self.inventory.append(item)
            if item.name.find("Kirillium") == 0:
                self.corrupted = True
            return True
        else:
            return False

    def remove_from_inventory(self, item_name):
        for item in self.inventory:
            if item_name == item.name:
                self.inventory.remove(item)
                return True

        return False

    def bm_move(self, user_input_word_list, kirill_position_x, kirill_position_y):
        match user_input_word_list[1]:
            case "north":
                if self.bm_position_y > 0 and (self.bm_position_x != kirill_position_x or self.bm_position_y - 1 != kirill_position_y):
                    self.bm_position_y -= 1
                    self.bm_previous_move = "move"
            case "east":
                if self.bm_position_x < 4 and (self.bm_position_x + 1 != kirill_position_x or self.bm_position_y != kirill_position_y):
                    self.bm_position_x += 1
                    self.bm_previous_move = "move"
            case "south":
                if self.bm_position_y < 4 and (self.bm_position_x != kirill_position_x or self.bm_position_y + 1 != kirill_position_y):
                    self.bm_position_y += 1
                    self.bm_previous_move = "move"
            case "west":
                if self.bm_position_x > 0 and (self.bm_position_x - 1 != kirill_position_x or self.bm_position_y != kirill_position_y):
                    self.bm_position_x -= 1
                    self.bm_previous_move = "move"

    def bm_check_item_uses(self):
        for item in self.inventory:
            if item.uses == 0:
                self.inventory.remove(item)

    def bm_use_item(self, user_input_word_list):
        user_input_word_list = user_input_word_list[1:]
        name_of_item = " ".join(user_input_word_list)
        for item in self.inventory:
            if name_of_item == item.name.lower():
                item.uses -= 1
                if name_of_item.find("shield") != -1:
                    self.defense += item.defense
                elif name_of_item.find("heal") != -1:
                    self.health += item.heal
                    if self.health > self.max_health:
                        self.health = self.max_health
                elif name_of_item.find("theory") != -1:
                    self.bm_previous_move = "freeze"
                elif name_of_item.find("firewall") != -1:
                    self.bm_block_next_attack = True
                    self.bm_previous_move = "block"
                else:
                    self.bm_check_item_uses()
                    return item.damage, name_of_item.find("kirillium") != -1

        self.bm_check_item_uses()
        return 0, False

    def bm_take_damage(self, damage):
        if self.bm_block_next_attack is True:
            self.bm_block_next_attack = False
        elif damage - self.defense > 0:
            self.health -= (damage - self.defense)
            for item in self.inventory:
                if item.name.lower().find("shield") != -1:
                    item.uses -= 1
            self.bm_check_item_uses()

    def bm_update(self):
        self.bm_previous_move = ""
        self.defense = self.bass_defense

        for item in self.inventory:
            self.defense += item.defense
