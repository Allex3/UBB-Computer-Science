from copy import deepcopy

import pickle

from board import Board, BoardError


class GameError(Exception):
    pass


class ComputerStrategy:
    def __init__(self, player: int, computer: int, board: Board):
        self.__player = player
        self.__computer = computer
        self.__best_move = None
        self.__board = board

    def place_piece(self) -> tuple:
        """
        Places the piece for the computer in a random square, or in a square not letting the player to win
        :return: The best position to place in
        """
        # Basically try to place the player in every free square and see if they win in one
        # If they do, then let the computer place there
        empties = self.__board.get_squares(0)
        for empty_square in empties:
            test_board = deepcopy(self.__board)
            test_board.place_piece(self.__player, empty_square[0], empty_square[1])
            if test_board.get_winner() == self.__player:  # Player won, place here
                return empty_square

        # If player doesn't win in any square, just place in the first
        return empties[0]

    def move_piece(self) -> tuple:
        """
        Moves a piece of the computer in the empty square and checks if any is a win, if not, make a random move
        :return: The best move
        """
        computer_squares = self.__board.get_squares(self.__computer)
        valid_squares = []
        for square in computer_squares:
            test_board = deepcopy(self.__board)
            try:
                test_board.move_piece(self.__computer, square[0], square[1])
                valid_squares.append(square)
                if test_board.get_winner() == self.__computer:
                    return square
            except BoardError:
                pass

        return valid_squares[0]


class Game:
    def __init__(self, board: Board, file_path: str = "game.bin"):
        self.__file_path = file_path
        self.__board = board
        self.__player = None
        self.__computer = None
        self.__computer_strategy = None

    def set_turns(self, player: int, computer: int):
        """
        Set the turns of the player and computer and sets up the computer strategy
        :param player: 1 or 2
        :param computer: 1 or 2
        :return: None
        """
        self.__board.set_player(player)
        self.__board.set_computer(computer)
        self.__player = player
        self.__computer = computer
        self.__computer_strategy = ComputerStrategy(self.__player, self.__computer, self.__board)

    def place_piece(self, player: int, row: int, column: int):
        """
        Place a piece in a given row and column
        :param player: The player for which we place the piece (1 or 2)
        :param row: Row
        :param column: Column
        :return: None
        """
        self.__board.place_piece(player, row, column)

    def place_computer(self):
        """
        Place the best move for the computer
        :return: None
        """
        move = self.__computer_strategy.place_piece()
        self.__board.place_piece(self.__computer, move[0], move[1])

    def move_piece(self, player: int, from_row: int, from_column: int):
        self.__board.move_piece(player, from_row, from_column)

    def move_computer(self):
        move = self.__computer_strategy.move_piece()
        self.__board.move_piece(self.__computer, move[0], move[1])

    def get_player(self):
        return self.__player

    def get_computer(self):
        return self.__computer

    def get_winner(self):
        return self.__board.get_winner()

    def get_phase(self):
        return self.__board.placement_phase_end()  # True if we are in the movement phase, False if still in the placement

    def get_turn(self):
        return self.__board.get_turn()

    def save(self):
        file = open(self.__file_path, "wb")
        pickle.dump(self.__board, file)

    def load(self):
        file = open(self.__file_path, "rb")
        try:
            self.__board = pickle.load(file)
        except EOFError:
            raise GameError("There is no game to load. Will start a new game.")
        if self.__board.get_player() is None:
            raise GameError("There is no game to load. Will start a new game.")
        self.set_turns(self.__board.get_player(), self.__board.get_computer())

    def __str__(self):
        return str(self.__board)
