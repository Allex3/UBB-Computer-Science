"""
 The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
 communicate via function parameters, the return statement and raising of exceptions.
"""
import copy
from random import randint
from texttable import Texttable

"""
Modular programming
functions.py - NonUI functions (computation/logic)
             - atleast one function for EACH functionality (command)
             - for C, display elems with a property = search+Display
                the search part is in functions.py, but does NOT display it too
                displaying happens in the UI, where the result is returned
start.py - put everything together here (main module) (call main from UI)
ui.py - functions with UI (reading/displaying/running the loop displaying the commands)
        - for the DISPLAY part (command C) use TEXTTABLE
start imports UI, UI imports functions.py

Test & Specifications - for functions in functions.py for A and B !
    def test_add(): #testing if one function works correctly
        - use add inside the test and check if the result is what you'd expect
        - e.g. add should add an element at the end of the list, so you
            l = []
            add(l, el)
            assert (l==[el])

            l=[e1, e2]
            add(l, e3)
            assert (l==[e1, e2, e3])
        These are some example of tests that check multiple edge cases

Function specification! (doc string)
 - for all functions in functions.py (nonUI functions)

Use lists or dictionaries (choose 1)
    -same as A5, create, getters and setters, and (maybe) to_string
"""


# Getters, setters and create

def create_participant(scores: list[int], cid: int) -> dict:
    return {"cid": cid, "P1": scores[0], "P2": scores[1], "P3": scores[2], "average": (scores[0]+scores[1]+scores[2])//3}

def get_P1(participant: dict) -> int:
    return participant["P1"]

def get_P2(participant: dict) -> int:
    return participant["P2"]

def get_P3(participant: dict) -> int:
    return participant["P3"]

def get_cid(participant: dict) -> int:
    return participant["cid"]

def get_average(participant: dict) -> int:
    return participant["average"]

def set_P1(participant: dict, p1: int) -> None:
    participant["P1"] = p1

def set_P2(participant: dict, p2: int) -> None:
    participant["P2"] = p2

def set_P3(participant: dict, p3: int) -> None:
    participant["P3"] = p3

def set_average(participant: dict) -> None:
    participant["average"] = (get_P1(participant) + get_P2(participant) + get_P3(participant))//3

# List to texttable

def list_to_texttable(contestants: list) -> Texttable:
    """
    Returns a Texttable corresponding to the list of contestants
    :param contestants: List of contestants
    :return: The texttable corresponding to the contestants
    """
    table = Texttable()
    table.add_row(["Contestant", "P1", "P2", "P3", "Average"])
    for i in range(0, len(contestants)):
        contestant = contestants[i]
        table.add_row([get_cid(contestant), get_P1(contestant), get_P2(contestant), get_P3(contestant), get_average(contestant)])

    return table


# Parsing and running the commands here

def parse_command(command: str, commands: list[str]) -> list:
    """
    Parses the command and returns the list of logical instructions that it's made of, that list of instructions will be used in the implementation of the commands
    :param command: The command the user inputs in string format
    :param commands: The list of all the possible main commands to check
    :return: A list of instructions that the command is made of
    """
    parsed = command.split(" ")
    # parsed[0] would be the main command
    if parsed[0] not in commands:
        return [-1]

    incorrect = [0]
    main_command = parsed[0]
    instructions = []
    match main_command:
        case "add":  # if add is correct, it has 3 integers after it
            if len(parsed) != 4:  # more or less than the maximum arguments for command
                return incorrect
            instructions.append(1)
            for i in range(1, 4):
                instructions.append(int(parsed[i]))
        case "insert":
            if len(parsed) != 6:
                return incorrect
            instructions.append(2)
            for i in range(1, 4):
                instructions.append(int(parsed[i]))
                if (not (0 <= instructions[i] <= 10)):
                    return incorrect  # good command but bad numbers
            # <position> is at parsed[5]
            instructions.append(int(parsed[5]))
        case "remove":
            if len(parsed) != 2 and len(parsed) != 4 and len(parsed) != 3:
                return incorrect

            instructions.append(3)
            if len(parsed) == 2:
                instructions.append(int(parsed[1]))
            if len(parsed) == 3:
                if not (parsed[1] == "<" or parsed[1] == "=" or parsed[1] == ">"):
                    return incorrect
                instructions.append(parsed[1])
                instructions.append(int(parsed[2]))
            if len(parsed) == 4:  # it's of type remove start to end
                instructions.append(int(parsed[1]))
                if (parsed[2] != "to"):
                    return incorrect
                instructions.append(int(parsed[3]))  # parsed[2] = "to", the end position is at parsed[3]

                if (parsed[1]>parsed[3]):
                    return incorrect
        case "replace":
            if len(parsed) != 5:
                return incorrect

            instructions.append(4)
            instructions.append(int(parsed[1]))
            if not (parsed[2] == "p1" or parsed[2] == "p2" or parsed[2] == "p3"):
                return incorrect

            instructions.append(parsed[2])
            if parsed[3] != "with":
                return incorrect

            instructions.append(int(parsed[4]))

        case "list":
            if len(parsed) != 1 and len(parsed)!=2 and len(parsed)!=3:
                return incorrect

            instructions.append(5)
            if len(parsed) == 2:
                if parsed[1] != "sorted":
                    return incorrect
                instructions.append(parsed[1])
            if len(parsed) == 3:
                if not (parsed[1] == "<" or parsed[1] == "=" or parsed[1] == ">"):
                    return incorrect

                instructions.append(parsed[1])
                instructions.append(int(parsed[2]))

        case "top":
            if len(parsed) !=2 and len(parsed)!=3:
                return incorrect

            instructions.append(6)
            if len(parsed) == 2:
                instructions.append(int(parsed[1]))

            if len(parsed) == 3:
                instructions.append(int(parsed[1]))
                if not (parsed[2] == "p1" or parsed[2] == "p2" or parsed[2] == "p3"):
                    return incorrect
                instructions.append(parsed[2])

        case "undo":
            if len(parsed) != 1:
                return incorrect
            instructions.append(7)

    return instructions


def run_command(instructions: list, contestants: list[dict], last_contestants: list) -> Texttable | bool | str|list:
    """
    Executes the command the user inputted
    :param instructions: Instructions of the command needed for it to run
    :param contestants: The list of contestants
    :param last_contestants: The lists of previous contestants, for the undo command
    :return: A Texttable that satisfied the condition (C, D) or a boolean signifying if there is an index error when accessing the list, False if error, True if command works fine, also a string for some cases of some commands, but a list if the command is of type "undo", that is the last unmodified list of contestants.
    """

    match instructions[0]:  # what main command it is, being a correct type of command
        case 1:
            if add(instructions[1:], contestants) is False:
                return "Scores should be between 0 and 10."
        case 2:
            try:
                insert(instructions[1:], contestants)
            except IndexError:
                return False
        case 3:
            try:
                remove(instructions[1:], contestants)
            except IndexError:
                return False
        case 4:
            try:
                replace(instructions[1:], contestants)
            except IndexError:
                return False
        case 5:
            return get_list(instructions[1:], contestants)  # get a list of some conditions and return it so it can be displayed
        case 6:
            return get_top(instructions[1:], contestants)
        case 7:
            try:
                return undo(last_contestants)
            except IndexError:
                return "Reached the unmodified list"

    return True


# The actual algorithms that run for a command

def add(scores: list, contestants: list) -> bool:
    """
    Adds a new participant to the list of participants, whose scores are given
    :param scores: List of the three scores that will compose a new participant in the list of participants
    :param contestants: The list of participants to add to
    :return: True if successfully added, False otherwise
    """
    # if we got here, the command should be valid and the participant added

    for i in range(0, 3):
        if not(0<=scores[i]<=10):
            return False

    new_participant = create_participant(scores, len(contestants))
    contestants.append(new_participant)

    return True

def insert(instructions: list, contestants: list) -> None:
    """
    Insert a new participant with a set of scores at a given position in the list of participants
    :param instructions: The list of scores and the position where to insert them
    :param contestants: The list of participants to insert to
    :return: None
    """
    # instructions[3] has the index to insert at

    new_contestant = create_participant(instructions[0:3], instructions[3])  # the scores are at positions 0, 1, 2
    contestants[instructions[3]] = new_contestant

def remove_impl(contestants: list, left:int, right: int) -> None:
    """
    Set to 0 the scores of a set of consecutive participants from the list
    Is used in the implementation of the "remove" command
    :param contestants: List of contestants
    :param left: The left position of the subarray to be removed
    :param right: The right position of the subarray to be removed
    :return: Nothing, the list is modified
    """

    for i in range(left, right+1):
        # remove it by moving all the participants from pos + 1 to the end of the list
        # to the left one position, thus clearing the position
        set_P1(contestants[i], 0)
        set_P2(contestants[i], 0)
        set_P3(contestants[i], 0)
        set_average(contestants[i])

def remove(instructions: list, contestants: list[dict]) -> None:
    """
    Set to 0 the score of one or multiple participants with the given condition, or from given indexes.
    :param instructions: Instructions that give what to remove from the list of participants
    :param contestants: The list of contestants
    :return: None
    """
    if type(instructions[0]) is int:  # we have remove <position> or remove <pos1> to <pos2>
        if len(instructions)==1:
            remove_impl(contestants, instructions[0], instructions[0])

        if len(instructions)==2:
           remove_impl(contestants, instructions[0], instructions[1])

    if type(instructions[0]) is str: # <, =, >
        comp = instructions[1] #number to be compared to
        for i in range(0, len(contestants)):
            match instructions[0]:
                case "<":
                    if get_average(contestants[i]) < comp:
                        remove_impl(contestants, i, i)
                case "=":
                    if get_average(contestants[i]) == comp:
                        remove_impl(contestants, i, i)
                case ">":
                    if get_average(contestants[i]) > comp:
                        remove_impl(contestants, i, i)

def replace(instructions: list, contestants: list[dict]) -> None:
    """
    Replace a score obtained at a specific problem by a participant with another score
    :param instructions: The instructions given to replace a participant: their index, the problem, and the score to replace it with
    :param contestants: The list of contestants
    :return: None
    """

    #instructions[0]: P1 | P2 | P3, instructions[1] = index of contestant, instructions[2], score
    match instructions[1]:
        case "p1":
            set_P1(contestants[instructions[0]], instructions[2])
        case "p2":
            set_P2(contestants[instructions[0]], instructions[2])
        case "p3":
            set_P3(contestants[instructions[0]], instructions[2])

    set_average(contestants[instructions[0]])

def partition(contestants: list[dict], left: int, right: int, sort_by: str):
    """
    Sort a partition from the quick sort algorithm by P1 | P2 | P3 | average of scores of a contestant
    :param contestants: List of contestants
    :param left: start index of partition
    :param right: end index of partition
    :param sort_by: P1 | P2 | P3 | average, what to sort by
    :return: The index for which all the elements to its left in the present partition are smaller than it, depending on what we sort by
    """
    # choose the pivot to be the rightmost contestant
    pivot_value = 0
    match sort_by:
        case "average":
            pivot_value = get_average(contestants[right])
        case "p1":
            pivot_value = get_P1(contestants[right])
        case "p2":
            pivot_value = get_P2(contestants[right])
        case "p3":
            pivot_value = get_P3(contestants[right])

    # Index of smaller element and indicates
    # the right position of pivot found so far
    i = left - 1

    # Traverse contestants[left,..., right] and move all smaller elements to the left side of itself
    for j in range(left, right):
        current_value = 0
        match sort_by:
            case "average":
                current_value = get_average(contestants[j])
            case "p1":
                current_value = get_P1(contestants[j])
            case "p2":
                current_value = get_P2(contestants[j])
            case "p3":
                current_value = get_P3(contestants[j])
        if current_value < pivot_value:
            i += 1
            contestants[i], contestants[j] = contestants[j], contestants[i]

    # move the pivot to the rightmost not switched index, so that
    #all that is to its left is smaller than it, so from left to i, smaller than the pivot i+1
    contestants[i+1], contestants[right] = contestants[right], contestants[i+1]
    return i + 1

def quick_sort(contestants: list[dict], left: int, right: int, sort_by: str) -> None:
    """
    Quick sort algorithm by P1 | P2 | P3 | average
    :param contestants: List of contestants to sort
    :param left: Start index of the sublist for which we will compute the partition
    :param right: End index of the sublist for which we will compute the partition
    :param sort_by: P1 | P2 | P3 | average, what part of the contestant scores to sort by
    :return: Nothing, sorts the list
    """
    if left < right:
        # the pivot is returned by the partition
        pivot = partition(contestants, left, right, sort_by)

        # go to the left and right of the index of the pivot in the contestants list
        # the elements from the left of the now pivot are all smaller than it
        quick_sort(contestants, left, pivot - 1, sort_by)
        quick_sort(contestants, pivot + 1, right, sort_by)

def get_list(instructions: list, contestants: list) -> Texttable:
    """
    Returns a list with the specified conditions
    :param instructions: List of instructions to know what type of listing you want
    :param contestants: List of contestants
    :return: A Texttable object of contestants adhering to the conditions (sorted, or < | = | > to an average)
    """

    if not instructions: #no conditions
        return list_to_texttable(contestants)

    filtered_list = []
    match instructions[0]:
        case "<":
            for i in range(0, len(contestants)):
                if get_average(contestants[i]) < instructions[1]:
                    filtered_list.append(contestants[i])
        case "=":
            for i in range(0, len(contestants)):
                if get_average(contestants[i]) == instructions[1]:
                    filtered_list.append(contestants[i])
        case ">":
            for i in range(0, len(contestants)):
                if get_average(contestants[i]) > instructions[1]:
                    filtered_list.append(contestants[i])
        case "sorted":
            filtered_list = contestants[:]
            sort_by = "average"
            quick_sort(filtered_list, 0, len(filtered_list)-1, sort_by)
            filtered_list.reverse()

    return list_to_texttable(filtered_list)

def get_top(instructions: list, contestants: list) -> Texttable:
    """
    Returns the set of participants with the highest average, or specific (p1, p2, p3) score
    :param instructions: The instructions to compute the top
    :param contestants: List of contestants
    :return: List of the top of participants
    """

    filtered_list = contestants[:]
    top_list = []
    if len(instructions)==1:
        sort_by = "average"
        quick_sort(filtered_list, 0, len(filtered_list)-1, sort_by)
        filtered_list.reverse()
        for i in range(0, instructions[0]):
            top_list.append(filtered_list[i])

    if len(instructions)==2:
        sort_by = instructions[1]
        quick_sort(filtered_list, 0, len(filtered_list)-1, sort_by)
        filtered_list.reverse()
        for i in range(0, instructions[0]):
            top_list.append(filtered_list[i])

    return list_to_texttable(top_list)

def undo(last_contestants: list[list]) -> list:
    """
    Undo the last command
    :param last_contestants: List of contestants after previous command
    :return: Last list of participants
    """
    return last_contestants.pop()


# Generate funhction
def generate_random_contestants(n: int) -> list[dict]:
    """
    Returns a list of n participants with random scores.
    :param n: The number of participants to generate a list of
    :return: The list of random participants
    """
    participants = list()
    for i in range(n):
        P1 = randint(1, 10)
        P2 = randint(1, 10)
        P3 = randint(1, 10)
        participant = create_participant([P1, P2, P3], i)
        participants.append(participant)

    return participants
