from random import randint

class ComputerFirstAvailablePosStrategy:
    def __init__(self, board):
        self.__board = board

    def getNextComputerMove(self):
        for i in range(3):
            for j in range(3):
                if self.__board.getBoardValue(i, j) == 0:
                    return i, j

        return -1, -1

class ComputerRandomStrategy:
    def __init__(self, board):
        self.__board = board

    def getNextComputerMove(self):
        found = False
        while not found:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.__board.getBoardValue(x, y) == 0:
                return x, y

class ComputerBlockingStrategy:
    pass

class Game:
    def __init__(self, board, computerStrategy):
        self.__board = board
        self.__computerStrategy = computerStrategy

    def humanMove(self, x: int, y: int):
        self.__board.moveBoard(x, y, 'X')

    def computerMove(self):
        x, y = self.__computerStrategy.getNextComputerMove()
        self.__board.moveBoard(x, y, 'O')