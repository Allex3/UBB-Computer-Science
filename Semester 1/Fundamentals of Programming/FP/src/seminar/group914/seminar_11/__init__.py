"""
    About undo/redo using the Command pattern
    https://refactoring.guru/design-patterns/command

    1. Undo/redo only operations that change data (add/remove/update)
    2. We must keep a list/stack of all program operations that we want undone
        -> Each time we have an operations we have to record it for undo
        -> undo is always the opposite operation
        -> redo is the operation itself (redo is only available after at least 1 undo)
    3. If one or more undo operations are followed by a new operation (not undo/redo), redo is no longer
    available
"""
