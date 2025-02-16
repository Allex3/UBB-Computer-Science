from random import choice

from seminar.group913.seminar_7.board import get_free_squares_board
from seminar.group913.seminar_7.board import move_board


# import seminar.group914.seminar_7.board


def move_human(board, row: int, col: int) -> None:
    move_board(board, 'X', row, col)


"""
    Each _play_* function implements a computer play algorithm
    You can switch how the computer plays by changing the function that is called
    Implementation of Strategy Design Pattern 
        https://refactoring.guru/design-patterns/strategy
"""


def _play_random_move(board) -> tuple:
    row, col = choice(get_free_squares_board(board))  # tuple unpacking
    move_board(board, 'O', row, col)
    return row, col


def _play_smart_move(board) -> tuple:
    # TODO Implement
    pass


def move_computer(board) -> tuple:
    # return _play_random_move(board)
    return _play_smart_move()
