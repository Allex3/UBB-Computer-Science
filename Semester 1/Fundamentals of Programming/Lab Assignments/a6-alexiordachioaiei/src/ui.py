#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
import copy

# Command based console app: "insert <number> at <position>"
# Instead of "insert" then "number" then "position" like in an menu
# In which you insert one part of the command at a time


# Command categories
#     A - add (add d, insert, etc.)
#     B - remove (element, or by type, etc.)
#     C - Displaying elements (all or with one property)
#     D - filtering (remove all elements that do not respect x condition)
#         e.g. filter integers = remove all non-integers from the list so only integers remain
#     E - undo (ofc, don't "undo" display commands)
#         Also, allowed to undo an infinitely number of times
#         Until you reach the start of the app

# User input validation
#   Whatever the user inputs, the program does NOT CRASH (try/except)
# Write relevant error messages

from texttable import Texttable
from src.functions import *

def print_documentation(command):
    match command:
        case "add":
            print("Usage: add <P1 score> <P2 score> <P3 score>")
        case "insert":
            print("Usage: insert <P1 score> <P2 score> <P3 score> at <position>")
            print("""add 3 8 10 – add a new participant with scores 3,8 and 10 (scores for P1, P2, P3 respectively)
            insert 10 10 9 at 5 – insert scores 10, 10 and 9 at position 5 in the list (positions numbered from 0)""")
        case "remove":
            print("Usage: remove <position>; remove <start position> to <end position>; remove [ < | = | > ] <score>")
            print("""remove 1 – set the scores of the participant at position 1 to 0
remove 1 to 3 – set the scores of participants at positions 1, 2 and 3 to 0
remove < 70 – set the scores of participants having an average score <70 to 0
remove > 89 – set the scores of participants having an average score >89 to 0""")
        case "replace":
            print("Usage: replace <old score> <P1 | P2 | P3> with <new score>")
            print("replace 4 P2 with 5 – replace the score obtained by participant 4 at P2 with 5")
        case "list":
            print("Usage: list; list sorted; list [ < | = | > ] <score>")
            print("""list – display participants and all their scores
list < 4 – display participants with an average score <4
list = 6 – display participants with an average score =6
list sorted – display participants sorted in decreasing order of average score""")
        case "top":
            print("Usage: top <number>; top <number> <P1 | P2 | P3>")
            print("""top 3 – display the 3 participants having the highest average score, in descending order of average score
top 4 P3 – display the 4 participants who obtained the highest score for P3, sorted descending by that score""")
        case "undo":
            print("Usage: undo - – the last operation that modified program data is reversed. The user can undo all operations performed since program start by repeatedly calling this function.")

    print()

def print_bad_command(command):
    print("Your command is invalid")
    if command=="error":
        print("Type 'help' to get the list of all commands.")
        return
    print_documentation(command)


def main():
    print("This app manages contest scores. Write your command")
    print("Write 'exit' to close the app.")

    commands = ["add", "insert", "remove", "replace", "list", "top", "undo"]
    contestants = generate_random_contestants(10)
    last_contestants = [ ] #previous lists of contestants, for the undo command
    while (True):
        command = input("> ")
        command = command.strip().lower()
        if command == "exit":
            return
        if command == "help":
            print_documentation("add")
            print_documentation("insert")
            print_documentation("remove")
            print_documentation("replace")
            print_documentation("list")
            print_documentation("top")
            print_documentation("undo")
            continue

        try:
            instructions = parse_command(command, commands)
        except ValueError or TypeError: # any error in parsing
            if command.split(" ")[0] in commands:
                print_bad_command(command.split(" ")[0])
                continue
            print_bad_command("error")
            continue

        if instructions==[-1]:
            print_bad_command("error")
            continue

        if instructions==[0]:
            #good command but used incorrectly
            print_bad_command(command.split(" ")[0])
            continue

        if command.split(" ")[0] in ["add", "remove", "replace", "insert"]: #command A or B, list modified
            last_contestants.append(copy.deepcopy(contestants))

        result = run_command(instructions, contestants, last_contestants) #command good, run it
        if result == "Scores should be between 0 and 10.":
            print(result)
            continue
        if result == "Reached the unmodified list":
            print(result)
            continue
        if type(result) is list:
            contestants = result
            print("List undone")
            continue
        if result is True:
            continue #ran a command that didn't display anything
        if result is False:
            # Of course, the command could be an index error, in that case, pop the last_contestants, because they weren't modified
            last_contestants.pop()
            print("Index is not in the list.")
            continue

        #if it ran good now it displays something
        if not result:
            print("The returned list is empty.")
            continue

        print(result.draw())