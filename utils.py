import random

def deep_copy(deep_list):
    """Returns a copy of a list of lists.

    The name is slighly misleading cause a list of list of list would break it,
    so it is not really _that_ deep, but enough for the game.

    @preconditions:
    type(deep_list[i][x]) is inmutable for every valid i, x
    """
    return [row[:] for row in deep_list[:]]

def is_a_sane_number(number, max):
    return 0 <= number <= max

def is_a_sane_letter(letter, max):
    return 0 <= letter_to_int(letter) <= max

def is_sane_point_choice(input, max):
    return is_a_sane_letter(input[0], max) and is_a_sane_number(int(input[1:]), max+1)

def int_to_letter(int):
    """Given the integer int, return a string representation.
    For example,
    0 -> 'A',
    1 -> 'B',
    25 -> 'Z'

    @preconditions:
    -65 <= i <= (1.114.111-65), whatever that is.
    You probably want to stay in the 0-25 range, though.
    """
    return chr(int + ord('A'))

def letter_to_int(letter):
    """Given a letter as a string, return its number representation.
    Caps agnostic.

    Example:
    'A' -> 0,
    'a' -> 0,
    'Z' -> 25

    @preconditions:
    len(letter) == 1
    """
    letter = letter.upper()
    return ord(letter) - 65

def _format_game_input(strings):
    """Take an arbitrary list of strings and format them nicely.
    """
    accum_string = ""
    for str in strings:
        accum_string = "{0} {1}\n".format(accum_string, str)
    final_string = "{0}\n>>> ".format(accum_string)
    return final_string

def _is_input_okey(conditions, user_input):
    """Take conditions, a list of functions that return booleans, and user_input,
    a string. Return True if all condition functions are True for the string,
    False otherwise.
    """
    return all([condition(user_input) for condition in conditions])

def game_input(conditions, examples, strings):
    """Take conditions, a list of functions that return booleans, examples, a list
    of strings from where one will be chosen as an example in case the user didn't
    format his input correctly and strings, a list of strings. Format the strings
    nicely for the game, then present the formatted string to the user as input.
    Validate the user input, and, when it makes sense, return it.
    """
    input_string = _format_game_input(strings)
    user_input = input(input_string)
    while not _is_input_okey(conditions, user_input):
        print("Not so fast, cowboy. It seems like your input wasn't correctly formated.")
        if examples:
            print("You inserted {0}. I'm looking for something like {1} \n".format(user_input, random.choice(examples)))
        user_input = input(input_string)
    return user_input
