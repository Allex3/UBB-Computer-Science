from Seminar916.Seminar8.board import Board
from Seminar916.Seminar8.game import ComputerFirstAvailablePosStrategy, Game, ComputerRandomStrategy, \
    ComputerBlockingStrategy


class UI:
    def __init__(self):
        pass

    def printDifficultyLevels(self):
        print("Available difficulty levels:")
        print("1. Easy")
        print("2. Medium")
        print("3. Difficult")

    def start(self):
        board = Board()

        self.printDifficultyLevels()
        diff = int(input("Choose your difficulty level: "))
        if diff == 1:
            computerStrategy = ComputerFirstAvailablePosStrategy(board)
        elif diff == 2:
            computerStrategy = ComputerRandomStrategy(board)
        else:
            computerStrategy = ComputerBlockingStrategy()

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
                    continue
            else:
                game.computerMove()

            if board.isBoardWon() == True:
                if humanTurn == True:
                    print("Congrats! You have won")
                    print(board)
                else:
                    print("The computer has won :(")
                    print(board)
                break
            elif board.isBoardDraw() == True:
                print("We have a draw")
                print(board)

            humanTurn = not humanTurn


if __name__=="__main__":
    ui = UI()
    ui.start()