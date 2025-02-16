from random import randint

from Seminar916.Seminar12.exceptions import BoardExceptions


class ComputerGame:
    def __init__(self, ownBoard, opponentBoard):
        self.__ownBoard = ownBoard
        self.__opponentBoard = opponentBoard

    def placeShip(self):
        try:
            row = randint(0, self.__ownBoard.size - 1)
            column = randint(0, self.__ownBoard.size - 4)
            self.__ownBoard.placeShip(row, column)
        except BoardExceptions:
            self.placeShip()

    def hit(self):
        try:
            row = randint(0, self.__opponentBoard.size - 1)
            column = randint(0, self.__opponentBoard.size - 1)

            self.__opponentBoard.hit(row, column)
            return row, column
        except BoardExceptions:
            self.hit()

