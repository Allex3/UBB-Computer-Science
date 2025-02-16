from src.services.services import Services

class UI():
    def __init__(self):
        settings = open("settings.properties", "r")
        self.__type_of_repo = settings.read()
        settings.close()
        if self.__type_of_repo not in ["memory", "JSON", "binary", "text", "database"]:
            print("This type of repository does not exist. Please change the input of the settings.properties file. It can only be: memory, text, binary, JSON, database.")
            exit(1)
        try:
            if self.__type_of_repo == "memory":
                self.__services = Services(self.__type_of_repo, "repository/expenses.txt", "\\repository\\expenses.bin", "repository/expenses.json", "repository/expenses.sql")
            else:
                self.__services = Services(self.__type_of_repo, "repository/expenses.txt", "repository/expenses.bin",
                                           "repository/expenses.json", "repository/expenses.sql")
        except ValueError as e:
            print(e)
            exit(2)
        self.__commands = ["1. Add an expense. Expense data is read from the console.",
                           "2. Display the list of expenses.",
                           "3. Filter the list so that it contains only expenses above a certain value read from the console.",
                           "4. Undo the last operation that modified program data. This step can be repeated. The user can undo only those operations made during the current run of the program.",
                           "5. Exit"]

    def display_expenses(self):
        for expense in self.__services.repository:
            print(expense)

    ADD = "1"
    DISPLAY = "2"
    FILTER = "3"
    UNDO = "4"
    EXIT = "5"

    def menu(self) -> None:
        print("Manage a list of expenses.")
        for command in self.__commands:
            print(command)
        while (True):
            option = input("> ")
            match option:
                case self.ADD:
                    expense = input("<day> <amount> <type>: ")
                    expense = expense.strip().split(" ")
                    if len(expense) != 3:
                        print("Invalid expense input!")
                        continue
                    try:
                        day = int(expense[0])
                        amount = int(expense[1])
                        type = expense[2]
                    except ValueError:
                        print("Day and amount should be integers!")
                        continue

                    try:
                        self.__services.add_expense(day, amount, type)
                    except Exception as e:
                        print(e)
                case self.DISPLAY:
                    self.display_expenses()
                case self.FILTER:
                    try:
                        filter_above = int(input("<filter>: "))
                    except ValueError:
                        print("The filter should be a positive integer.")
                        continue
                    self.__services.filter_above(filter_above)
                case self.UNDO:
                    try:
                        self.__services.undo()
                    except IndexError as e:
                        print(e)
                case self.EXIT:
                    exit(0)
                case _:
                    print("Invalid input")

