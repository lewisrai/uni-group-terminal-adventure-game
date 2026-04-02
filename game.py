import time

from input import normalise_input, bm_normalise_input

# Music
from playsound import playsound
import multiprocessing

from display.display import display_screen, display_title_text, display_collapse_animation, display_simple_text
from display.display_kirill import display_opening_animation, display_kirill

# Import as rooms_xx otherwise it would overide the previous room
from floors.floor_00 import rooms as rooms_00, get_map_ascii as get_map_floor_00
from floors.floor_01 import rooms as rooms_01, get_map_ascii as get_map_floor_01
from floors.floor_02 import rooms as rooms_02, get_map_ascii as get_map_floor_02
from floors.floor_03 import rooms as rooms_03, get_map_ascii as get_map_floor_03
from floors.floor_04 import rooms as rooms_04, get_map_ascii as get_map_floor_04

from bosses.kirill_boss_class import Kirill as KirillClass
from items.item_class import Item as ItemClass
from items.items import *
from player.player_class import Player as PlayerClass


def list_options(room, inventory, current_room):
    # Returns a list of strings for the players options
    output_list = []

    # Get room options
    for direction in room["exits"]:
        output_list.append(f'GO {direction.upper()} to {room["exits"][direction]}')

    # Get inventory options
    for item in inventory:
        if "-".join(output_list).find(f'USE / DROP / INSPECT {item.name}') == -1:  # Nate's checking if the item is unique and isnt blank (name and shame)
            output_list.append(f'USE / DROP / INSPECT {item.name}')

    # listing all the items the player can pick up
    for item in current_room["items"]:
        if "-".join(output_list).find(f'TAKE {item.name}') == -1: #checking if the item is unique
            output_list.append(f'TAKE {item.name}')

    # checking if the current room has a puzzle
    if len(current_room["puzzle"]) > 0:
        if current_room["puzzle"][4] is False:
            output_list.append("DO PUZZLE")

    return output_list


def execute_go_command(building, current_floor, current_room, user_input_word_list):
    # Check if user entered a direction
    if len(user_input_word_list) < 2:
        print("Invalid Direction Given! Try North, South, East or West.")
        time.sleep(2)
        return current_room

    # Check if user input matches a direction in the room dictionary
    if user_input_word_list[1] in current_room["exits"]:
        current_room = building[current_floor][current_room["exits"][user_input_word_list[1]]]
    else:
        print("No Room Found!")
        time.sleep(2)

    return current_room

# pick up item
def execute_take_command(current_room, player, user_input_list):
    remove_words = ["take", "a", "an", "the", "please"]
    out_list = []
    # sanitise input
    for word in user_input_list:
        if word not in remove_words:
            out_list.append(word)

    item_name = " ".join(out_list)
    # checking if the item is in the room
    for item in current_room["items"]:
        if item_name == item.name.lower():
            # checking if the item can be added to the inventory, if so remove the item from the room
            if player.add_to_inventory(item):
                current_room["items"].remove(item)
                playsound("sounds/pick_item.wav", block=False)
                return

            print("Not enough inventory space.")
            time.sleep(2)
            return

    print(f'{item_name} not found.')
    time.sleep(2)

# drop an item
def execute_drop_command(current_room, player, user_input_list):
    remove_words = ["drop", "a", "an", "the", "please"]
    out_list = []
    # sanitise inptut
    for word in user_input_list:
        if word not in remove_words:
            out_list.append(word)

    item_name = " ".join(out_list)

    # checking if item is inventory
    for item in player.inventory:
        if item_name == item.name.lower():
            current_room["items"].append(item) # if item is in player inventory, romove it and add to room
            player.inventory.remove(item)
            playsound("sounds/drop_item.wav", block=False)
            return

    print(f'{item_name} not found.')
    time.sleep(2)

