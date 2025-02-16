import string
from enum import Enum

from texttable import Texttable


class InvalidMoveException(Exception):
    pass


class GameOverException(Exception):
    pass


class ChompSymbol(Enum):
    X = 0
    O = 1


class ChompBoard:
    def __init__(self, rows: int = 6, columns: int = 9):
        """
        How do we represent the board?
        ' '   - space character means empty
        ?     - poisoned part :(
        X, O  - moves
        =     - part that was bitten off
        """
        self.__rows = rows
        self.__columns = columns
        self.__data = [[' ' for j in range(columns)] for i in range(rows)]
        # the poisoned part must never be eaten!
        self.__data[0][0] = '?'

        # prepare the list of unoccupied squares
        self.__free_squares = []
        for i in range(rows):
            for j in range(columns):
                self.__free_squares.append((i, j))
        self.__free_squares.remove((0, 0))

    def chomp(self, symbol: ChompSymbol, row: int, column: int):
        if not (0 <= row <= self.__rows) or not (0 <= column <= self.__columns):
            raise InvalidMoveException(f"Move played outside the board ({row},{column})")
        if row == 0 and column == 0:
            raise GameOverException("Game over. You lost")
        if self.__data[row][column] != ' ':
            raise InvalidMoveException("Played an invalid square -> " + self.__data[row][column])

        # make the actual move
        if symbol == ChompSymbol.X:
            self.__data[row][column] = 'X'
            self.__free_squares.remove((row, column))
        elif symbol == ChompSymbol.O:
            self.__data[row][column] = 'O'
            self.__free_squares.remove((row, column))

        # break off everything that is to the right and below
        for i in range(row, self.__rows):
            for j in range(column, self.__columns):
                if self.__data[i][j] == ' ':
                    self.__data[i][j] = '='
                    self.__free_squares.remove((i, j))

    @property
    def free_squares(self):
        """
        Returns a reference to the live list!
        """
        return self.__free_squares

    def __str__(self):
        t = Texttable()
        t.header('/' + string.ascii_uppercase[:self.__columns])

        for i in range(0, self.__rows):
            t.add_row([i + 1] + self.__data[i])

        return t.draw()


if __name__ == "__main__":
    cb = ChompBoard(4, 5)
    print(cb)
    cb.chomp(ChompSymbol.O, 2, 2)
    cb.chomp(ChompSymbol.X, 1, 1)
    print(cb)
