from Seminar915.Seminar8.board import Board
from Seminar915.Seminar8.game import Game, ComputerFirstPositionStrategy, ComputerRandomStrategy


class UI:
    def __init__(self):
        pass

    def printDifficulty(self):
        print("Available difficulties:")
        print("1. Easy")
        print("2. Medium")
        print("3. Difficult")

    def start(self):
        self.printDifficulty()
        diff = int(input("Choose your difficulty level: "))

        board = Board()
        if diff == 1:
            computerStrategy = ComputerFirstPositionStrategy(board)
        elif diff == 2:
            computerStrategy = ComputerRandomStrategy(board)
        else:
            pass

        game = Game(board, computerStrategy)
        humanTurn = True

        while True:
            print(board)

            if humanTurn == True:
                try:
                    x = int(input("x = "))
                    y = int(input("y = "))
                    game.humanMove(x, y)
                except ValueError as ve:
                    print(ve)
            else:
                game.computerMove()

            if board.isBoardWon() == True:
                if humanTurn == True:
                    print("You have won !!!!!!!")
                else:
                    print("The computer has won ! :(")
                print(board)
                break
            elif board.isBoardDraw() == True:
                print("We have a a draw")
                break

            humanTurn = not humanTurn

if __name__=="__main__":
    ui = UI()
    ui.start()
