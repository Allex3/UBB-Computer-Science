class FunctionCall:
    def __init__(self, functionName, *functionParamteres):
        self.__functionName = functionName
        self.__functionParameters = functionParamteres

    def call(self):
        self.__functionName(*self.__functionParameters)

    def __call__(self, *args, **kwargs):
        return self.call()

class Operation:
    def __init__(self, functionUndo, functionRedo):
        self.__functionUndo = functionUndo
        self.__functionRedo = functionRedo

    def undo(self):
        self.__functionUndo()

    def redo(self):
        self.__functionRedo()

class CascadedOperation:
    def __init__(self, *operations):
        self.__operations = operations

    def undo(self):
        for oper in self.__operations:
            oper.undo()

    def redo(self):
        for oper in self.__operations:
            oper.redo()

class UndoError(Exception):
    pass

class UndoService:
    def __init__(self):
        self.__history = []
        self.__index = -1

    def recordUndo(self, operation: Operation):
        self.__history.append(operation)
        self.__index = len(self.__history) - 1

    def undo(self):
        if self.__index == -1:
            raise UndoError("No more undos")

        self.__history[self.__index].undo()
        self.__index -= 1

    def redo(self):
        if self.__index == len(self.__history) - 1:
            raise UndoError("No more redos")

        self.__index += 1
        self.__history[self.__index].redo()

