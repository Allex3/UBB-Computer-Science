import json
import pickle
from random import randint
import os
import mysql.connector

from src.domain.expense import Expense

class MemoryRepository():
    """
    This class is used to store and handle memory instances of the Expense class, the instances being discarded at program exit

    If you need to save the expenses information, you can do so by using the classes derived from this one (ex: TextFileRepository, which stores Expenses in .txt files, etc.)

    Initializes with a random list of n instances of the Expense class, which are also stored outside of the program, if the files to store in are empty.

    Functions
    ---------
    add(day, amount, type) -> Adds an expense to the list _expenses, initialized with the arguments day, amount and type.

    remove(index) -> Removes the Expense at a given index in the list of expenses.

     __generate_expenses(number_of_expenses) -> generates a list of random Expenses

     undo(last_expenses) (Sets the list to a list given as argument (this list is the last list of the history container from the services class.))

     Uses __len__ to return the length of the list of expenses

     Uses __getitem__ to return the expense at a given index from the list of expenses

     Notes
     -----
     These magic methods and the above methods are also used by the classes which inherit from it.
    """
    CREATE_TABLE_STRING = "CREATE TABLE expenses (day varchar(255), amount varchar(255), type varchar(255))"
    DROP_TABLE_STRING = "DROP TABLE expenses"
    def __init__(self, n: int, text_file_path: str = "repository/expenses.txt", binary_file_path: str = "\\repository\\expenses.bin", json_file_path: str = "repository/expenses.json", db_path: str = "repository/expenses.sql"):
        """
        Initializer of the MemoryRepository Class, initializes the list of expenses with some random expenses and inputs them in some files, if they are empty.
        :param n: The number of random expenses to generate
        :param text_file_path: The relative path of the text file
        :param binary_file_path: The relative path of the binary file
        :param json_file_path: The relative path of the json file
        :param db_path: The relative path of the database file
        """
        self._expenses = []
        self.__generate_expenses(n)

        # If the input is 0, it just means we started from a storage file
        if n==0:
            return
        # Fill the text file

        text_file = open(text_file_path, "r")
        if text_file.read() == "": #There are no generated expenses ever, put them in the file
            text_file.close()
            text_file = open(text_file_path, "w")
            for i in range(10):
                text_file.write(f"{str(self._expenses[i])}\n")
        text_file.close()

        # Fill the binary file
        binary_file_path = os.getcwd() + binary_file_path
        if (os.path.getsize(binary_file_path)) == 0:
            binary_file = open(binary_file_path, "wb")
            pickle.dump(self._expenses, binary_file)

        # Fill the JSON File
        json_file = open(json_file_path, "r")
        if json_file.read() == "":
            json_file.close()
            expenses_json = {"expenses": [self.expense_to_json_format(expense) for expense in self._expenses]}
            json_file = open(json_file_path, "w")
            json_file.write(json.dumps(expenses_json, indent=4))
        json_file.close()

        #Fill the database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "alex",
            database = "expenses"
        )
        cursor = mydb.cursor()
        cursor.execute("""SELECT * FROM expenses""")
        if not cursor.fetchone(): #empty table
            try:
                for expense in self._expenses:
                    cursor.execute(f"""INSERT INTO expenses(
            day, amount, type)
             VALUES ({str(expense.day)}, {str(expense.amount)}, '{str(expense.type)}')""")
                mydb.commit()
            except:
                mydb.rollback()
        mydb.close()


    def __getitem__(self, index: int) -> None:
        """
        Magic method to return the Expense at a given index in _expenses, when an object of this class is called like a list, i.e., repo[index]
        :param index: The index of the expense to return
        :return: The expense at that index
        """
        return self._expenses[index]

    @staticmethod
    def expense_to_json_format(expense: Expense) -> dict:
        """
        Returns the json format (dictionary) of an object of class Expense
        :param expense: The expense we are converting
        :return: The JSON format of the expense
        """
        json_expense = {"day": expense.day, "amount": expense.amount, "type": expense.type}
        return json_expense

    def __generate_expenses(self, number_of_expenses: int) -> None:
        """
        A private method to generate n random expenses to put in the list that is empty, in memory
        :param number_of_expenses: The number of expenses to generate
        :return: None
        """
        for index in range(number_of_expenses):
            day = randint(1, 30)
            amount = randint(1, 1000    )
            type = chr(ord("a")+index)
            self.add(day, amount, type)

    def add(self, day: int, amount: int, type: str) -> None:
        """
        Adds a new expense given by its day, amount and type to the list of expenses in memory
        :param day: Day of expense
        :param amount: Amount in money of expense cost
        :param type: Type of expense
        :return: None
        """
        self._expenses.append(Expense(day, amount, type))

    def remove(self, index: int) -> None:
        """
        Removes an Expense at a given index from the list of expenses in memory
        :param index: The index of the expense to be removed
        :return: None
        """
        self._expenses.pop(index)

    def __len__(self) -> int:
        """
        Returns the length of the list of expenses from memory when len() is called on an instance of this class
        :return: The length of the list of expenses from this repository
        """
        return len(self._expenses)

    def undo(self, last_expenses: list[Expense]) -> None:
        """
            Goes back one change made to expenses, the argument is the last list of the history container from the Services class.
            :param last_expenses: The list of expenses without the last change
            :return: None
        """
        self._expenses = last_expenses

