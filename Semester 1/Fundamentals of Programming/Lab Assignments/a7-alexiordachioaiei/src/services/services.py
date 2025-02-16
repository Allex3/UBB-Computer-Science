from random import randint

from ..repository.repository import MemoryRepository, TextFileRepository, BinaryRepository, JSONRepository, DBRepository


class Services():
    def __init__(self, type_of_repo:str, text_file_name: str, binary_file_name: str, json_file_name: str, db_name: str):
        match type_of_repo:
            case "memory":
                self.repository = MemoryRepository(10, text_file_name, binary_file_name, json_file_name, db_name) # For the initial loading send the file names
            case "text":
                self.repository = TextFileRepository(text_file_name)
            case "binary":
                self.repository = BinaryRepository(binary_file_name)
            case "JSON":
                self.repository = JSONRepository(json_file_name)
            case "database":
                self.repository = DBRepository()
            case _:
                raise ValueError("This repository type does not exist.")
        self.__history = [] # the changes made to the repository list in memory ONLY TAKEN IN THE CURRENT RUN
        # So all the lists of expenses before any change, for the undo command

    @property
    def history(self):
        return self.__history

    def add_expense(self, day: int, amount: int, type: str) -> None:
        self.__history.append([expense for expense in self.repository])
        self.repository.add(day, amount, type) # Add the expense of day, amount, type to repo

    def filter_above(self, filter_above: int) -> None:
        # Using __getitem__ in each type of repository for the expense list

        # In any repository, the list of expenses is the same
        # And is made at the instantiation of an object of the class, when you parse the extern files
        # What differs is how elements are added, you not only add to expense_list, but also to the file
        # And removed, also from the file
        # It is better this way so as not to implement getters and setters for expense_list
        # When we talk about other types of repositories

        number_of_expenses = len(self.repository)
        index = 0
        self.__history.append([expense for expense in self.repository])
        while(index < number_of_expenses):
            if self.repository[index].amount < filter_above:
                self.repository.remove(index)
                number_of_expenses-=1
                index-=1
            index+=1

    def undo(self):
        if not self.__history:
            raise IndexError("Cannot undo. There is no history.")
        self.repository.undo(self.__history.pop())



