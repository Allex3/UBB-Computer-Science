from Seminar916.Seminar12.board import PlayerBoard, ComputerBoard
from Seminar916.Seminar12.exceptions import BoardExceptions, GameOverException
from Seminar916.Seminar12.game import ComputerGame
from colorama import Fore, Style

class UI:
    def __init__(self):
        self.__humanBoard = PlayerBoard()
        self.__computerBoard = ComputerBoard()
        self.__computerPlayer = ComputerGame(self.__computerBoard, self.__humanBoard)

    def __place_human_ship(self):
        print("Please place your ship")
        try:
            row = int(input("Row = "))
            column = int(input("Column = "))
            self.__humanBoard.placeShip(row, column)
        except BoardExceptions as be:
            print(be)

    def printBoards(self):
        print(Fore.YELLOW)
        print("The computer's board")
        print(self.__computerBoard)
        print(Style.RESET_ALL)

        print(Fore.GREEN)
        print("The human's board")
        print(self.__humanBoard)
        print(Style.RESET_ALL)

    def startGame(self):
        self.__computerPlayer.placeShip()
        self.__place_human_ship()
        self.printBoards()

        humanTurn = True
        while True:
            if humanTurn == True:
                try:
                    row = int(input("Row = "))
                    column = int(input("Column = "))

                    self.__computerBoard.hit(row, column)
                    humanTurn = False
                    self.printBoards()
                except GameOverException:
                    print("You won !!!!!!")
                    self.printBoards()
                    break
                except BoardExceptions as be:
                    print(be)
            else:
                try:
                    row, column = self.__computerPlayer.hit()
                    print("Computer tried to hit row " + str(row) + " and column " + str(column))
                    humanTurn = True
                    self.printBoards()
                except GameOverException:
                    print("You lost !!!!!!")
                    self.printBoards()
                    break
                except BoardExceptions as be:
                    print(be)

