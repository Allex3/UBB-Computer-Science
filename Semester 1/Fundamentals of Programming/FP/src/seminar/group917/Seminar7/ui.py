from Seminar917.Seminar7.board import createBoard, toString, isBoardWon, isBoardDraw
from Seminar917.Seminar7.game import humanMove, computerMove


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
                print("Congrats! You won !!!")
                print(toString(board))
            else:
                print("The computer has won! :(")
                print(toString(board))
            break
        elif isBoardDraw(board) == True:
            print("We have a draw!!!!")
            break

        humanTurn = not humanTurn

start()