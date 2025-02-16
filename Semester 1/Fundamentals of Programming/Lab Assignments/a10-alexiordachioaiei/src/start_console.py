from src.UI.ApplicationConsole import Application
from src.game.game import ConnectFour
from src.board.grid import DiscsGrid

if __name__ == '__main__':
    grid = DiscsGrid()
    game = ConnectFour(grid)
    UI = Application(game)
    UI.run()