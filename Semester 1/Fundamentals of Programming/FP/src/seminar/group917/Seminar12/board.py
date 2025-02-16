from texttable import Texttable

from Seminar917.Seminar12.exceptions import OutOfBoundsException, AlreadyHitException, GameOver


class BattleshipBoard:
    def __init__(self, size = 5):
        self.__size = size
        self._board = [[' ' for _ in range(self.__size)] for _ in range(self.__size)]
        self.__hits = 0

    """
    def setSize(self, newSize):
        self.__size = newSize
    """

    @property
    def size(self):
        return self.__size

    def placeShip(self, row, column):
        if not (0 <= row < self.size) or not (0 <= column <= self.size - 3):
            raise OutOfBoundsException()

        for i in range(column, column + 3):
            self._board[row][i] = 'X'

    def hit(self, row, column):
        if not (0 <= row < self.size) or not (0 <= column < self.size):
            raise OutOfBoundsException()
        if self._board[row][column] in ['*', 'H']:
            raise AlreadyHitException()

        if self._board[row][column] == 'X':
            self._board[row][column] = 'H'
            self.__hits += 1

            if self.__hits == 3:
                raise GameOver()
        else:
            self._board[row][column] = '*'

class PlayerBoard(BattleshipBoard):
    def __str__(self):
        table = Texttable()
        header = [' '] + [str(i) for i in range(self.size)]
        table.header(header)

        for i in range(self.size):
            row = [str(i)] + self._board[i]
            table.add_row(row)

        return table.draw()

class ComputerBoard(BattleshipBoard):
    def __str__(self):
        table = Texttable()
        """
        result = []
        for i in range(self.size):
            result.append(str(i))
        """
        header = [' '] + [str(i) for i in range(self.size)]
        table.header(header)

        for i in range(self.size):
            row = self._board[i]
            rowWithHiddenBoat = [' ' if cell == 'X' else cell for cell in row]
            row = [str(i)] + rowWithHiddenBoat
            table.add_row(row)

        return table.draw()
