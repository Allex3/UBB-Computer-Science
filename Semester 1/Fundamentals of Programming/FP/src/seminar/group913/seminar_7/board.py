from pdoc import pdoc
from texttable import Texttable


def create_board():
    """
    Create an empty board for the game
    :return: The empty board
    """

    """
    0 -> empty square
    1 -> X
    -1 -> O
    """
    return {"board": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "move_count": 0}


def move_board(board, symbol: str, row: int, col: int):
    """
    Make a move on the board
    :param board: The board
    :param symbol: Either an 'X' or 'O'
    :param row: The row (one of 0, 1 or 2)
    :param col: The col (one of 0, 1 or 2)
    :return: None
    :raises: ValueError In case the move is invalid
    """
    board_data = board["board"]

    if symbol not in ['X', 'O']:
        raise ValueError("Invalid symbol")
    if row not in (0, 1, 2) or col not in (0, 1, 2):
        raise ValueError(f"Invalid coordinates for move - ({row},{col})")
    if board_data[row][col] != 0:
        raise ValueError(f"Square already taken - ({row},{col})")
    board_data[row][col] = 1 if symbol == 'X' else -1
    # increase the move counter only after the move is placed successfully
    board["move_count"] += 1


def is_full_board(board):
    return board["move_count"] == 9


def is_won_board(board):
    if board["move_count"] < 3:
        return False
    for row in board["board"]:
        if abs(sum(row)) == 3:
            return True

    b = board["board"]
    for col in (0, 1, 2):
        if abs(b[0][col] + b[1][col] + b[2][col]) == 3:
            return True

    if abs(b[0][0] + b[1][1] + b[2][2]) == 3:
        return True
    if abs(b[2][0] + b[1][1] + b[0][2]) == 3:
        return True
    return False


def _private_function(board):
    # Names starting with a _ are supposed to be private
    pass


def get_free_squares_board(board):
    board_data = board["board"]
    result = []

    for row in (0, 1, 2):
        for col in (0, 1, 2):
            if board_data[row][col] == 0:
                result.append((row, col))
    return result


def to_str_board(board) -> str:
    """
    Convert the board to a *string*

    >>> to_str_board(create_board())

    :param board: The board
    :return: The string representation of the board
    """
    t = Texttable()  # Texttable is a Python class
    board_data = board["board"]

    for row in board_data:
        display_row = row[:]  # display_row creates a copy of row
        for i in range(3):
            if display_row[i] == 0:
                display_row[i] = ' '
            elif display_row[i] == 1:
                display_row[i] = 'X'
            else:
                display_row[i] = 'O'
        t.add_row(display_row)
    return t.draw()  # draw() converts the Texttable to an str


if __name__ == "__main__":
    # __name__ is a Python attribute of the current module

    """
    To generate HTML documentation for this module
    """
    # f = open("doc.html", "wt")
    # f.write(pdoc("board.py", ""))
    # f.close()

    b = create_board()
    print(to_str_board(b))
    move_board(b, 'X', 1, 1)
    move_board(b, 'O', 0, 0)
    move_board(b, 'X', 2, 1)
    print(to_str_board(b))
    print(is_full_board(b))
    print(is_won_board(b))
