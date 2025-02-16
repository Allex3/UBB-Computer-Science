from texttable import Texttable

class Board:
    def __init__(self):
        self.__board = [0] * 9

    def __str__(self) -> str:
        """
        Represents the board as a 3x3 grid using Texttables
        :param board: the board
        :return: the required string representation
        """

        table = Texttable()
        table.set_cols_align(["c", "c", "c"])

        formattedTable = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = self.__board[3 * i + j]

                if cell == -1:
                    row.append('O')
                elif cell == 1:
                    row.append('X')
                else:
                    row.append(' ')
            formattedTable.append(row)

        table.add_rows(formattedTable, header=False)
        return table.draw()

    def getBoardValue(self, x: int, y: int) -> int:
        if x not in (0, 1, 2) or y not in (0, 1, 2):
            raise ValueError("Position is not on the board")

        return self.__board[3 * x + y]

    def moveBoard(self, x: int, y: int, symbol: str):
        """
        Makes a move on the board
        :param board: the given board
        :param x: the row on which we want to make the move
        :param y: the column on which we want to make the move
        :param symbol: the symbol we want to place at position (x, y) - should be either 'X' or 'O'
        :return: None
        """

        if symbol.upper() not in ['X', 'O']:
            raise ValueError("Symbol should be X or O")
        if x not in (0, 1, 2) or y not in (0, 1, 2):
            raise ValueError("Position is not on the board")
        if self.getBoardValue(x, y) != 0:
            raise ValueError("Invalid position. We already have something there")

        if symbol.upper() == 'X':
            self.__board[3 * x + y] = 1
        else:
            self.__board[3 * x + y] = -1

    def isBoardWon(self) -> bool:
        """
        Verifies if the board has been won
        :param board:
        :return:
        """

        # check the rows
        for i in range(0, 9, 3):  # 0, 3, 6
            if abs(sum(self.__board[i:i + 3])) == 3:
                return True

        # check the columns
        for i in range(3):
            if abs(sum(self.__board[i::3])) == 3:
                return True

        # check the diagonals
        if abs(self.__board[0] + self.__board[4] + self.__board[8]) == 3:
            return True
        if abs(self.__board[2] + self.__board[4] + self.__board[6]) == 3:
            return True

        return False

    def isBoardDraw(self) -> bool:
        found = True
        for i in range(9):
            if self.__board[i] == 0:
                found = False
                break

        return found

    """
    def getPrivateMember(self):
        return self.__board3

    def setPrivateMember(self, newValue):
        self.__board3 = newValue
    """


if __name__=="__main__":
    """
    board = Board()
    board.board1[3] = 1
    print(board.board1)
    print(board.getPrivateMember())
    board.setPrivateMember(19)
    print(board.getPrivateMember())
    """
    board = Board()
    print(board)


