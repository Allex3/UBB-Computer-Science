class FunctionCall:
    """
    Objects of this class encode calling a function with given parameters
    e.g., client_repo.delete(105)
    """

    def __init__(self, function_name, *function_params):
        # *function_params packs all parameters into a tuple called <function_params>
        self.__function_name = function_name
        self.__function_params = function_params

    def call(self):
        self.__function_name(*self.__function_params)

    def __call__(self, *args, **kwargs):
        self.call()


class Operation:
    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall):
        self.__undo_function = undo_function
        self.__redo_function = redo_function

    def undo(self):
        self.__undo_function()  # works because __call__ is implemented

    def redo(self):
        self.__redo_function()


class CascadedOperation:
    def __init__(self):
        self.__undo_function = []
        self.__redo_function = []

    def add_undo_function(self, undo_function: FunctionCall):
        self.__undo_function.append(undo_function)

    def add_redo_function(self, redo_function: FunctionCall):
        self.__redo_function.append(redo_function)

    def undo(self):
        for func in self.__undo_function:
            # call each function to undo one entity at a time
            func()

    def redo(self):
        for func in self.__redo_function:
            # call each function to redo one entity at a time
            func()


class UndoRedoError(Exception):
    pass


class UndoService:
    """
    The UI has access to this UndoService and calls undo() or redo() directly
    This service is common across all program entities and functionalities
    """

    def __init__(self):
        self.__undo_stack = []
        self.__redo_stack = []

    def record(self, operation: Operation):
        # NOTE When an operation that is not undo or redo is made, all stored redos are invalidated
        self.__redo_stack.clear()
        self.__undo_stack.append(operation)

    def undo(self):
        if len(self.__undo_stack) == 0:
            raise UndoRedoError("No more undos!")

        current_operation = self.__undo_stack.pop()
        current_operation.undo()
        self.__redo_stack.append(current_operation)

    def redo(self):
        if len(self.__redo_stack) == 0:
            raise UndoRedoError("No more redos!")

        current_operation = self.__redo_stack.pop()
        current_operation.redo()
        self.__undo_stack.append(current_operation)


if __name__ == "__main__":
    def fun(x, y, z, t):
        print(x, y, z, t)


    fc = FunctionCall(fun, 1, 2, "abcd", 99)

    # bunch of code goes here

    fc.call()
    fc()
