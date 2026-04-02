import time
from display.display import create_pixel_buffer, render_border, render_screen, print_screen, display_simple_text, print_collapse_animation
from display.display_extra import centre_string, get_kirill_ascii_art
from display.display_settings import RESOLUTION_X, RESOLUTION_Y, MAP_SIZE_X, MAP_SIZE_Y, TEXT_POSITION_X, TEXT_POSITION_Y, TEXT_AREA_X, TEXT_AREA_Y


def display_kirill(grid, player, player_options, kirill):
    # Create a blank map to satisfy argument for render_screen
    map = create_pixel_buffer(MAP_SIZE_X, MAP_SIZE_Y)

    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            map[y][x] = "?"

    # Create a blank room to satisfy argument for render_screen
    room = {"name": "", "short_name": "??? ????? ?? ??????", "description": "", "items": [], "locked_exits": [], "puzzle": []}

    pixel_buffer = create_pixel_buffer(RESOLUTION_X, RESOLUTION_Y)
    pixel_buffer = render_screen(map, room, player, player_options)

    # Clear room.name, room.description and player_options for custom interface with boss
    for y in range(TEXT_POSITION_Y, TEXT_POSITION_Y + TEXT_AREA_Y):
        for x in range(TEXT_POSITION_X, TEXT_POSITION_X + TEXT_AREA_X):
            pixel_buffer[y][x] = " "

    position_x = TEXT_POSITION_X
    position_y = TEXT_POSITION_Y

    # Title
    for i in range(0, len(kirill.name)):
        pixel_buffer[position_y][position_x + i] = kirill.name[i]

    position_y += 2

    grid_size_x = 5
    grid_size_y = 5

    grid_area_x = 5
    grid_area_y = 2

    for i in range(0, grid_size_y):
        for j in range(0, grid_size_x):
            render_border(pixel_buffer, position_x + (grid_area_x + 1) * j, position_y + (grid_area_y + 1) * i, grid_area_x + 2, grid_area_y + 2)
            pixel_buffer[position_y + (grid_area_y + 1) * i + 2][position_x + (grid_area_x + 1) * j + 3] = grid[i][j]

    # Offset text to avoid grid
    text_offset = 34
    position_x += text_offset

    # Display text
    health_text = "Kirill's Health: " + str(kirill.health)

    for i in range(0, len(health_text)):
        pixel_buffer[position_y][position_x + i] = health_text[i]

    position_y += 2

    for char in kirill.message:
        if char != "\n":
            pixel_buffer[position_y][position_x] = char
            position_x += 1
        else:
            position_x = TEXT_POSITION_X + text_offset
            position_y += 1

    # Display player_options
    position_x = TEXT_POSITION_X + text_offset
    position_y += 2

    for option in player_options:
        for i in range(0, len(option)):
            pixel_buffer[position_y][position_x + i] = option[i]
        position_y += 1

    print_screen(pixel_buffer)


def display_opening_animation():
    # Render kirill acsii to blank pixel_buffer
    pixel_buffer = create_pixel_buffer(RESOLUTION_X, RESOLUTION_Y)
    render_border(pixel_buffer, 0, 0, RESOLUTION_X, RESOLUTION_Y)

    kirill_ascii = get_kirill_ascii_art()

    y = 1
    for line in kirill_ascii.split("\n"):
        line = centre_string(line, RESOLUTION_X - 2)
        for i in range(0, RESOLUTION_X - 2):
            pixel_buffer[y][i + 1] = line[i]
        y += 1

    # Display kirill opening boss animation
    display_simple_text("A horrible chill goes down your spine...")  # Terraria reference
    print_screen(pixel_buffer)
    time.sleep(2)
    print_collapse_animation(pixel_buffer)
