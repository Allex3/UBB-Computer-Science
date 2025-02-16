from random import choice

from seminar.group913.seminar_8.board import Board

"""
    Strategy design pattern
    https://refactoring.guru/design-patterns/strategy
"""


class RandomComputerMove:
    """
    This class has one move() method which receives the state of the board as a parameter and makes its move
    on the board, returning the move coordinates
    """

    def __init__(self, board: Board):
        self.__board = board

    def move(self) -> tuple:
        row, col = choice(self.__board.get_free_squares())  # tuple unpacking
        self.__board.move('O', row, col)
        return row, col


class SmartComputerMove:
    def __init__(self, board: Board):
        self.__board = board

    def move(self) -> tuple:
        # TODO Implement me!
        pass


class Game:
    def __init__(self, computer_algorithm):
        self.__board = Board()
        self.__algorithm = computer_algorithm

    def get_board(self):
        # NOTE This exposes the board object used internally
        return self.__board

    def move_human(self, row: int, col: int) -> None:
        self.__board.move('X', row, col)

    def move_computer(self) -> tuple:
        self.__algorithm.move()
