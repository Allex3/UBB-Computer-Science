from texttable import Texttable
import pickle


class BoardError(Exception):
    pass


class Board:
    """
    Class that implements the board of a 3x3 tic-tac-toe custom game
    """

    def __init__(self):
        """
        Initialize board with 0 on every square, 1 is X, 2 is O
        """
        self.__player = None
        self.__computer = None
        self.__turn = 1
        self.__ROWS = 3
        self.__COLUMNS = 3
        self.__board = [[0 for _ in range(self.__COLUMNS)] for _ in range(self.__ROWS)]

        self.__empty_square_column = None
        self.__empty_square_row = None
        self.__pieces_placed = 0

    def get_player(self):
        return self.__player

    def get_computer(self):
        return self.__computer

    def set_player(self, value: int):
        self.__player = value

    def set_computer(self, value: int):
        self.__computer = value

    def place_piece(self, player: int, row: int, column: int) -> None:
        """
        Place a piece for player 1 or 2 in a given row and column, if the square is free and valid.
        :param player: The player for which we place the piece (1 or 2)
        :param row: The row of the piece in the board
        :param column: The column of the piece in the board
        :return: None
        """
        if not (0 <= row < self.__ROWS and 0 <= column < self.__COLUMNS):
            raise BoardError(
                "You tried to place a piece on an invalid board position. Try a row and column between 0 and 2.")
        if self.__board[row][column] != 0:  # Position already occupied
            raise BoardError("You tried to place a piece in an occupied position.")
        self.__board[row][column] = player
        self.__turn = self.__turn % 2 + 1
        self.__pieces_placed += 1
        if self.__pieces_placed == 8:
            self.compute_empty_square()

    def __check_win_row(self):
        for row in range(self.__ROWS):
            if self.__board[row][0] != 0:
                if self.__board[row][0] == self.__board[row][1] == self.__board[row][2]:
                    return self.__board[row][0]

        return 0

    def __check_win_column(self):
        for column in range(self.__COLUMNS):
            if self.__board[0][column] != 0:
                if self.__board[0][column] == self.__board[1][column] == self.__board[2][column]:
                    return self.__board[0][column]
        return 0

    def __check_win_main_diagonal(self):
        if self.__board[0][0] != 0 and self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
            return self.__board[0][0]
        return 0

    def __check_win_secondary_diagonal(self):
        if self.__board[0][2] != 0 and self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            return self.__board[0][2]
        return 0

    def get_winner(self) -> int:
        """
        Returns the winner (1 or 2), or 0, if no one won yet
        :return: The winner (1 or 2), or 0, if no one won yet
        """
        if self.__check_win_row():
            return self.__check_win_row()
        if self.__check_win_column():
            return self.__check_win_column()
        if self.__check_win_main_diagonal():
            return self.__check_win_main_diagonal()
        if self.__check_win_secondary_diagonal():
            return self.__check_win_secondary_diagonal()

        return 0

    def placement_phase_end(self):
        return self.__pieces_placed == 8

    def __position_adjacent_to_empty_square(self, from_row: int, from_column: int):
        """
        See if the position we want to move from is adjacent to the empty square
        :param from_row: The old position's row
        :param from_column: The old position's column
        :return: True if we can move, False if not
        """
        if from_row == self.__empty_square_row and from_column == self.__empty_square_column - 1:
            return True
        if from_row == self.__empty_square_row and from_column == self.__empty_square_column + 1:
            return True
        if from_row == self.__empty_square_row + 1 and from_column == self.__empty_square_column:
            return True
        if from_row == self.__empty_square_row - 1 and from_column == self.__empty_square_column:
            return True
        if from_row == self.__empty_square_row + 1 and from_column == self.__empty_square_column + 1:
            return True
        if from_row == self.__empty_square_row - 1 and from_column == self.__empty_square_column + 1:
            return True
        if from_row == self.__empty_square_row - 1 and from_column == self.__empty_square_column - 1:
            return True
        if from_row == self.__empty_square_row + 1 and from_column == self.__empty_square_column - 1:
            return True

        # Basically check all the 8 positions that can be around the empty square.
        # The position given to check for is valid, and even if one of the positions is -1
        # It will just not return True in that loop, because from_row and from_column are valid between 0 and 2

        return False

    def get_turn(self):
        return self.__turn

    def set_turn(self):
        return self.__turn

    def move_piece(self, player: int, from_row: int, from_column: int):
        """
        During the movement phase, move from a square into the empty square and see if it's possible
        :param player: The player who moves (1 or 2)
        :param from_row: The row from which we want to move a piece into the empty square
        :param from_column: The column from which we want to move a piece into the empty square
        :return: None
        """
        if not (0 <= from_row < self.__ROWS and 0 <= from_column < self.__COLUMNS):
            raise BoardError(
                "You tried to place a piece on an invalid board position. Try a row and column between 0 and 2.")

        if not self.__position_adjacent_to_empty_square(from_row, from_column):
            raise BoardError("Square is not adjacent to the empty square")

        self.__board[from_row][from_column] = 0
        self.__board[self.__empty_square_row][self.__empty_square_column] = player
        self.__turn = self.__turn % 2 + 1

        self.compute_empty_square()

    def compute_empty_square(self):
        """
        Computes the position of the empty square on the board and puts it in a private field.
        :return:
        """
        for row in range(self.__ROWS):
            for column in range(self.__COLUMNS):
                if self.__board[row][column] == 0:
                    self.__empty_square_row = row
                    self.__empty_square_column = column
                    return

    def get_squares(self, state: int) -> list[tuple]:
        squares = []
        for row in range(self.__ROWS):
            for column in range(self.__COLUMNS):
                if self.__board[row][column] == state:
                    squares.append((row, column))
        return squares

    def __str__(self):
        """
        Magic method that is returned when we try to print an object of this class
        :return: The print form of the object using Texttable.draw()
        """
        table = Texttable()
        for row in range(self.__ROWS):
            data_row = []
            for column in range(self.__COLUMNS):
                match self.__board[row][column]:
                    case 0:
                        data_row.append(" ")
                    case 1:
                        data_row.append("X")
                    case 2:
                        data_row.append("O")
            table.add_row(data_row)

        return table.draw()
