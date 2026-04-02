import random
import input as text_input
# from player_class import Player
import time
#from playsound import playsound
#from game import execute_command, print_inventory_items


# THIS IS NOT FINISHED
# THIS IS NOT FINISHED
# THIS IS NOT FINISHED
# THIS IS NOT FINISHED
# THIS IS NOT FINISHED
# THIS IS NOT FINISHED
# I will be changing it later


objects = [["Maths student", [1, 1]], ["Scroll", [4, 4]]]  # TEMPORARY


def print_room_board(player, enemy, objects):
    cols = 5
    rows = 5  # 5 * 5 grid, 25 squares

    top = [" _______"]
    side = ["|       "]
    end = ["|"]

    parts = top, side, side, side

    tiles = []  # this creates the whole board
    for row in range(rows):
        row = []
        for p in parts:
            tempList = []
            for col in range(cols):
                tempList.append(p)
            tempList.append(end)
            row.append(tempList)
        tiles.append(row)
    tiles.append([top * 5])

    # this adds the icons on the board, their position corresponds to the position in the list
    tiles[player[1]][2][player[0]] = ["|   𝐏   "]
    tiles[enemy[1]][2][enemy[0]] = ["|   𝙆   "]
    for obj in objects:
        tiles[obj[1]][2][obj[0]] = ["|   ?   "]

    # this draws the board
    for row in tiles:
        for section in row:
            output_string = []
            for char in section:
                output_string += char
            print(''.join(output_string))
    print()


allowed_words = ["quit", "accept", "deny", "kirill", "go", "take", "drop", "use", "read", "inspect", "north", "east",
                 "south", "west"]


class Kirill:
    def __init__(self):
        self.name = "Grand Wizard of ABACWS, Kirill"
        self.health = 50
        self.atk = 1  # Base damage
        self.moves = {"Melee Attack": {"Damage": 1 * self.atk, "Description": f"{self.name} attacked!"},
                      "Block": {"Damage": 0, "Description": f"{self.name} used block!"},
                      "Ranged Attack": {"Damage": 1 * self.atk,
                                        "Description": f"{self.name} threw a bottle of water at you.."},
                      "Boost": {"Damage": 0, "Description": f"{self.name} boosted his stats"},
                      "Ultimate": {"Damage": 2 * self.atk, "Description": f"{self.name} used an ultimate!"}}

        self.moves_list = ["Melee Attack", "Ranged Attack", "Boost", "Block", "Ultimate"]

    def take_damage(self, damage):
        self.health -= damage
        print(self.name, "took", damage, "damage")

    def update(self):
        pass

    def choose_move(self):
        # if player is in range
        if (-1 <= (self.position_Y - self.player.position_Y) <= 1) and (
                -1 <= self.position_X - self.player.position_X <= 1):
            print("melee range")
            move = random.choice(["Melee Attack", "Ranged Attack", "Boost", "Block", "Ultimate"])
        else:
            move = random.choice(["Ranged Attack", "Boost"])
            print("long range")

        print(self.moves[move]["Description"])
        self.player.take_damage(self.moves[move]["Damage"])
        return move


class bossFight:
    def __init__(self):
        self.player = Player()
        self.player_position_X = 2
        self.player_position_Y = 1
        self.boss = Kirill()
        self.player_turn = True
        self.taken_positions = [[3, 1], [3, 3], [self.boss_position_X, self.boss_position_Y]]

    def print_turn(self):
        #print_inventory_items(self.player.items)
        pass


    def calculate_damage(self, boss_move):
        if boss_move == "Block":
            self.boss.take_damage(0)

        else:
            self.boss.take_damage(5)

    def main(self):
        #playsound('gamesound.mp3', block=False)
        print("Kirill has started attacking you!")
        dialogues = ["Insert text here", "Insert text here", "Is computer science a science?"]

        while self.boss.health > 0:
            player_attacked = False
            while self.player_turn:
                print_room_board([self.player_position_X, self.player_position_Y],
                                 [self.boss_position_X, self.boss_position_Y], [[3, 1], [3, 3]])
                player_move = input("What will you do? \n")
                player_move = text_input.normalise_input(player_move)
                player_attacked = self.player_move(player_move)

            boss_move = self.boss.choose_move()
            if player_attacked:
                self.calculate_damage(boss_move)
            self.player_turn = True


            if self.boss.health > 100:
                for sentence in dialogues:
                    time_now = time.time()
                    while time.time() - time_now < 5:
                        choice = input("wefat4wtt5")
                        if choice not in self.boss.moves_list:
                            self.player.take_damage(1)
                    break
            # print_inventory_items()
            # self.take_damage()

    def player_move(self, command):

        if 0 == len(command):
            return

        if command[0] == "go":
            if len(command) > 1:
                self.move_player(command[1])
            else:
                print("Go where?")

        elif command[0] == "attack":
            if len(command) == 1:
                self.player_turn = False
                return command
            else:
                print("Go where?")

        elif command[0] == "take":
            if len(command) > 1:
                self.execute_take(command[1])
            else:
                print("Take what?")

        elif command[0] == "drop":
            if len(command) > 1:
                self.execute_drop(command[1])
            else:
                print("Drop what?")

        else:
            print("This makes no sense.")

        # else:
        #     execute_command(command)

    def execute_drop(self, item_id):
        self.player_turn = False

    def execute_take(self, item_id):
        self.player_turn = False

    def is_valid_move(self, direction, newpos):
        if 0 <= newpos[0] > 5 or -1 < newpos[1] > 4 or newpos in self.taken_positions:
            print("You can't go there!")
            return False
        else:
            print("You moved", direction)
            self.player_turn = False
            return True

    def move_player(self, direction):
        if direction == "north":
            if self.is_valid_move(direction, [self.player.position_X, self.player.position_Y - 1]):
                self.player.position_Y -= 1

        elif direction == 'south':
            if self.is_valid_move(direction, [self.player.position_X, self.player.position_Y + 1]):
                self.player.position_Y += 1

        elif direction == "east":
            if self.is_valid_move(direction, [self.player.position_X + 1, self.player.position_Y]):
                self.player.position_X += 1

        elif direction == 'west':
            if self.is_valid_move(direction, [self.player.position_X - 1, self.player.position_Y]):
                self.player.position_X -= 1


# b = bossFight()
# b.main()
