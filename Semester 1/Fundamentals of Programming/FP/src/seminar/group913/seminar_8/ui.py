from seminar.group913.seminar_8.game import Game, RandomComputerMove, SmartComputerMove


class UI:
    def __init__(self):
        # not a smart opponent
        self.__game = Game(RandomComputerMove())
        # yes!
        # self.__game = Game(SmartComputerMove())

    def play(self):
        b = self.__game.get_board()
        is_players_turn = True
        print(b)

        while not (b.is_won() or b.is_full()):
            if is_players_turn:
                try:
                    row = int(input("X="))
                    col = int(input("Y="))
                    self.__game.move_human(row, col)
                except ValueError as ve:
                    print(ve)
                    is_players_turn = not is_players_turn
            else:
                row, col = self.__game.move_computer()
                print(f"Computer played at ({row},{col})")
                print(b)
            is_players_turn = not is_players_turn

        if b.is_won():
            if is_players_turn:
                print("Game over. Computer wins")
            else:
                print("Congrats!")
        elif b.is_full():
            print("It's a draw!")
            print(b)


if __name__ == "__main__":
    ui = UI()
    ui.play()
