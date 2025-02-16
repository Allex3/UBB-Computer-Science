from Seminar916.Seminar7.board import createBoard, toString, isBoardWon, isBoardDraw
from Seminar916.Seminar7.game import humanMove, computerMove


def start():
    board = createBoard()
    humanTurn = True

    while True:
        print(toString(board))

        if humanTurn == True:
            try:
                x = int(input("x = "))
                y = int(input("y = "))
                humanMove(board, x, y)
            except ValueError as ve:
                print(ve)
                continue
        else:
            computerMove(board)

        if isBoardWon(board) == True:
            if humanTurn == True:
                print("Congrats! You have won")
            else:
                print("The computer has won :(")
            break
        elif isBoardDraw(board) == True:
            print("We have a draw")

        humanTurn = not humanTurn

start()