import unittest
from src.game.game import ConnectFour, ComputerStrategy, DiscsGrid, DiscException, GridException
from src.UI.ApplicationConsole import Application


class TestImportantFunctionalities(unittest.TestCase): # pragma: no cover
    def test_place_disc(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)
        self.assertRaises(GridException, game.place_player, 8, 1)
        self.assertRaises(GridException, game.place_player, -2, 2)
        for _ in range(6):
            game.place_player(1, True)
        self.assertRaises(DiscException, game.place_player, 1, 1)

    def test_full(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)
        for i in range(1, 8):
            for _ in range(6):
                game.place_player(i, 1)

        if game.check_full():
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_column_win(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)

        game.place_player(1, True)
        game.place_player(1, False)
        game.place_player(1, True)
        game.place_player(2, False)
        game.place_player(1, True)
        game.place_player(3, False)
        game.place_player(1, True)
        game.place_player(4, False)
        game.place_player(1, True)
        if game.check_win() == 1:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_row_win(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)

        game.place_player(1, True)
        game.place_player(2, False)
        game.place_player(3, True)
        game.place_player(3, False)
        game.place_player(4, True)
        game.place_player(4, False)
        game.place_player(5, True)
        game.place_player(5, False)
        game.place_player(6, True)
        if game.check_win() == 1:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_check_main_diagonal(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)

        game.place_player(1, True)
        game.place_player(1, False)
        game.place_player(1, True)
        game.place_player(2, False)
        game.place_player(1, True)
        game.place_player(2, False)
        game.place_player(2, True)
        game.place_player(3, False)
        game.place_player(3, True)
        game.place_player(5, False)
        game.place_player(4, True)
        if game.check_win() == 1:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_check_secondary_diagonal(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)

        game.place_player(1, True)
        game.place_player(1, False)
        game.place_player(2, True)
        game.place_player(1, False)
        game.place_player(2, True)
        game.place_player(1, False)
        game.place_player(3, True)
        game.place_player(4, False)
        game.place_player(3, True)
        game.place_player(4, False)
        game.place_player(3, True)
        game.place_player(4, False)
        game.place_player(4, True)
        if game.check_win() == 1:
            self.assertTrue(True)
        else:
            self.assertFalse(True)
    def test_bitboard(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)

        game.place_player(4, True)
        game.place_player(3, False)
        game.place_player(5, True)
        game.place_player(6, False)
        game.place_player(5, True)
        game.place_player(4, False)
        game.place_player(4, True)
        game.place_player(3, False)
        game.place_player(4, True)
        game.place_player(3, False)
        game.place_player(3, True)
        game.place_player(4, False)

        print(game)
        self.assertTrue(grid.get_bitboard() == 4468739801217)

    def test_scoring(self):
        grid = DiscsGrid()
        game = ConnectFour(grid)

        game.place_player(4, True)
        game.place_player(3, False)
        game.place_player(5, True)
        game.place_player(6, False)
        game.place_player(5, True)
        game.place_player(4, False)
        game.place_player(4, True)
        game.place_player(3, False)
        game.place_player(4, True)
        game.place_player(3, False)
        game.place_player(3, True)
        game.place_player(4, False)

        print(game)

        counts_of_2_p1, counts_of_3_p1 = grid.count_discs_connected_of(1)
        counts_of_2_p2, counts_of_3_p2 = grid.count_discs_connected_of(2)

        self.assertEqual(counts_of_2_p1, 7)
        self.assertEqual(counts_of_2_p2, 5)
        self.assertEqual(counts_of_3_p1, 1)
        self.assertEqual(counts_of_3_p2, 1)

if __name__ == '__main__':
    unittest.main()