# use an item, only functionality is to open locked exits
def execute_use_command(current_room, player, user_input_list):
    remove_words = ["use", "a", "an", "the", "please"]
    out_list = []
    # sanitising the input
    for word in user_input_list:
        if word not in remove_words:
            out_list.append(word)

    item_name = " ".join(out_list)

    item_to_use = ItemClass

    for item in player.inventory:
        if item_name == item.name.lower():
            item_to_use = item
            break
    #testing to see if the item exists, stops an error
    try:
        item_to_use.name
    except:
        print("You do not currently have that item.")
        time.sleep(2)
        return current_room

    # Only functionality in open rooms now, checking if its a key
    for locked_exit in current_room["locked_exits"]:
        if item_to_use.name == locked_exit[2].name:
            current_room["exits"][locked_exit[0]] = locked_exit[1]
            current_room["locked_exits"].remove(locked_exit)
            item_to_use.uses = item_to_use.uses - 1
            if item_to_use.uses <= 0:
                player.inventory.remove(item_to_use)
                print(f'{item_to_use.name} has been broken.')
            print(f'The passage {locked_exit[0]} has been unlocked!')
            time.sleep(2)
            return current_room
        else:
            print("This item does not work here.")
            time.sleep(2)
            return current_room


def execute_inspect_command(player, user_input_list, room, map):
    remove_words = ["inspect", "a", "an", "the", "please"]
    out_list = []
    # sanitise input
    for word in user_input_list:
        if word not in remove_words:
            out_list.append(word)

    item_name = " ".join(out_list)

    item_to_inspect = ItemClass
    for item in player.inventory:
        if item_name.lower() == item.name.lower():
            item_to_inspect = item
            break
    # checking if the item is in inventory
    try:
        item_to_inspect.name
    except:
        print(f'You do not currently have that item.')
        time.sleep(5)
        return

    display_title_text(map, room, player, item_to_inspect.name, item_to_inspect.description) #display it
    input("Press [Enter] to continue.")
    return

# run a puzzle in the room, each puzzle returns true for correct and false for incorrect
def execute_puzzle_command(current_room, player):
    if current_room["puzzle"][0](current_room["puzzle"][1]):
        print("Correct!")
        print(f'The {current_room["puzzle"][2].name} materialises in front of you!')
        current_room["items"].append(current_room["puzzle"][2])
        current_room["puzzle"][4] = True
        time.sleep(2)
        return
    else:
        print("Incorrect")
        time.sleep(2)
        return


def kirill_boss_fight(music_thread, player):
    kirill = KirillClass()

    display_opening_animation()

    # Boss fight loop
    # Check if both Kirill and Player are alive
    while (not player.health <= 0) and (not kirill.health <= 0):
        # Clear grid
        grid = [[" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "]]

        # Update defense
        player.bm_update()
        # Randomise move, update message
        kirill.update()

        # Calculate player options
        player_options = []

        if player.bm_position_y > 0:
            player_options.append("GO NORTH")
        if player.bm_position_x < 4:
            player_options.append("GO EAST")
        if player.bm_position_y < 4:
            player_options.append("GO SOUTH")
        if player.bm_position_x > 0:
            player_options.append("GO WEST")
        for item in player.inventory:
            player_options.append("USE " + item.name.upper())

        # Update grid
        grid[kirill.position_y][kirill.position_x] = "K"
        grid[player.bm_position_y][player.bm_position_x] = "P"

        display_kirill(grid, player, player_options, kirill)

        # Add quit option after display since it shouldn't be displayed
        player_options.append("quit")

        user_input = input(": ")
        user_input_word_list = bm_normalise_input(user_input, player_options)

        # Execute player's command
        match user_input_word_list[0]:
            case "quit":
                break
            case "use":
                damage = player.bm_use_item(user_input_word_list)
                kirill.attack_player(player)
                kirill.take_damage(damage[0], damage[1], player)
                kirill.message = "You think that hurt me? Absolutely not!\n"
            case "go":
                player.bm_move(user_input_word_list, kirill.position_x, kirill.position_y)
                kirill.attack_player(player)
                kirill.message = "Stop moving around and try and get me.\n"

    # Returns the ending depending on factors such as is Kirill dead, player used corrupted items, etc.
    if kirill.health > 0:
        music_thread.terminate()
        music_thread = multiprocessing.Process(target=play_kirill_won)
        music_thread.start()
        ending = ["Kirill lives on... you don't know what happens next because you're dead.", "But seriously, how did you lose that fight?"]
    elif player.health > 0 and player.corrupted is True:
        ending = ["You won, but at what cost?", "Your mind and body is corrupted and you become the new Grand Wizard of ABACWS"]
    elif player.health > 0:
        ending = ["You defeated the Grand Wizard of ABACWS, Kirill.", "You live a new life famous from your achievement."]
    else:
        ending = ["You sacrificed yourself for the world.", "You live on as a legend."]

    return ending


def play_bgm():
    while True:
        playsound("sounds/bgm.mp3")


