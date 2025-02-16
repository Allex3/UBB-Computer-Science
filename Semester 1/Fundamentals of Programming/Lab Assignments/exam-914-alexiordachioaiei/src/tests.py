import unittest
from board import Board, BoardError
from game import Game

class Tests(unittest.TestCase):
    def test_win_row(self):
        board = Board()
        board.place_piece(1, 0, 0)
        board.place_piece(1, 1, 0)
        self.assertTrue(board.get_winner() == 0)
        board.place_piece(1, 2, 0)
        self.assertTrue(board.get_winner() == 1)

    def test_win_column(self):
        board = Board()
        board.place_piece(1, 1, 0)
        board.place_piece(1, 1, 1)
        self.assertTrue(board.get_winner() == 0)
        board.place_piece(1, 1, 2)
        self.assertTrue(board.get_winner() == 1)

    def test_win_diagonals(self):
        board = Board()
        board.place_piece(1, 0, 0)
        board.place_piece(1, 1, 1)
        board.place_piece(1, 2, 2)
        self.assertTrue(board.get_winner() == 1)

        board = Board()
        board.place_piece(1, 0, 2)
        board.place_piece(1, 1, 1)
        board.place_piece(1, 2, 0)
        self.assertTrue(board.get_winner() == 1)

    def test_place_piece(self):
        board = Board()
        self.assertRaises(BoardError, board.place_piece, 1, 0, 4)
        self.assertRaises(BoardError, board.place_piece, 1, 5, 4)
        self.assertRaises(BoardError, board.place_piece, 1, -1, 4)
        self.assertRaises(BoardError, board.place_piece, 1, 0, -1)
if __name__ == "__main__":
    unittest.main()