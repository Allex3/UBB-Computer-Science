from random import randint

from Seminar916.Seminar7.board import moveBoard, getBoardValue


def humanMove(board, x : int, y: int):
    moveBoard(board, x, y, 'X')

def getNextComputerMove(board):
    # TODO: Implement a more complex algorithm such that it might prevent the next moves of the human
    found = False

    while not found:
        x = randint(0, 2)
        y = randint(0, 2)

        if getBoardValue(board, x, y) == 0:
            return x, y

def computerMove(board):
    x, y = getNextComputerMove(board)
    moveBoard(board, x, y, 'O')

