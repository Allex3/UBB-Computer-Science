class FunctionCall:
    def __init__(self, function, *params):
        self.__function = function
        self.__params = params

    def call(self):
        # () - call operator in Python
        self.__function(*self.__params)

    # def __call__(self, *args, **kwargs):
    #     self.call()


class Operation:
    def __init__(self, function_undo: FunctionCall, function_redo: FunctionCall):
        self.__function_undo = function_undo
        self.__function_redo = function_redo

    def undo(self):
        self.__function_undo.call()

    def redo(self):
        self.__function_redo.call()


class UndoService:
    def __init__(self):
        # this is the list of how to undo/redo all program operations
        # each element is an Operation object, which can both undo() and redo()
        self.__history = []
        # index is where we are in the operations history list
        self.__index = 0

    def record(self, operation: Operation):
        # TODO After at least one undo operation, the __index is no longer at the end of the operations
        # list. This means that when we record an operation for undo/redo, we need to delete all list
        # elements with an index > __index (when a non undo/redo operation takes place, the redo history
        # is invalidated)
        self.__history.append(operation)
        self.__index = len(self.__history)

    def undo(self) -> None:
        """
        Undo the last operations carried out
        """
        self.__index -= 1
        self.__history[self.__index].undo()

    def redo(self) -> None:
        """
        Redo the last operation that was undone. Only available after at least one undo
        """
        self.__history[self.__index].redo()
        self.__index += 1


if __name__ == "__main__":
    def fun(*params):  # actually a tuple * - unpacking
        for p in params:
            print(p)


    fc = FunctionCall(fun, 1, 2, 3, 4, 5)
    fc.call()
    # fc()
