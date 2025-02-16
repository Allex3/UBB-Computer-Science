from random import randint

from Seminar917.Seminar12.exceptions import BoardException


class ComputerGame:
    def __init__(self, ownBoard, opponentBoard):
        self.__ownBoard = ownBoard
        self.__opponentBoard = opponentBoard

    def placeShip(self):
        try:
            row = randint(0, self.__ownBoard.size - 1)
            column = randint(0, self.__ownBoard.size - 3)
            self.__ownBoard.placeShip(row, column)
        except BoardException:
            self.placeShip()

    def hit(self):
        try:
            row = randint(0, self.__opponentBoard.size - 1)
            column = randint(0, self.__opponentBoard.size - 1)
            self.__opponentBoard.hit(row, column)
            return row, column
        except BoardException:
            self.hit()
