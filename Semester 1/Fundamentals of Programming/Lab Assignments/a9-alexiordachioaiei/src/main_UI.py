"""
Main file of project
My problem: 2
"""

"""
Application/UI = Client
Console = Invoker
Commands = Command classes that take methods from the Services and the receiver to run on
Services = The logic to run along with a receiver on those methods
Repository = List of objects we work on with the logic in Services CRUD
Domain = Objects which we store and move around
"""

from src.settings import Parser
if __name__ == "__main__":
    parser = Parser("UI")
    UI = parser.parse_settings()
    UI.open_menu()
