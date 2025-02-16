from Seminar917.Seminar12.board import PlayerBoard, ComputerBoard
from Seminar917.Seminar12.exceptions import BoardException, GameOver
from Seminar917.Seminar12.game import ComputerGame
from colorama import Fore, Style

class UI:
    def __init__(self):
        self.__humanBoard = PlayerBoard()
        self.__computerBoard = ComputerBoard()
        self.__computerGame = ComputerGame(self.__computerBoard, self.__humanBoard)

    def __placeHumanShip(self):
        print("Please place your ship on the board")
        try:
            row = int(input("Row = "))
            column = int(input("Column = "))
            self.__humanBoard.placeShip(row, column)
        except BoardException as be:
            print(be)
            self.__placeHumanShip()

    def printBoards(self):
        print(Fore.GREEN)
        print("The human's board:")
        print(self.__humanBoard)
        print(Style.RESET_ALL)

        print(Fore.RED)
        print("The computer's board:")
        print(self.__computerBoard)
        print(Style.RESET_ALL)

    def startGame(self):
        self.__computerGame.placeShip()
        self.__placeHumanShip()
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
                except GameOver:
                    print("You won !!!!!!")
                    self.printBoards()
                    break
                except BoardException as be:
                    print(be)
            else:
                try:
                    self.__computerGame.hit()
                    humanTurn = True
                    self.printBoards()
                except GameOver:
                    print("You lost !")
                    self.printBoards()
                    break
                except BoardException as be:
                    print(be)
