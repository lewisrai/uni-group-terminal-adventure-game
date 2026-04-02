# Import display_screen, display_title_text, display_collapse_animation, display_simple_text and display_appear_animation for rendering the screen
# All other functions should not be imported

import time
from display.display_extra import centre_string, create_pixel_buffer, get_item_ascii_art
from display.display_settings import RESOLUTION_X, RESOLUTION_Y, MAP_OFFSET, MAP_SIZE_X, MAP_SIZE_Y, TEXT_POSITION_X, TEXT_POSITION_Y, TEXT_AREA_X, TEXT_AREA_Y


def render_border(pixel_buffer, position_x, position_y, size_x, size_y):
    for x in range(position_x, position_x + size_x):
        # Top
        pixel_buffer[position_y][x] = "-"
        # Bottom
        pixel_buffer[position_y + size_y - 1][x] = "-"

    for y in range(position_y, position_y + size_y):
        # Left side
        pixel_buffer[y][position_x] = "|"
        # Right side
        pixel_buffer[y][position_x + size_x - 1] = "|"


def render_health_defense(pixel_buffer, player):
    position_x = 2
    position_y = 17

    # Display health
    # Maxiumum length of the actual bar of health displayed
    max_length = 20

    # Percentage of the max_length to display bar
    health_bar = "#" * int(player.health / player.max_health * max_length)

    info_text = "HEALTH:" + str(player.health) + " " + "DEFENSE:" + str(player.defense)

    info_text = centre_string(info_text, max_length)

    # Display info
    render_border(pixel_buffer, position_x, position_y, max_length + 2, 3)

    for i in range(0, len(info_text)):
        pixel_buffer[position_y + 1][position_x + i + 1] = info_text[i]

    # Display health bar
    render_border(pixel_buffer, position_x, position_y + 2, max_length + 2, 3)

    for i in range(0, len(health_bar)):
        pixel_buffer[position_y + 3][position_x + i + 1] = health_bar[i]


def render_inventory(pixel_buffer, player):
    number_of_slots = 6

    # Top corner of first slot
    position_x = 2
    position_y = 23

    slot_size_x = 20
    slot_size_y = 10

    # Inventory title
    length_x = (slot_size_x + 1) * number_of_slots + 1

    render_border(pixel_buffer, position_x, position_y, length_x, 3)

    inventory_text = centre_string("INVENTORY", length_x - 2)

    for i in range(0, length_x - 2):
        pixel_buffer[position_y + 1][position_x + i + 1] = inventory_text[i]

    position_y += 2

    # Slot borders
    for i in range(0, number_of_slots):
        render_border(pixel_buffer, (slot_size_x + 1) * i + position_x, position_y, slot_size_x + 2, slot_size_y + 2)

    art_position_x = position_x + 2
    art_position_y = position_y + 2

    # Create a new list with just names of items
    name_of_items = []

    for item in player.inventory:
        name_of_items.append(item.name)

    # Add blank items for the remaining slots
    while len(name_of_items) < number_of_slots:
        name_of_items.append("BLANK")

    # Change slots to locked if player hasn't unlocked backpack
    for i in range(player.max_inventory_slots, number_of_slots):
        name_of_items[i] = "LOCKED"

    for item_name in name_of_items:
        ascii_image = get_item_ascii_art(item_name)

        # Draw ascii art inside slot
        for y in range(0, slot_size_y - 4):
            for x in range(0, slot_size_x - 2):
                pixel_buffer[art_position_y + y][art_position_x + x] = ascii_image[y][x]

        # Item name below ascii art
        if item_name not in ["BLANK", "LOCKED"]:
            item_name_centred = centre_string(item_name, slot_size_x)

            for i in range(0, len(item_name_centred)):
                pixel_buffer[art_position_y + 8][art_position_x + i - 1] = item_name_centred[i]

        # Move to next slot
        art_position_x += slot_size_x + 1


def render_minimap(pixel_buffer, map, room_short_name):
    render_border(pixel_buffer, MAP_OFFSET, MAP_OFFSET, MAP_SIZE_X + 2, MAP_SIZE_Y + 2)

    # Copy characters from 2D list of map to pixel_buffer
    for y in range(0, MAP_SIZE_Y):
        for x in range(0, MAP_SIZE_X):
            pixel_buffer[MAP_OFFSET + y + 1][MAP_OFFSET + x + 1] = map[y][x]

    # Display room name underneath
    room_text = centre_string(room_short_name, 18)

    render_border(pixel_buffer, MAP_OFFSET, MAP_OFFSET + MAP_SIZE_Y + 1, MAP_SIZE_X + 2, 3)

    for i in range(0, len(room_text)):
        pixel_buffer[MAP_OFFSET + MAP_SIZE_Y + 2][MAP_OFFSET + i + 1] = room_text[i]


def render_text_area(pixel_buffer, room, player_options):
    # Top left corner of text
    position_x = TEXT_POSITION_X
    position_y = TEXT_POSITION_Y

    # Title
    room_title_text = "You are currently in " + room["name"]

    for i in range(0, len(room_title_text)):
        pixel_buffer[position_y][position_x + i] = room_title_text[i]

    position_y += 2

    # Add description
    room_text = room["description"] + "\n"

    # Add locked exits
    for locked_exit in room["locked_exits"]:
        room_text += "\n" + locked_exit[3] + locked_exit[0] + ", that requires " + locked_exit[2].name + "."

    # Check for puzzles inside the room
    if len(room["puzzle"]) != 0:
        if room["puzzle"][4] is False:
            room_text += "\n" + room["puzzle"][3]

    # Check for items inside the room
    if len(room["items"]) != 0:
        room_text += "\nIn this room there is:"
        for item in room["items"]:
            room_text += "\n" + item.name

    # Print room_text
    for char in room_text:
        if char != "\n":
            pixel_buffer[position_y][position_x] = char
            position_x += 1
        else:
            # End of line
            position_x = TEXT_POSITION_X
            position_y += 1

    # Print player_options with space below room_text
    position_x = TEXT_POSITION_X
    position_y += 2

    for option in player_options:
        for i in range(0, len(option)):
            pixel_buffer[position_y][position_x + i] = option[i]
        position_y += 1


