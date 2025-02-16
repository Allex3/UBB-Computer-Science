from Seminar915.Seminar12.board import PlayerBoard, ComputerBoard, BoardExceptions, GameOverException
from Seminar915.Seminar12.game import ComputerPlayer
from colorama import Fore, Style

class UI:
    def __init__(self):
        self.__playerBoard = PlayerBoard()
        self.__computerBoard = ComputerBoard()
        self.__computerPlayer = ComputerPlayer(self.__computerBoard, self.__playerBoard)

    def __placePlayerBattleship(self):
        print("Please place your ship: ")
        try:
            row = int(input("Row = "))
            column = int(input("Column = "))
            self.__playerBoard.placeShip(row, column)
        except BoardExceptions as be:
            print(be)
            self.__placePlayerBattleship()

    def printBoards(self):
        print(Fore.BLUE)
        print("The computer's board")
        print(self.__computerBoard)
        print(Style.RESET_ALL)

        print(Fore.GREEN)
        print("Your board")
        print(self.__playerBoard)
        print(Style.RESET_ALL)

    def startGame(self):
        self.__placePlayerBattleship()
        self.__computerPlayer.placeShip()
        print("Initial boards")
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
                    print("You won !!!!! ")
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
                except BoardExceptions as be:
                    print(be)