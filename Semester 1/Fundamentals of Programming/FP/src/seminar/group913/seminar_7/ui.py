from seminar.group913.seminar_7.board import create_board, to_str_board, is_won_board, is_full_board
from seminar.group913.seminar_7.game import move_human, move_computer


def play():
    board = create_board()
    is_players_turn = True
    print(to_str_board(board))

    while not (is_won_board(board) or is_full_board(board)):
        if is_players_turn:
            try:
                row = int(input("X="))
                col = int(input("Y="))
                move_human(board, row, col)
            except ValueError as ve:
                print(ve)
                is_players_turn = not is_players_turn
        else:
            row, col = move_computer(board)
            print(f"Computer played at ({row},{col})")
            print(to_str_board(board))
        is_players_turn = not is_players_turn

    # FIXME !
    if is_full_board(board):
        print("Game over. It's a draw!")

    if is_won_board(board):
        if is_players_turn:
            print("Game over. Computer wins")
        else:
            print("Congrats!")
    print(to_str_board(board))


play()
