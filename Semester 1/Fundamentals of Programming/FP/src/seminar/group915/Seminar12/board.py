from texttable import Texttable


class BoardExceptions(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

class  OutOfBoundsException(BoardExceptions):
    def __init__(self):
        super().__init__("Ship is out of bounds")

class AlreadyHitException(BoardExceptions):
    def __init__(self):
        super().__init__("Place is already hit")

class GameOverException(Exception):
    pass

class BattleshipBoard:
    def __init__(self, size = 5):
        self.__size = 5
        self._board = [[' ' for _ in range(self.__size)] for _ in range(self.__size)]
        self.__hits = 0

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
                raise GameOverException()
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
        header = [' '] + [str(i) for i in range(self.size)]
        table.header(header)

        for i in range(self.size):
            row = self._board[i]
            rowWithHiddenBoat = [' ' if cell == 'X' else cell for cell in row]
            row = [str(i)] + rowWithHiddenBoat
            table.add_row(row)

        return table.draw()