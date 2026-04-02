import string


def remove_punctuation(input_string):
    output_string = ""

    for char in input_string:
        # Don't add punctuation to new string
        if char not in string.punctuation:
            output_string += char

    return output_string


def filter_words(input_string):
    allowed_words = ["quit", "accept", "deny", "kirill", "go", "take", "drop", "use", "read", "inspect", "move", "do", "puzzle"]

    # Put words separated by a space into a list
    input_word_list = input_string.split(" ")

    if input_word_list[0] in allowed_words:
        return input_word_list

    return []


def normalise_input(input_string):
    input_string = input_string.lower()

    # Remove leading and trailing whitespaces
    input_string = input_string.strip()

    input_string = remove_punctuation(input_string)

    output_word_list = filter_words(input_string)

    return output_word_list


# Different input parser for the boss fight, checks if user input matches player_options
def bm_normalise_input(input_string, player_options):
    input_string = input_string.lower()
    input_string = input_string.strip()
    input_string = remove_punctuation(input_string)

    for i in range(0, len(player_options)):
        player_options[i] = player_options[i].lower()

    while input_string not in player_options:
        input_string = input("Not an option: ")
        input_string = input_string.lower()
        input_string = input_string.strip()
        input_string = remove_punctuation(input_string)

    output_word_list = input_string.split(" ")

    return output_word_list
