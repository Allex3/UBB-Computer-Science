from lecture.livecoding.lecture_12.chomp_board import InvalidMoveException, GameOverException
from lecture.livecoding.lecture_12.chomp_game import ChompGame, RandomMoveStrategy


class ChompUI:
    def __init__(self):
        # TODO It's much better to receive constructor parameters instead of hard coding, as that
        # allows us to change them without touching the code of this class => dependency injection
        self.__game = ChompGame(RandomMoveStrategy())

    def start(self):
        print("The board")
        print(self.__game.board)

        humans_turn = True

        while True:
            try:
                if humans_turn:
                    move = input("Where to move (e.g. D2) ->")
                    # C4 -> C is the column, 4 is the row
                    row = int(move[1]) - 1
                    column = ord(move[0].upper()) - ord('A')  # ASCII code subtraction
                    self.__game.human_move(row, column)
                else:
                    move = self.__game.computer_move()
                    print(f"Computer moved at ({move[0]},{move[1]})")
                    print(self.__game.board)
                humans_turn = not humans_turn
            except ValueError as ve:
                print(ve)
                humans_turn = True
            except InvalidMoveException as ime:
                print(ime)
                humans_turn = True
            except GameOverException:
                if humans_turn:
                    print("Loser!")
                else:
                    print("oops!")
                print(self.__game.board)
                break


ui = ChompUI()
ui.start()
