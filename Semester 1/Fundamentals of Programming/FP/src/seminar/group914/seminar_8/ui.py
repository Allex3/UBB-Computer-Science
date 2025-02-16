from seminar.group914.seminar_8.game import Game


class UI:
    def __init__(self):
        self.__game = Game()

    def play(self):
        is_player_turn = True
        board = self.__game.get_board()
        while True:
            print(board)

            if is_player_turn:
                move_row = int(input("X="))
                move_col = int(input("Y="))
                self.__game.move_human(move_row, move_col)
            else:
                self.__game.move_computer()

            if board.is_won():
                if is_player_turn:
                    print("Congratulations!")
                else:
                    print("Comiserations!")
                print(board)
                break
            if board.is_full():
                print("Game over!")
                print(board)
                break

            is_player_turn = not is_player_turn


if __name__ == "__main__":
    ui = UI()
    ui.play()
