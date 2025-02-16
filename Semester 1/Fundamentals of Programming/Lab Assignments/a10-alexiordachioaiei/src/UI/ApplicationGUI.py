import pygame
from src.game.game import ConnectFour


class Button:
    def __init__(self, pos, font, big_font, color, hovering_color, text_input):
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.big_font = big_font
        self.color = color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.color)

        # Use the rendered text to get its rectangle positions with the center at the position of the button
        # The left/right/up/bottom of this rectangle are the positions at which we will click the button!
        self.rect = self.text.get_rect(center=(self.x, self.y))

    def update(self, screen):
        screen.blit(self.text, self.rect)

    def check_for_input(self, position: tuple):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True  # Button is clicked
        return False

    def change_if_hovered(self, position: tuple):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):  # Button hovered
            self.text = self.big_font.render(self.text_input, True, self.hovering_color)
            self.rect = self.text.get_rect(center=(self.x, self.y))
        else:
            self.text = self.font.render(self.text_input, True, self.color)
            self.rect = self.text.get_rect(center=(self.x, self.y))


class Column:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.__discs = [0, 0, 0, 0, 0, 0]
        self.HEIGHT = 600
        self.WIDTH = 114  # (798/7)
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)  # Surface
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH,
                                self.HEIGHT)  # The column's position rectangle, that is the same width and height as the surface to represent the destination of the column on the screen
        self.surface.fill((0, 0, 0, 255))  # Make the column surface black
        self.disc_radius = 37
        self.last_row_placed = 6
        self.Y_DISCS = [85, 85*2, 85*3, 85*4, 85*5, 85*6]

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)

    def draw_discs(self):
        for i in range(len(self.__discs)):
            if self.__discs[i] == 0:
                pygame.draw.circle(self.surface, self.WHITE, (self.WIDTH / 2, self.Y_DISCS[i]), self.disc_radius)
            if self.__discs[i] == 1:
                pygame.draw.circle(self.surface, self.RED, (self.WIDTH / 2, self.Y_DISCS[i]), self.disc_radius)
            if self.__discs[i] == 2:
                pygame.draw.circle(self.surface, self.BLUE, (self.WIDTH / 2, self.Y_DISCS[i]), self.disc_radius)

    def update(self, screen):
        self.draw_discs()
        screen.blit(self.surface, self.rect)

    def change_disc(self, column: int, player: bool): # Someone placed a disc
        self.last_row_placed -= 1
        if player:
            self.__discs[self.last_row_placed] = 1
        else:
            self.__discs[self.last_row_placed] = 2

    def check_for_input(self, position: tuple):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True  # Button is clicked
        return False

    def change_if_hovered(self, position: tuple):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):  # Button hovered
            self.surface.fill((0, 0, 0, 200))
        else:
            self.surface.fill((0, 0, 0, 255))