def play_boss_bgm():
    while True:
        playsound("sounds/boss_bgm.mp3")


def play_kirill_won():
    while True:
        playsound("sounds/kirill_won.mp3")


def main():
    # Play BGM
    music_thread = multiprocessing.Process(target=play_bgm)
    music_thread.start()

    # Initialise variables on starting rooms
    building = [rooms_00, rooms_01, rooms_02, rooms_03, rooms_04]
    current_floor = 0
    current_room = building[current_floor]["Entrance"]
    map = get_map_floor_00(current_room["name"])

    is_game_running = True
    is_fighting_kirill = False

    # Skip to floor before boss fight
    #current_room = building[4]["Tech"]

    player = PlayerClass()
    player_options = ["You can:"] + list_options(current_room, player.inventory, current_room)

    # Skip to floor before boss fight
    # player.add_to_inventory(Item(item_advanced_sword))
    # player.add_to_inventory(Item(item_chair))
    # player.add_to_inventory(Item(item_backpack))
    # player.add_to_inventory(Item(item_advanced_shield))
    # player.add_to_inventory(Item(item_healing))
    # player.add_to_inventory(Item(item_box_set))
    # player.add_to_inventory(Item(item_firewall))

    ending = ["You quit early.", "At least finish the game."]

    # Main Loop
    while is_game_running:
        if is_fighting_kirill:
            music_thread.terminate()
            music_thread = multiprocessing.Process(target=play_boss_bgm)
            music_thread.start()
            ending = kirill_boss_fight(music_thread, player)
            is_game_running = False
        else:
            # Check if room has no exits, go to next floor
            if len(current_room["exits"]) == 0 and len(current_room["locked_exits"]) == 0:
                if current_floor == 4:
                    is_fighting_kirill = True
                else:
                    current_floor += 1
                    playsound("sounds/new_floor.mp3", block=False)
                    # Check for room that is at "the top of the stairs", ie the first room on the floor
                    for room in building[current_floor]:
                        if building[current_floor][room]["top_of_stairs"] is True:
                            # Start room transition
                            display_collapse_animation(map, current_room, player, player_options)
                            display_simple_text(current_room["description"])
                            current_room = building[current_floor][room]
                            break
            else:
                # Update map
                match current_floor:
                    case 1:
                        map = get_map_floor_01(current_room["name"])
                    case 2:
                        map = get_map_floor_02(current_room["name"])
                    case 3:
                        map = get_map_floor_03(current_room["name"])
                    case 4:
                        map = get_map_floor_04(current_room["name"])

                # Update player_options
                player_options = ["You can:"] + list_options(current_room, player.inventory, current_room)

                display_screen(map, current_room, player, player_options)

                user_input = input(": ")

                user_input_word_list = normalise_input(user_input)

                # Execute the player's command
                if len(user_input_word_list) == 0:
                    print("Please enter a command.")
                    time.sleep(2)
                elif user_input_word_list[0] == "quit":
                    is_game_running = False
                elif user_input_word_list[0] == "go" or user_input_word_list[0] == "move":
                    current_room = execute_go_command(building, current_floor, current_room, user_input_word_list)  # error occured here, if second word wasnt a dir, there would be no user_input_word_list[1]
                elif user_input_word_list[0] == "take":
                    execute_take_command(current_room, player, user_input_word_list)
                elif user_input_word_list[0] == "drop":
                    execute_drop_command(current_room, player, user_input_word_list)
                elif user_input_word_list[0] == "use":
                    current_room = execute_use_command(current_room, player, user_input_word_list)
                elif user_input_word_list[0] == "inspect":
                    execute_inspect_command(player, user_input_word_list, current_room, map)
                elif user_input_word_list[0] == "do" and user_input_word_list[1] == "puzzle" and len(current_room["puzzle"]) > 0:
                    if current_room["puzzle"][4] == False: #doing this chain cus this would cause error otherwise
                        execute_puzzle_command(current_room, player)
                    else:
                        print("I didn't understand your command.")
                        time.sleep(2)
                elif user_input_word_list[0] == "zork":
                    is_fighting_kirill = True
                else:
                    print("I didn't understand your command.")
                    time.sleep(2)

    # Display ending
    display_simple_text(ending[0])
    display_simple_text(ending[1])
    input("")
    print("\033c")

    # Stop music
    music_thread.terminate()


if __name__ == "__main__":
    main()
