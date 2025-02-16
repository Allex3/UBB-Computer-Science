from texttable import Texttable

class Board:
    def __init__(self):
        self.__board = [0] * 9

    def __str__(self):
        """
        Represent the board as a 3x3 grid using Texttable
        :param board: The board
        :return: The string representation of the board
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

    def getBoard(self, x: int, y: int) -> int:
        if x not in (0, 1, 2) or y not in (0, 1, 2):
            raise ValueError("Position is outside the board")
        return self.__board[3 * x + y]

    def moveBoard(self, x: int, y: int, symbol: str):
        """
        Move item on board
        :param board: the board
        :param x: the row on which we want to place the current element
        :param y: the column on which we want to place the current element
        :param symbol: The current element, either 'X' or 'O'
        :return: None
        """
        if symbol.upper() not in ['X', 'O']:
            raise ValueError("Invalid symbol")
        if x not in (0, 1, 2) or y not in (0, 1, 2):
            raise ValueError("Position is outside the board")
        if self.getBoard(x, y) != 0:
            raise ValueError("Position is already occupied")
        if symbol.upper() == "X":
            self.__board[3 * x + y] = 1
        else:
            self.__board[3 * x + y] = -1

    def isBoardWon(self) -> bool:
        for x in range(0, 3):
            s = 0
            for y in range(0, 3):
                s += self.getBoard(x, y)
            if abs(s) == 3:
                return True

        for i in range(0, 3):
            if abs(sum(self.__board[i::3])) == 3:
                return True

        if abs(self.__board[0] + self.__board[4] + self.__board[8]) == 3:
            return True

        if abs(self.__board[2] + self.__board[4] + self.__board[6]) == 3:
            return True

        return False

    def isBoardDraw(self):
        found = True
        for i in range(9):
            if self.__board[i] == 0:
                found = False
                break

        return found

    """
    self.publicMember = 3
    self.__privateMember = 2

    def setPublicObject(self, newValue):
        self.publicMember = newValue

    def setPrivateObject(self, newValue):
        self.__privateMember = newValue

    def getPrivateObject(self):
        return self.__privateMember
    """

if __name__=="__main__":
    """
    board = Board()
    print(board.publicMember)
    board.publicMember = 4
    print(board.publicMember)
    print(board.getPrivateObject())
    board.setPrivateObject(7)
    print(board.getPrivateObject())
    """
    board = Board()
    print(board)