class Application:
    def __init__(self, game: ConnectFour):
        self.__game = game
        pygame.init()

        self.__SCREEN_WIDTH = 1150
        self.__SCREEN_HEIGHT = 600
        self.__FONT = pygame.font.SysFont('Courier', 25, bold=True)
        self.__BIG_FONT = pygame.font.SysFont('Courier', 30, bold=True)

        self.__WHITE = (255, 255, 255)
        self.__PURPLE = (156, 89, 209)
        self.__YELLOW = (252, 244, 52)
        self.__BLACK = (0, 0, 0)

        self.color = self.__YELLOW
        self.hovered_color = self.__WHITE

        self.__POSITIONS = {"QUIT_BUTTON": (self.__SCREEN_WIDTH - 120, self.__SCREEN_HEIGHT - 70),
                            "PLAY_BUTTON": (self.__SCREEN_WIDTH / 2 - 25, self.__SCREEN_HEIGHT / 2 - 15),
                            "PVP": (self.__SCREEN_WIDTH / 2, self.__SCREEN_HEIGHT / 2 - 50),
                            "PVCOMPUTER": (self.__SCREEN_WIDTH / 2, self.__SCREEN_HEIGHT / 2 + 10),
                            "CHOOSE_DIFFICULTY": (250, self.__SCREEN_HEIGHT / 2 - 120),
                            "EASY": (250, self.__SCREEN_HEIGHT / 2 - 60),
                            "MEDIUM": (250, self.__SCREEN_HEIGHT / 2),
                            "HARD": (250, self.__SCREEN_HEIGHT / 2 + 60),
                            "IMPOSSIBLE": (250, self.__SCREEN_HEIGHT / 2 + 120),
                            "DIFFICULTY": (250, self.__SCREEN_HEIGHT / 2 + 180),
                            "CHOOSE_PLAYER": (700, self.__SCREEN_HEIGHT / 2 - 120),
                            "PLAYER_1": (700, self.__SCREEN_HEIGHT / 2 - 60),
                            "PLAYER_2": (700, self.__SCREEN_HEIGHT / 2),
                            "PLAY_AS": (700, self.__SCREEN_HEIGHT / 2 + 180),
                            "START": (950, self.__SCREEN_HEIGHT / 2),
                            "COLUMN_1": (0, 0),
                            "COLUMN_2": (114, 0),
                            "COLUMN_3": (114 * 2, 0),
                            "COLUMN_4": (114 * 3, 0),
                            "COLUMN_5": (114 * 4, 0),
                            "COLUMN_6": (114 * 5, 0),
                            "COLUMN_7": (114 * 6, 0),
                            "COMPUTER_WIN": (114*8+60, 200),
                            "PLAYER_WIN": (114*8+60, 200),
                            "DRAW": (114*8+60, 200),
                            "COMPUTER_WIN_SECOND": (114*8+60, 225),
                            "PLAYER_WIN_SECOND": (114*8+60, 225),
                            "DRAW_SECOND": (114*8+60, 225)}

        self.__COMPUTER_WIN_BUTTON_ON = False
        self.__PLAYER_WIN_BUTTON_ON = False
        self.__DRAW_BUTTON_ON = False
        self.__GAME_ENDED = False

        self.__MAIN_BUTTONS = {}
        self.__CONFIG_BUTTONS = {}
        self.__COLUMN_BUTTONS = {}
        self.__GAME_BUTTONS = {}

        self.__difficulty = "Difficulty: Not selected"
        self.__you_play_as = "You play: Not selected"

        self.__screen = pygame.display.set_mode((self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT))

    def __create_main_GUI(self):
        self.__MAIN_BUTTONS["QUIT"] = Button(self.__POSITIONS["QUIT_BUTTON"], self.__FONT, self.__BIG_FONT,
                                             self.color, self.hovered_color, "Quit")

        self.__MAIN_BUTTONS["PLAY"] = Button(self.__POSITIONS["PLAY_BUTTON"], self.__FONT, self.__BIG_FONT,
                                             self.color, self.hovered_color, "Play")

    def __create_config_GUI(self):
        self.__CONFIG_BUTTONS["CHOOSE_DIFFICULTY"] = Button(self.__POSITIONS["CHOOSE_DIFFICULTY"], self.__FONT,
                                                            self.__BIG_FONT, self.color, self.hovered_color,
                                                            "Choose difficulty")

        self.__CONFIG_BUTTONS["EASY"] = Button(self.__POSITIONS["EASY"], self.__FONT, self.__BIG_FONT, self.color,
                                               self.hovered_color, "Easy")

        self.__CONFIG_BUTTONS["MEDIUM"] = Button(self.__POSITIONS["MEDIUM"], self.__FONT, self.__BIG_FONT,
                                                 self.color,
                                                 self.hovered_color, "Medium")
        self.__CONFIG_BUTTONS["HARD"] = Button(self.__POSITIONS["HARD"], self.__FONT, self.__BIG_FONT, self.color,
                                               self.hovered_color, "Hard")
        self.__CONFIG_BUTTONS["IMPOSSIBLE"] = Button(self.__POSITIONS["IMPOSSIBLE"], self.__FONT, self.__BIG_FONT,
                                                     self.color,
                                                     self.hovered_color, "Impossible")

        self.__CONFIG_BUTTONS["CHOOSE_PLAYER"] = Button(self.__POSITIONS["CHOOSE_PLAYER"], self.__FONT, self.__BIG_FONT,
                                                        self.color, self.hovered_color, "Choose your player:")

        self.__CONFIG_BUTTONS["PLAYER_1"] = Button(self.__POSITIONS["PLAYER_1"], self.__FONT, self.__BIG_FONT,
                                                   self.color, self.hovered_color, "Player 1")

        self.__CONFIG_BUTTONS["PLAYER_2"] = Button(self.__POSITIONS["PLAYER_2"], self.__FONT, self.__BIG_FONT,
                                                   self.color, self.hovered_color, "Player 2")

        self.__CONFIG_BUTTONS["START"] = Button(self.__POSITIONS["START"], self.__FONT, self.__BIG_FONT, self.color,
                                                self.hovered_color, "Start")

        self.__CONFIG_BUTTONS["DIFFICULTY"] = Button(self.__POSITIONS["DIFFICULTY"], self.__FONT, self.__BIG_FONT,
                                                     self.color, self.hovered_color, self.__difficulty)

        self.__CONFIG_BUTTONS["PLAY_AS"] = Button(self.__POSITIONS["PLAY_AS"], self.__FONT, self.__BIG_FONT,
                                                  self.color, self.hovered_color, self.__you_play_as)

    def __create_game_GUI(self):
        self.__COLUMN_BUTTONS["COLUMN_1"] = Column(self.__POSITIONS["COLUMN_1"])
        self.__COLUMN_BUTTONS["COLUMN_2"] = Column(self.__POSITIONS["COLUMN_2"])
        self.__COLUMN_BUTTONS["COLUMN_3"] = Column(self.__POSITIONS["COLUMN_3"])
        self.__COLUMN_BUTTONS["COLUMN_4"] = Column(self.__POSITIONS["COLUMN_4"])
        self.__COLUMN_BUTTONS["COLUMN_5"] = Column(self.__POSITIONS["COLUMN_5"])
        self.__COLUMN_BUTTONS["COLUMN_6"] = Column(self.__POSITIONS["COLUMN_6"])
        self.__COLUMN_BUTTONS["COLUMN_7"] = Column(self.__POSITIONS["COLUMN_7"])

        self.__GAME_BUTTONS["COMPUTER_WIN"] = Button(self.__POSITIONS["COMPUTER_WIN"], self.__FONT, self.__BIG_FONT, self.color, self.hovered_color, "Computer won! Better")
        self.__GAME_BUTTONS["PLAYER_WIN"] = Button(self.__POSITIONS["PLAYER_WIN"], self.__FONT, self.__BIG_FONT,
                                                     self.color, self.hovered_color,
                                                     "Player won! The AI")

        self.__GAME_BUTTONS["DRAW"] = Button(self.__POSITIONS["DRAW"], self.__FONT, self.__BIG_FONT,
                                                     self.color, self.hovered_color,
                                                     "It is a draw!")

        self.__GAME_BUTTONS["COMPUTER_WIN_SECOND"] = Button(self.__POSITIONS["COMPUTER_WIN_SECOND"], self.__FONT, self.__BIG_FONT,
                                                     self.color, self.hovered_color,
                                                     "luck next time :3")
        self.__GAME_BUTTONS["PLAYER_WIN_SECOND"] = Button(self.__POSITIONS["PLAYER_WIN_SECOND"], self.__FONT, self.__BIG_FONT,
                                                   self.color, self.hovered_color,
                                                   "won't overtake us :3")

        self.__GAME_BUTTONS["DRAW_SECOND"] = Button(self.__POSITIONS["DRAW_SECOND"], self.__FONT, self.__BIG_FONT,
                                             self.color, self.hovered_color,
                                             "You're good :3")

    def __create_GUI(self):
        self.__create_main_GUI()
        self.__create_config_GUI()
        self.__create_game_GUI()

    def __set_difficulty(self, difficulty: str):
        match difficulty:
            case "Easy":
                self.__game.set_difficulty(5)
            case "Medium":
                self.__game.set_difficulty(8)
            case "Hard":
                self.__game.set_difficulty(10)
            case "Impossible":
                self.__game.set_difficulty(12)

        self.__difficulty = "Difficulty: " + difficulty
        self.__CONFIG_BUTTONS["DIFFICULTY"].text_input = self.__difficulty

    def __set_computer_turn(self, turn: bool):
        self.__AI_TURN = turn
        self.__PLAYER = not turn
        self.__game.set_computer_turn(turn)
        if turn:
            self.__you_play_as = "You play: Player 2"
        if not turn:
            self.__you_play_as = "You play: Player 1"

        self.__CONFIG_BUTTONS["PLAY_AS"].text_input = self.__you_play_as

    def __game_loop(self):
        pygame.display.set_caption("Game")
        self.__game.set_computer_strategy()
        if self.__AI_TURN: # AI plays first , calculate the moves first
            column = self.__game.place_computer()
            self.__COLUMN_BUTTONS["COLUMN_" + str(column)].change_disc(column, self.__AI_TURN)

        while True:
            mouse = pygame.mouse.get_pos()

            self.__screen.fill(self.__PURPLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.__MAIN_BUTTONS["QUIT"].check_for_input(mouse):
                        pygame.quit()

                    for column in self.__COLUMN_BUTTONS:
                        if self.__COLUMN_BUTTONS[column].check_for_input(mouse) and not self.__GAME_ENDED:
                            # Enter if we click a column and game did not end

                            column_number = int(column.split("_")[1])
                            self.__game.place_player(column_number, self.__PLAYER)
                            self.__COLUMN_BUTTONS[column].change_disc(column_number, self.__PLAYER)

                            check_win = self.__game.check_win()
                            if self.__PLAYER and check_win == 1: # Player is player 1 and they won
                                self.__PLAYER_WIN_BUTTON_ON = True
                                self.__GAME_ENDED = True
                            if not self.__PLAYER and check_win == 2:
                                self.__PLAYER_WIN_BUTTON_ON = True
                                self.__GAME_ENDED = True

                            if self.__game.check_full():
                                self.__DRAW_BUTTON_ON = True
                                self.__GAME_ENDED = True

                            # You did not win, let the computer play and check its win
                            column = self.__game.place_computer()
                            self.__COLUMN_BUTTONS["COLUMN_" + str(column)].change_disc(column, self.__AI_TURN)

                            check_win = self.__game.check_win()
                            if check_win == 1 and self.__AI_TURN: # AI is player 1 and it won
                                self.__COMPUTER_WIN_BUTTON_ON = True
                                self.__GAME_ENDED = True
                            if check_win == 2 and not self.__AI_TURN: # Ai is player 2 and it won
                                self.__COMPUTER_WIN_BUTTON_ON = True
                                self.__GAME_ENDED = True

                            if self.__game.check_full():
                                self.__DRAW_BUTTON_ON = True
                                self.__GAME_ENDED = True


            for column in self.__COLUMN_BUTTONS.values():
                column.change_if_hovered(mouse)
                column.update(self.__screen)

            if self.__PLAYER_WIN_BUTTON_ON:
                self.__GAME_BUTTONS["PLAYER_WIN"].change_if_hovered(mouse)
                self.__GAME_BUTTONS["PLAYER_WIN"].update(self.__screen)
                self.__GAME_BUTTONS["PLAYER_WIN_SECOND"].change_if_hovered(mouse)
                self.__GAME_BUTTONS["PLAYER_WIN_SECOND"].update(self.__screen)

            if self.__COMPUTER_WIN_BUTTON_ON:
                self.__GAME_BUTTONS["COMPUTER_WIN"].change_if_hovered(mouse)
                self.__GAME_BUTTONS["COMPUTER_WIN"].update(self.__screen)
                self.__GAME_BUTTONS["COMPUTER_WIN_SECOND"].change_if_hovered(mouse)
                self.__GAME_BUTTONS["COMPUTER_WIN_SECOND"].update(self.__screen)

            if self.__DRAW_BUTTON_ON:
                self.__GAME_BUTTONS["DRAW"].change_if_hovered(mouse)
                self.__GAME_BUTTONS["DRAW"].update(self.__screen)
                self.__GAME_BUTTONS["DRAW_SECOND"].change_if_hovered(mouse)
                self.__GAME_BUTTONS["DRAW_SECOND"].update(self.__screen)

            self.__MAIN_BUTTONS["QUIT"].change_if_hovered(mouse)
            self.__MAIN_BUTTONS["QUIT"].update(self.__screen)

            pygame.display.update()

    def __start_menu(self):
        pygame.display.set_caption("Start Menu")

        while True:
            mouse = pygame.mouse.get_pos()

            self.__screen.fill(self.__PURPLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__CONFIG_BUTTONS["EASY"].check_for_input(mouse):
                        self.__set_difficulty("Easy")
                    if self.__CONFIG_BUTTONS["MEDIUM"].check_for_input(mouse):
                        self.__set_difficulty("Medium")
                    if self.__CONFIG_BUTTONS["HARD"].check_for_input(mouse):
                        self.__set_difficulty("Hard")
                    if self.__CONFIG_BUTTONS["IMPOSSIBLE"].check_for_input(mouse):
                        self.__set_difficulty("Impossible")

                    if self.__CONFIG_BUTTONS["PLAYER_1"].check_for_input(mouse):
                        self.__set_computer_turn(False)

                    if self.__CONFIG_BUTTONS["PLAYER_2"].check_for_input(mouse):
                        self.__set_computer_turn(True)

                    if self.__CONFIG_BUTTONS["START"].check_for_input(mouse):
                        if self.__difficulty == "Difficulty: Not selected":
                            continue
                        if self.__you_play_as ==  "You play: Not selected":
                            continue
                        # If difficulty and player are not selected do not do anything

                        self.__game_loop()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__main_menu()

            for button in self.__CONFIG_BUTTONS.values():
                button.change_if_hovered(mouse)
                button.update(self.__screen)

            pygame.display.update()

    def __main_menu(self):
        pygame.display.set_caption("Main Menu")

        while True:
            mouse = pygame.mouse.get_pos()

            self.__screen.fill(self.__PURPLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.__MAIN_BUTTONS["QUIT"].check_for_input(mouse):
                        pygame.quit()

                    if self.__MAIN_BUTTONS["PLAY"].check_for_input(mouse):
                        self.__start_menu()

            for button in self.__MAIN_BUTTONS.values():
                button.change_if_hovered(mouse)
                button.update(self.__screen)

            # Updates game frames
            pygame.display.update()

    def run(self):

        self.__create_GUI()

        self.__main_menu()