def render_screen(map, room, player, player_options):
    # Render all areas of screen
    pixel_buffer = create_pixel_buffer(RESOLUTION_X, RESOLUTION_Y)
    render_border(pixel_buffer, 0, 0, RESOLUTION_X, RESOLUTION_Y)
    render_health_defense(pixel_buffer, player)
    render_inventory(pixel_buffer, player)
    render_minimap(pixel_buffer, map, room["short_name"])
    render_text_area(pixel_buffer, room, player_options)

    return pixel_buffer


def is_pixel_buffer_empty(pixel_buffer):
    # pixel_buffer is a list of lists
    for pixel_row in pixel_buffer:
        # pixel_row is a list
        for pixel in pixel_row:
            if pixel != " ":
                return False

    return True


def print_screen(pixel_buffer):
    # Time pause between lines
    sleep = 0.03

    # Clears terminal
    print("\033c")

    # Print line by line with a pause
    # pixel_buffer is a list of lists
    for pixel_row in pixel_buffer:
        line = ""
        # pixel_row is a list
        for pixel in pixel_row:
            line += pixel
        time.sleep(sleep)
        print(line)


def display_screen(map, room, player, player_options):
    # Render and display to screen
    pixel_buffer = render_screen(map, room, player, player_options)

    print_screen(pixel_buffer)


def display_title_text(map, room, player, title, text):
    # Render normal hud
    player_options = []

    pixel_buffer = render_screen(map, room, player, player_options)

    position_x = TEXT_POSITION_X
    position_y = TEXT_POSITION_Y

    # Clear room.name, room.description and player_options
    for y in range(position_y, position_y + TEXT_AREA_Y):
        for x in range(position_x, position_x + TEXT_AREA_X):
            pixel_buffer[y][x] = " "

    # Replace with title
    for i in range(0, len(title)):
        pixel_buffer[position_y][position_x + i] = title[i]

    # Add text underneath title
    position_y += 2

    for char in text:
        if char != "\n":
            pixel_buffer[position_y][position_x] = char
            position_x += 1
        else:
            position_x = TEXT_POSITION_X
            position_y += 1

    print_screen(pixel_buffer)


def print_animation_frame(pixel_buffer):
    # Print pixel_buffer without time delay
    print("\033c")

    pixels = ""

    for pixel_row in pixel_buffer:
        for pixel in pixel_row:
            pixels += pixel
        pixels += "\n"

    # Remove final new line character "\n" and print
    print(pixels[:-1])


def print_collapse_animation(pixel_buffer):
    # Animation Speed
    animation_speed = 125

    # Time between each frame, lower numbers produce more flicker
    sleep = 0.05

    # Initial direction
    direction_x = -1
    direction_y = 0

    # Start bottom right
    current_x = RESOLUTION_X - 1
    current_y = RESOLUTION_Y - 1

    # Borders
    left_limit_x = 0
    top_limit_y = 0
    right_limit_x = RESOLUTION_X - 1
    bottom_limit_y = RESOLUTION_Y - 2

    # Check which border is next
    next_border = 0

    while not is_pixel_buffer_empty(pixel_buffer):
        # Repeats the following loop depending on the animation speed
        # Deletes pixel in a spiral pattern, once reaches "border", it changes direction
        # _ being used as a throw away variable
        for _ in range(0, animation_speed):
            pixel_buffer[current_y][current_x] = " "
            current_x += direction_x
            current_y += direction_y

            # Check left border
            if current_x < left_limit_x and next_border == 0:
                current_x = left_limit_x
                left_limit_x += 1
                direction_x = 0
                direction_y = -1
                next_border = 1
            # Check top border
            elif current_y < top_limit_y and next_border == 1:
                current_y = top_limit_y
                top_limit_y += 1
                direction_x = 1
                direction_y = 0
                next_border = 2
            # Check right border
            elif current_x > right_limit_x and next_border == 2:
                current_x = right_limit_x
                right_limit_x -= 1
                direction_x = 0
                direction_y = 1
                next_border = 3
            # Check bottom border
            elif current_y > bottom_limit_y and next_border == 3:
                current_y = bottom_limit_y
                bottom_limit_y -= 1
                direction_x = -1
                direction_y = 0
                next_border = 0

        time.sleep(sleep)
        print_animation_frame(pixel_buffer)


def display_collapse_animation(map, room, player, player_options):
    # Render and display animation
    pixel_buffer = render_screen(map, room, player, player_options)

    print_collapse_animation(pixel_buffer)


def display_simple_text(text):
    # Get cursor in the middle of the screen relative to given resolution
    middle_y = int(RESOLUTION_Y / 2)

    text = centre_string(text, RESOLUTION_X)

    is_blank_range = True
    is_previous_space = False

    # Clears terminal
    print("\033c")

    for _ in range(0, middle_y):
        print()

    for char in text:
        # Skip initial spaces
        if is_blank_range and char == " ":
            print(" ", end="", flush=True)
        else:
            # Print each character separately and check for double spaces to stop print the trailing spaces
            is_blank_range = False
            if (is_previous_space is True) and char == " ":
                break
            elif char == " ":
                is_previous_space = True
            else:
                is_previous_space = False

            print(char, end="", flush=True)
            time.sleep(0.04)

    time.sleep(2)