class TextFileRepository(MemoryRepository):
    """
    This class handles Expenses stored in a text file, in their string format, each expense string on a line.

    It inherits from the MemoryRepository class, because it makes use of the add() and remove() methods from it, and it also instantiates a list of expenses in memory, that updates at the same time as the text file.
    We work with that list of expenses in memory for Services compatibility, so we make use of the MemoryRepository class methods too.

    However, in this class we have load and save methods, which load the Expenses from the text file into the list of expenses in memory, and, respectively, output the list of expenses from memory into the text file, in string format of each Expense.

    Initializes by loading into a list of expenses from memory, the expenses from the text file found at a given relative path.
    """
    def __init__(self, text_file_path: str = "repository/expenses.txt"):
        """
        The initializer of the class TextFileRepository
        :param text_file_path: The path of the text file we work with
        """
        super().__init__(0)
        self.__text_file_path = text_file_path
        self.__load()

    @staticmethod
    def str_to_expense(str_form: list[str]) -> list:
        """
        Return the expense made from parsing its string form, split into multiple words.
        :param str_form: The list of strings from its string form
        :return: The Expense corresponding to this list of strings.
        """
        return [int(str_form[8]), int(str_form[10]), str_form[3]]

    def __load(self) -> None:
        """
        Loads the expenses from the text file into memory (expenses list)
        :return: None
        """
        with open(self.__text_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                expense_attributes = self.str_to_expense(line.strip("\n").split(" "))
                self._expenses.append(Expense(expense_attributes[0], expense_attributes[1], expense_attributes[2]))
            # Add to the list of expenses the expense made from the string of the line in the file without \n

    def __save(self) -> None:
        """
        Saves the list of expenses from memory into string format in the text file.
        :return: None
        """
        with open(self.__text_file_path, "w") as file:
            for expense in self._expenses:
                file.write(f"{str(expense)}\n") # uses __str__ from Expense class

    def add(self, day: int, amount: int, type: str) -> None:
        """
        Add an expense in the text file of expenses and also in the list of expenses from memory
        :param day: The day of the expense
        :param amount: The amount in money of the expense
        :param type: The type of the expense
        :return: None
        """
        super().add(day, amount, type)
        self.__save()

    def remove(self, index: int) -> None:
        """
        Removes an expense from expenses.txt and also from the list of expenses in the text file repository
        :param index: The index of that expense in the list of expenses from memory.
        :return: None
        """
        super().remove(index)
        self.__save()

    def undo(self, last_expenses: list[Expense]) -> None:
        """
            Goes back one change made to the list of expenses (consequently, modify the file too)
            :param last_expenses: The list of expenses without the last change
            :return: None
        """
        self._expenses = last_expenses
        self.__save()


class BinaryRepository(MemoryRepository):
    """
    This class handles Expenses stored in a binary file using the pickle module.

    It inherits from the MemoryRepository class, because it makes use of the add() and remove() methods from it, and it also instantiates a list of expenses in memory, that updates at the same time as the binary file.
    We work with that list of expenses in memory for Services compatibility, so we make use of the MemoryRepository class methods too.

    However, in this class we have load and save methods, which load the Expenses from the binary file into the list of expenses in memory, and, respectively, output the list of expenses from memory into the binary file, serializing with pickle.

    Initializes by loading into a list of expenses from memory, the expenses from the binary file found at a given relative path.
    """
    def __init__(self, binary_file_path: str = "repository/expenses.bin"):
        """
        The initializer of the class BinaryRepository, loads the contents of the file into memory as a list of expenses.
        :param binary_file_path: The relative path of the binary file we use
        """
        super().__init__(0)
        self.__binary_file_path = binary_file_path
        self.__load()

    def __load(self) -> None:
        """
        Loads into a list of expenses the expenses data stored in a binary file, using pickle.
        :return: None
        """
        try:
            file = open(self.__binary_file_path, "rb")
            self._expenses = pickle.load(file)
            file.close()
        except FileNotFoundError:
            pass

    def __save(self):
        """
        Saves in the binary file the contents of the list of expenses from memory, using serialization with pickle.
        :return: None
        """
        file = open(self.__binary_file_path, "wb")
        pickle.dump(self._expenses, file)
        file.close()

    def add(self, day: int, amount: int, type: str) -> None:
        """
        Add an expense in the binary file of expenses and also in the list of expenses from memory
        :param day: The day of the expense
        :param amount: The amount in money of the expense
        :param type: The type of the expense
        :return: None
        """
        super().add(day, amount, type)
        self.__save()

    def remove(self, index: int) -> None:
        """
        Removes an expense from expenses.bin and also from the list of expenses
        :param index: The index of that expense in the list of expenses from memory
        :return: None
        """
        if not (0<= index < len(self._expenses)):
            raise IndexError("The object you try to remove does not exist.")
        super().remove(index)
        self.__save()

    def undo(self, last_expenses: list[Expense]) -> None:
        """
        Goes back one change made to the list of expenses (consequently, modify the file too)
        :param last_expenses: The list of expenses without the last change
        :return: None
        """
        self._expenses = last_expenses
        self.__save()

class JSONRepository(MemoryRepository):
    """
        This class handles Expenses stored in a JSON file using the JSON module.

        It inherits from the MemoryRepository class, because it makes use of the add() and remove() methods from it, and it also instantiates a list of expenses in memory, that updates at the same time as the JSON file.
        We work with that list of expenses in memory for Services compatibility, so we make use of the MemoryRepository class methods too.

        However, in this class we have load and save methods, which load the Expenses from the JSON file into the list of expenses in memory, and, respectively, output the list of expenses from memory into the JSON file, using the JSON module to format easier.

        Initializes by loading into a list of expenses from memory, the expenses from the JSON file found at a given relative path.
    """
    def __init__(self, json_file_path: str = "repository/expenses.json"):
        """
        The initializer of the JSONRepository class, which loads the expenses from the JSON file into a list of expenses in memory, to work with.
        :param json_file_path: The relative path of the json file
        """
        super().__init__(0)
        self.__json_file_path = json_file_path
        self.__load()

    def __load(self) -> None:
        """
        Load the list of expenses from the JSON file in memory, converting the contents of the file to a dictionary, then to a list of instances of the Expense class
        :return: None
        """
        file = open(self.__json_file_path, "r")
        json_expenses = json.load(file)["expenses"]
        self._expenses = [Expense(int(e["day"]), int(e["amount"]), e["type"]) for e in json_expenses]

    def __save(self) -> None:
        """
        Saves the list of expenses from memory into the json file provided, using a function to convert the expenses into a dictionary of the list of expenses, where the expenses are each a dictionary, so we use the JSON module to convert them.
        :return: None
        """
        expenses_json = {"expenses": [super().expense_to_json_format(expense) for expense in self._expenses]}
        json_file = open(self.__json_file_path, "w")
        json_file.write(json.dumps(expenses_json, indent=4))

    def add(self, day: int, amount: int, type: str) -> None:
        """
        Add an expense in the JSON file and expenses and also in the list of expenses from memory
        :param day: The day of the expense
        :param amount: The amount in money of the expense
        :param type: The type of the expense
        :return: None
        """
        super().add(day, amount, type)
        self.__save()

    def remove(self, index: int) -> None:
        """
        Removes an expense from expenses.json and also from the list of expenses in memory
        :param index: The index of that expense in the list of expenses from memory, that mirrors the JSON data structure to work easier with it
        :return: None
        """
        super().remove(index)
        self.__save()

    def undo(self, last_expenses: list[Expense]) -> None:
        """
            Goes back one change made to the list of expenses (consequently, modify the file too)
            :param last_expenses: The list of expenses without the last change
            :return: None
        """
        self._expenses = last_expenses
        self.__save()

class DBRepository(MemoryRepository):
    """
        This class handles Expenses stored in a DB file using the mysql.connector module.

        It inherits from the MemoryRepository class, because it makes use of the add() and remove() methods from it, and it also instantiates a list of expenses in memory, that updates at the same time as the DB file.
        We work with that list of expenses in memory for Services compatibility, so we make use of the MemoryRepository class methods too.

        However, in this class we have load and save methods, which load the Expenses from the DB file into the list of expenses in memory, and, respectively, output the list of expenses from memory into the DB file, using the JSON module to format easier.

        Initializes by loading into a list of expenses from memory, the expenses from the DB sql file found at a given relative path.
    """
    def __init__(self, db_file_path: str = "repository/expenses.json"):
        """
        The initializer of the DBRepository class, which loads the expenses from the DB sql file into a list of expenses in memory, to work with.
        :param db_file_path: The relative path of the json file
        """
        super().__init__(0)
        self.__db_file_path = db_file_path
        self.__load()

    def __load(self) -> None:
        """
        Load the list of expenses from the JSON file in memory, converting the contents of the file to a dictionary, then to a list of instances of the Expense class
        :return: None
        """

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alex",
            database="expenses"
        )
        if not mydb.is_connected():
            raise ValueError("Cannot connect to database")
        cursor = mydb.cursor()
        cursor.execute("""SELECT * FROM expenses""")
        expenses_table = cursor.fetchall() # get all the rows from the table to output them in memory list
        # The result is a list of tuples!
        for expense_row in expenses_table:
            self._expenses.append(Expense(int(expense_row[0]), int(expense_row[1]), expense_row[2]))
        mydb.close()


    def add(self, day: int, amount: int, type: str) -> None:
        """
        Add an expense in the DB file and also in the list of expenses from memory
        :param day: The day of the expense
        :param amount: The amount in money of the expense
        :param type: The type of the expense
        :return: None
        """
        super().add(day, amount, type)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alex",
            database="expenses"
        )
        cursor = mydb.cursor()
        try:
            cursor.execute(f"""INSERT INTO expenses
VALUES ({day}, {amount}, '{type}')""")
            mydb.commit()
        except:
            mydb.rollback()
        mydb.close()

    def remove(self, index: int) -> None:
        """
        Removes an expense from expenses.json and also from the list of expenses in memory
        :param index: The index of that expense in the list of expenses from memory, that mirrors the JSON data structure to work easier with it
        :return: None
        """
        type_to_remove = self._expenses[index].type
        day_to_remove = self._expenses[index].day
        super().remove(index)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alex",
            database="expenses"
        )
        cursor = mydb.cursor()
        try:
            cursor.execute(f"""DELETE FROM expenses WHERE type = '{type_to_remove}' AND day = {str(day_to_remove)}""")
            mydb.commit()
        except:
            mydb.rollback()
        mydb.close()

    def undo(self, last_expenses: list[Expense]) -> None:
        """
            Goes back one change made to the list of expenses (consequently, modify the file too)
            :param last_expenses: The list of expenses without the last change
            :return: None
        """
        self._expenses = last_expenses
        types = [expense.type for expense in self._expenses]
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alex",
            database="expenses"
        )
        cursor = mydb.cursor()
        cursor.execute("""SELECT * from expenses""")
        rows = cursor.fetchall()
        try:
            for expense in rows: # Remove the expenses that are not in the history
                if not (expense[2].strip("'") in types):
                    cursor.execute(f"""DELETE FROM expenses WHERE type = '{expense[2]}'""")
                    mydb.commit()
            for expense in last_expenses: #add the expenses that are not in the database
                inDB = False
                for db_expense in rows:
                    if expense.day == int(db_expense[0]) and expense.type == db_expense[2].strip("'"):
                        inDB = True
                        break
                if not inDB:
                    cursor.execute(f"""INSERT INTO expenses VALUES({str(expense.day)}, {str(expense.amount)}, '{expense.type}')""")
                    mydb.commit()

        except:
            mydb.rollback()
        mydb.close()