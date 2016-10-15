import levels
import utils
import sys

def str_board(board):
    """Take a board as a list of lists of booleans, where True indicates
    "light on" and False indicates "light out". Return a str representation
    of that board.

    @preconditions:
    len(board) == len(board[i]) for every i, 0 <= i < len(board)
    """
    def circle_or_dot(point_as_bool):
        return "o" if point_as_bool else "."

    first_row = list(map(utils.int_to_letter, range(len(board))))
    first_column = range(len(board))

    row_with_borders = []
    for i, row in enumerate(board):
        row_with_borders.append(([str(first_column[i]+1)]) + list(map(circle_or_dot, row)))

    board_as_string = "  {0} \n".format(" ".join(first_row))
    for row in row_with_borders:
        board_as_string = "{0}{1}\n".format(board_as_string, " ".join(row))
    return board_as_string

def is_position_on_board(x, y, board):
    """Take x, y integers and board a list of lists.

    Return True if accessing board[y][x] will not raise IndexError.

    @preconditions:
    len(board) == len(board[i]) for every i, 0 <= i < len(board).
    """
    return 0 <= x < len(board) and 0 <= y < len(board)

def change_board(x, y, board):
    """Take x,y integers and board a list of lists. Modify the board
    so that pre(board[y][x]) == not board[y][x], where pre is the
    function that returns the board before passing through this function.
    It does the same for the points up, down, left and right of the specified
    x, y, if they are found inside the board.

    Return None.
    """
    board[y][x] = not board[y][x]  # economists would love these inverted x,y axis
    up, right, down, left = ((x, y-1), (x+1, y), (x, y+1), (x-1, y))
    for x, y in (up, right, down, left):
        if is_position_on_board(x, y, board):
            board[y][x] = not board[y][x]

def success(board):
    """Take a board, a list of lists.

    Return True if there are no "truthy" elements inside the lists of
    the board, False otherwise.
    """
    return not any([any([light for light in row]) for row in board])

def amount_of_lights_turned_on(board):
    """Take a board, a list of lists.
    Return an integer represeting the amount of lights turned on on the board.
    """

    # booleans are pretty much integers for python except when it comes to
    # the __str__ method so this works :)
    return sum([sum([light for light in row]) for row in board])

def play_a_level(board):
    """Take a board, a list of lists.  Guides the user through a level of
    "Lights out!".

    Sideffects include I/O with the user and modifying the board.

    Return the amount of points scored by the user as a integer.
    """
    def input_condition(i):
        return (2 <= len(i) <= 3 and i[1:].isdigit() and utils.is_sane_point_choice(i, len(board)-1))\
                or (i == 'RESET')

    original_board = utils.deep_copy(board)  # keep one in case user resets
    turns_available = len(board)*3
    points_scored = 0
    for _ in range(turns_available):
        print(str_board(board))
        game_choice = utils.game_input([input_condition],
                                       ["A1", "B6", "D9", "C4"],
                                       ["Please input the light you'd like to switch",
                                        "For example, A1 for the top leftmost light",
                                        "No spaces please. Input RESET to reset the level"])
        if game_choice.upper() == "RESET":
            print("Remember that reseting will cost you 50 times the number of lights you've got turned on!")
            points_scored -= 50 * amount_of_lights_turned_on(board)
            board = original_board
            continue
        point = game_choice  # if the user didnt reset, this is a point on the board
        x, y = (utils.letter_to_int(point[0]), int(point[1])-1)
        change_board(x, y, board)  # mod board to reflect user decision
        turns_available -= 1
        if success(board):
            points_scored += 500
            print("Wohooo! You made it! +500 points!")
            return points_scored
    else:
        print("Boooh, you lost! 300 points lost!")
        points_scored -= 300
        return points_scored

def main():
    """Start up a game of "Lights out!". Print some welcome messages and
    let the user choose history mode or random mode. Will print the amount
    of points, both accumulated and on each level, after each level.

    Return None.
    """
    print("Welcome to Lights Out! \n")
    while True:
        choice = utils.game_input([], [],
                                  ["Do you want to play History Mode or Random Mode? [H/R]",
                                   "Press any key other than H or R to exit."])
        choice = choice.lower()
        global_score = 0
        if choice != "r" and choice != "h":
            sys.exit(0)
        elif choice == "r":
            dimension = int(utils.game_input([lambda i: i.isdigit() and 0 <= int(i) <= 10],
                                             ["1", "2", "3", "5", "7"],
                                             ["What size do you want the board to be?",
                                              "Enter just one number.",
                                              "For example '5' for a 5x5 board."]))
            boards = levels.get_five_random_of_dimension(dimension)
        elif choice == "h":
            boards = levels.get_all()

        for i in range(5):
            board = boards[i]
            level_score = play_a_level(board)
            global_score += level_score
            score_string = ("You got {0} points on this level "
                            "and you have {1} points accumulated").format(level_score, global_score)
            print(score_string)

if __name__ == '__main__':
    main()
