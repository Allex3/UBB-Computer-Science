import random

from lecture.livecoding.lecture_12.chomp_board import ChompBoard, ChompSymbol


class ChompStrategy:
    """
    This is the base class of the Strategy design pattern for making computer moves

    """

    def play(self, board: ChompBoard) -> tuple:
        raise NotImplementedError("Supposedly an abstract class :)")


class RandomMoveStrategy(ChompStrategy):
    def play(self, board: ChompBoard) -> tuple:
        if len(board.free_squares) == 0:
            board.chomp(ChompSymbol.O, 0, 0)
        move = random.choice(board.free_squares)
        board.chomp(ChompSymbol.O, move[0], move[1])
        return move


class ChompGame:
    def __init__(self, computer_strategy: ChompStrategy):
        # TODO board size from the UI !?
        self.__board = ChompBoard()
        self.__strategy = computer_strategy

    def computer_move(self) -> tuple:
        """
        We use the Strategy design pattern here
        https://refactoring.guru/design-patterns/strategy

        What are design patterns?
        1. When writing larger programs there are some problems that show up again and again ...
            examples:
                going over every elements of a list, tuple, dict -> Iterator (in Python, __next__, __iter__)
                make the program do something, but at an unspecified point in the future -> Command (undo/redo in A9)
                have the same single object accessible from the entire program -> Singleton
                remember the state of things and revert to them when necessary -> Memento (undo/redo the first implementation)

                encode an algorithm (/way of doing things) inside a class and use it; if we want to change
                the way we do things, we change the class -> Strategy

                In our program, each computer player difficulty is encoded in its own class


        2. Layered architecture is also a design pattern :) but high-level one
        """
        return self.__strategy.play(self.board)

    def human_move(self, row: int, column: int):
        self.__board.chomp(ChompSymbol.X, row, column)

    @property
    def board(self):
        return self.__board


if __name__ == "__main__":
    game = ChompGame(RandomMoveStrategy())
    print(game.board)
    game.human_move(2, 3)
    game.computer_move()
    print(game.board)
