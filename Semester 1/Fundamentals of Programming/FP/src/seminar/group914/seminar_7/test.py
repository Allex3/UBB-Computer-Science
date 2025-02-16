from seminar.group914.seminar_7.board import create_board, is_won_board, is_full_board, move_board, get_symbol_board


# import seminar.group914.seminar_7.board

def test_board():
    b = create_board()

    assert is_won_board(b) is False
    assert is_full_board(b) is False

    move_board(b, 'X', 1, 1)
    assert get_symbol_board(b, 1, 1) == 'X'
    # TODO write more tests
