from random import randint

from Seminar915.Seminar12.board import BoardExceptions


class ComputerPlayer:
    def __init__(self, ownBoard, opponentBoard):
        self.__ownBoard = ownBoard
        self.__opponentBoard = opponentBoard

    def placeShip(self):
        try:
            row = randint(0, self.__ownBoard.size - 1)
            column = randint(0, self.__ownBoard.size - 3)
            self.__ownBoard.placeShip(row, column)
        except BoardExceptions:
            self.placeShip()

    def hit(self):
        row = randint(0, self.__ownBoard.size - 1)
        column = randint(0, self.__ownBoard.size - 1)
        self.__opponentBoard.hit(row, column)
        return row, column