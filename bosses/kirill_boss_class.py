from random import randrange
from playsound import playsound


class Kirill:
    def __init__(self):
        self.name = "Grand Wizard of ABACWS, Kirill"
        self.position_x = 2
        self.position_y = 0
        self.message = "YOU WILL NEVER DEFEAT ME\n"
        self.health = 100
        self.defense = 2
        self.base_defense = 2
        self.extra_damage = 0
        self.available_moves = {"Melee": {"damage": 18, "description": "Kirill is preparing his sword!\n"},
                                "Block": {"damage": 0, "description": "Kirill is conjuring a shield!\n"},
                                "Range": {"damage": 17, "description": "Kirill is about to throw a bottle of water at you...?\n"},
                                "Boost": {"damage": 0, "description": "Kirill is powering up!\n"},
                                "Ultimate": {"damage": 29, "description": "Kirill is preparing his ultimate move!\n"}}
        self.move_list = ["Melee", "Block", "Range", "Boost", "Ultimate"]
        self.current_move = ""

    def update(self):
        # Reset defense and randomise move
        self.defense = self.base_defense

        random_number = randrange(0, 100)

        if random_number < 40:
            self.current_move = self.move_list[0]
        elif random_number < 55:
            self.current_move = self.move_list[1]
        elif random_number < 85:
            self.current_move = self.move_list[2]
        elif random_number < 95:
            self.current_move = self.move_list[3]
        else:
            self.current_move = self.move_list[4]

        self.message += self.available_moves[self.current_move]["description"]

    def take_damage(self, damage, kirillium_sword, player):
        # Adjust damage depending on distance
        distance = abs(player.bm_position_x - self.position_y) + abs(player.bm_position_y - self.position_y)
        damage += (6 - distance)

        # Check if kirillium sword, then decrease defense and take damage
        if kirillium_sword is True:
            if damage - (self.defense // 2) > 0:
                self.health -= damage - (self.defense // 2)
                playsound("sounds/hit.wav", block=False)
        elif damage - self.defense > 0:
            self.health -= (damage - self.defense)
            playsound("sounds/hit.wav", block=False)

    def attack_player(self, player):
        # Reset message and attack player
        self.message = ""

        # Add message for special moves by player
        if player.bm_previous_move == "freeze":
            self.message = "Don't you dare cancel my attack. You will pay for that!\n"
            return
        elif player.bm_previous_move == "block":
            self.message = "That won't last for ever. Hahaha.\n"
            return

        match self.current_move:
            case "Melee":
                player.bm_take_damage(self.available_moves[self.current_move]["damage"] + self.extra_damage)
            case "Block":
                self.defense += 10
            case "Range":
                if player.bm_previous_move == "move":
                    self.message += "Nice dodge but you won't be so lucky next time.\n"
                elif self.current_move == "Range":
                    player.bm_take_damage(self.available_moves[self.current_move]["damage"] + self.extra_damage)
            case "Boost":
                self.extra_damage += 1
            case "Ultimate":
                player.bm_take_damage(self.available_moves[self.current_move]["damage"] + self.extra_damage)
