from random import choice
from utils import deep_copy

_ONE = [[True, True, False, True, True],
        [True, False, True, False, True],
        [False, True, True, True, False],
        [True, False, True, False, True],
        [True, True, False, True, True]]

_TWO = [[False, True, False, True, False],
        [True, True, False, True, True],
        [False, True, False, True, False],
        [True, False, True, False, True],
        [True, False, True, False, True]]

_THREE = [[True, False, False, False, True],
         [True, True, False, True, True],
         [False, False, True, False, False],
         [True, False, True, False, False],
         [True, False, True, True, False]]

_FOUR = [[True, True, False, True, True],
         [False, False, False, False, False],
         [True, True, False, True, True],
         [False, False, False, False, True],
         [True, True, False, False, False]]

_FIVE = [[False, False, False, True, True],
         [False, False, False, True, True],
         [False, False, False, False, False],
         [True, True, False, False, False],
         [True, True, False, False, False]]

_TEST = [[True, True, True],
         [True, False, False],
         [True, True, True]]

def get_first():
    """Return a copy of the board for the first level."""
    return deep_copy(_ONE)

def get_second():
    """Return a copy of the board for the second level."""
    return deep_copy(_TWO)

def get_third():
    """Return a copy of the board for the third level."""
    return deep_copy(_THREE)

def get_fourth():
    """Return a copy of the board for the fourth level."""
    return deep_copy(_FOUR)

def get_fifth():
    """Return a copy of the board for the fifth level."""
    return deep_copy(_FIVE)

def get_all():
    """Return an ordered list for the 5 pre-stablished levels."""
    return [get_first(), get_second(), get_third(), get_fourth(), get_fifth()][:]

def get_n(n):
    """Return the board for the pre-stablished level number n.

    @preconditions:
    0 <= n < 5
    """
    return get_all()[n]

def create_random_of_dimension(n):
    """Return a random board of dimension n"""
    return deep_copy([[choice([True, False]) for _ in range(n)] for row in range(n)])

def get_five_random_of_dimension(n):
    """Return a list of five random boards of dimension n."""
    return [create_random_of_dimension(n) for _ in range(5)]
