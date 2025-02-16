from settings import Parser

if __name__ == "__main__":
    parser = Parser("GUI")
    UI = parser.parse_settings()
    UI.open_menu()