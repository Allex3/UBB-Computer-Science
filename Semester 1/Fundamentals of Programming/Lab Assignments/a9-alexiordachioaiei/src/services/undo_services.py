from src.commands.command import CommandUndoRedo

class UndoException(Exception):
    pass

class UndoServices:
    def __init__(self):
        # List of "how" to undo/redo all program operations
        # each element is an Operation object, which has defined both undo() and redo()
        # for a given operation (command)
        # For example, we can have remove = Operation(add, remove)
        # basically the undo for remove is add, the redo is remove, we essentially just do it again...
        self.__history = []
        self.__index = -1

    def record(self, operation: CommandUndoRedo):
        # After you go back in the list to undo or redo, and then do a NEW operation
        # The undo/redo of that operation is added to the history list
        # But the index is not at the end, and if we keep it where it is, then the order won't be good anymore
        # Because we did a new operation so now undoing has to start from there
        # But, if we delete the elements of the list after the element undone we cannot redo
        # so ONLY delete them after you record a new operation
        # Because then undo/redo doesn't work as intended, it would undo/redo commands BEFORE the last added one, ignoring it and we cannot undo it

        # So, for bugs' sake, when we carry out a new operation, get the index after it so the list works as intended starting undoing/redoing from there
        # But also first delete the existing operations to the right of index
        # Because they were undone, and if we keep them they could be done again
        # Like we have 1, 2, 3, 4, 5, we get to 3 by undoing 4 and 5
        # then we append a new 6, we should have 1 2 3 6, but we have 1 2 3 6 5 if we don't clear to the right
        # And so we could do redo() and we will now redo 5, which should be illegal, because that action wasn't the current one!
        
        # So like, pop until the length IS the index right, then index will be one after the last element, as it should be
        # We do this because, we got to an element which is undone from the left, we also need to pop it too
        # If we don't we risk undoing an undone already command
        if self.__index > -1:
            while self.__index < len(self.__history):
                self.__history.pop()
        self.__history.append(operation)
        self.__index = len(self.__history)

    def undo(self) -> None:
        """
        Undo the last operations carried out
        :return: None
        """
        # history = add, add, remove, add, - <- index after the last element
        # undo() -> index--, add.undo() = remove
        # history = add, add, remove, add, BUT index is at add now, because we've done an undo
        # if we do more undos the index keeps going to the left and doing the undo of that operation
        # To redo, we redo the operation I'm at because that's the one that was undone, then go to the next one
        # redo() -> add.redo() = add, index++

        if self.__index == 0:
            raise UndoException("There are no more actions to be undone!")

        self.__index -= 1
        self.__history[self.__index].undo()

    def redo(self) -> None:
        """
        Redoes the last undone operation
        :return: None
        """
        if self.__index == len(self.__history):
            raise UndoException("There are no more actions to be redone!")

        self.__history[self.__index].redo()
        self.__index += 1
