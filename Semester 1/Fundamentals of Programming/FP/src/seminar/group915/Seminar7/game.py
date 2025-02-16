from Seminar915.Seminar7.board import moveBoard, getBoard
from random import randint

def humanMove(board, x: int, y: int):
    moveBoard(board, x, y, 'X')

def computerMove(board):
    x, y = getNextComputerMove(board)
    moveBoard(board, x, y, 'O')

def getNextComputerMove(board):
    """
    Decides where the computer places its next move
    TODO: Implement a version that prevents human's moves
    :param board: the board
    :return: x, y - the positions of the next move
    """
    found = False
    while not found:
        x = randint(0, 2)
        y = randint(0, 2)

        if getBoard(board, x, y) == 0:
            return x, y

