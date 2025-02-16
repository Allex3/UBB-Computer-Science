from seminar.group914.seminar_7.board import create_board, to_str, is_won_board, is_full_board
from seminar.group914.seminar_7.game import move_human, move_computer


def play():
    board = create_board()
    is_player_turn = True

    while True:
        print(to_str(board))

        if is_player_turn:
            move_row = int(input("X="))
            move_col = int(input("Y="))
            move_human(board, move_row, move_col)
        else:
            move_computer(board)

        if is_won_board(board):
            if is_player_turn:
                print("Congratulations!")
            else:
                print("Comiserations!")
            print(to_str(board))
            break
        if is_full_board(board):
            print("Game over!")
            print(to_str(board))
            break

        is_player_turn = not is_player_turn


if __name__ == "__main__":
    play()
