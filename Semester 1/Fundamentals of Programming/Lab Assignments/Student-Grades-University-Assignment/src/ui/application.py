from datetime import datetime

from src.services.repo_error import RepositoryError
from src.services.student_services import StudentServices
from src.services.grade_services import GradeServices
from src.services.assignment_services import AssignmentServices
from src.services.undo_services import UndoServices
from src.commands.command import Command, CommandUndoRedo, Assign, AddAssignmentWithGrades, AddStudentWithGrades


class Application(object):
    def __init__(self, student_services: StudentServices, assignment_services: AssignmentServices,
                 grade_services: GradeServices, undo_services: UndoServices):

        self.__student_services = student_services
        self.__assignment_services = assignment_services
        self.__grade_services = grade_services
        self.__history = undo_services

        self.__MANAGE = "1"
        self.__GIVE = "2"
        self.__GRADE = "3"
        self.__STATISTICS = "4"
        self.__UNDO = "5"
        self.__REDO = "6"

        self.__MANAGE_STUDENTS = "1"
        self.__MANAGE_ASSIGNMENTS = "2"

        self.__ADD = "1"
        self.__REMOVE = "2"

        self.__UPDATE = "3"

        self.__UPDATE_NAME = "1"
        self.__UPDATE_GROUP = "2"

        self.__UPDATE_DESCRIPTION = "1"
        self.__UPDATE_DEADLINE = "2"

        self.__LIST = "4"

        self.__GIVE_STUDENT = "1"
        self.__GIVE_GROUP = "2"

        self.__GRADE_DESCENDING = "1"
        self.__LATE_STUDENTS = "2"
        self.__BEST_STUDENTS = "3"

        self.__EXIT = "0"

        self.__OPTIONS = {"MANAGE": "1 - Manage students and assignments.",
                          "GIVE": "2 - Give assignments to a student or a group of students.",
                          "GRADE": "3 - Grade student for a given assignment.",
                          "STATISTICS": "4 - Get some statistics regarding the student's grades.",
                          "UNDO": "5 - Undo the last action",
                          "REDO": "6 - Redo the action you just undone.",

                          "MANAGE_STUDENTS": "1 - Manage students",
                          "MANAGE_ASSIGNMENTS": "2 - Manage assignments",

                          "ADD_STUDENT": "1 - Add a new student",
                          "REMOVE_STUDENT": "2 - Remove student given by their ID",
                          "UPDATE_STUDENT": "3 - Update a student given by their ID",
                          "UPDATE_NAME": "1 - Change this student's name",
                          "UPDATE_GROUP": "2 - Change this student's group",

                          "LIST_STUDENTS": "4 - List all the students.",

                          "ADD_ASSIGNMENT": "1 - Add a new assignment",
                          "REMOVE_ASSIGNMENT": "2 - Remove assignment given by its ID",
                          "UPDATE_ASSIGNMENT": "3 - Update an assignment given by its ID",
                          "UPDATE_DESCRIPTION": "1 - Give a new description to this assignment",
                          "UPDATE_DEADLINE": "2 - Update the deadline for this assignment",
                          "LIST_ASSIGNMENTS": "4 - List all the assignments.",

                          "GIVE_STUDENT": "1 - Give a new assignment (by ID) to a student given by their ID.",
                          "GIVE_GROUP": "2 - Give a new assignment (given by ID) to a specific group of students.",

                          "GRADE_DESCENDING": "1 - All students who received a given assignment, ordered descending by grade.",
                          "LATE_STUDENTS": "2 -All students who are late in handing in at least one assignment. These are all the students who have an ungraded assignment for which the deadline has passed.",
                          "BEST_STUDENTS": "3- Students with the best school situation, sorted in descending order of the average grade received for all graded assignments.",

                          "EXIT": "0 - Exit the program."}

        self.__ERRORS = {"INT": "The ID/group/grade/day/month/year/hour/minute should be a positive integer. Try again",
                         "INVALID_INPUT": "Your input is not valid. Try again",
                         "DATE": "The date format is invalid. 1<=month<=12, 1<=day<=no. of days in month, 0<=hour<=24, 0<=minute<60. Try again"}

    def open_menu(self):
        print("This application manages students and their assignments. Choose an option from the menu below.")
        self.__menu()

    def __get_student_id(self) -> int:
        try:
            student_id = int(input("Student id: "))
            return student_id
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_student_id()

    def __get_student_name(self) -> str:
        return input("Student name: ")

    def __get_student_group(self) -> int:
        try:
            student_group = int(input("Student group: "))
            return student_group
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_student_group()

    def __get_assignment_id(self) -> int:
        try:
            assignment_id = int(input("Assignment id: "))
            return assignment_id
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_assignment_id()

    def __get_assignment_description(self) -> str:
        return input("Assignment description: ")

    def __get_assignment_deadline(self) -> datetime:
        print("Input the assignment's deadline.")
        try:
            year = int(input("Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))
            hour = int(input("Hour: "))
            minute = int(input("Minute: "))

        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_assignment_deadline()

        try:
            deadline = datetime(year, month, day, hour, minute)
            return deadline
        except ValueError:
            print(self.__ERRORS["DATE"])
            return self.__get_assignment_deadline()

    def __manage(self):
        print(self.__OPTIONS["MANAGE_STUDENTS"])
        print(self.__OPTIONS["MANAGE_ASSIGNMENTS"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__MANAGE_STUDENTS:
                self.__manage_students()
            case self.__MANAGE_ASSIGNMENTS:
                self.__manage_assignments()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__manage()

    def __manage_students(self):
        print(self.__OPTIONS["ADD_STUDENT"])
        print(self.__OPTIONS["REMOVE_STUDENT"])
        print(self.__OPTIONS["UPDATE_STUDENT"])
        print(self.__OPTIONS["LIST_STUDENTS"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__ADD:
                self.__add_new_student()
            case self.__REMOVE:
                self.__remove_student()
            case self.__UPDATE:
                self.__update_student()
            case self.__LIST:
                self.__list_students()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__manage_students()

    def __manage_assignments(self):
        print(self.__OPTIONS["ADD_ASSIGNMENT"])
        print(self.__OPTIONS["REMOVE_ASSIGNMENT"])
        print(self.__OPTIONS["UPDATE_ASSIGNMENT"])
        print(self.__OPTIONS["LIST_ASSIGNMENTS"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__ADD:
                self.__add_new_assignment()
            case self.__REMOVE:
                self.__remove_assignment()
            case self.__UPDATE:
                self.__update_assignment()
            case self.__LIST:
                self.__list_assignments()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__manage_assignments()

    def __add_new_student(self):
        student_id = self.__get_student_id()
        name = self.__get_student_name()
        group = self.__get_student_group()
        command = Command(self.__student_services.add, student_id, name, group)
        undo_command = Command(self.__student_services.remove, student_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __remove_student(self):
        student_id = self.__get_student_id()
        try:
            name = self.__student_services.get_name(student_id)
            group = self.__student_services.get_group(student_id)
        except Exception as e:
            print(e)
            return
        command = Command(self.__student_services.remove, student_id)
        student_grades = self.__grade_services.get_student_grades(student_id)
        undo_command = AddStudentWithGrades(student_grades, self.__grade_services.add, self.__student_services.add,
                                            student_id, name, group)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_student_name(self):
        student_id = self.__get_student_id()
        new_name = self.__get_student_name()
        try:
            old_name = self.__student_services.get_name(student_id)
        except Exception as e:
            print(e)
            return
        command = Command(self.__student_services.update_name, student_id, new_name)
        undo_command = Command(self.__student_services.update_name, student_id, old_name)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_student_group(self):
        student_id = self.__get_student_id()
        new_group = self.__get_student_group()
        try:
            old_group = self.__student_services.get_group(student_id)
        except Exception as e:
            print(e)
            return
        command = Command(self.__student_services.update_group, student_id, new_group)
        undo_command = Command(self.__student_services.update_group, student_id, old_group)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_student(self):
        print(self.__OPTIONS["UPDATE_NAME"])
        print(self.__OPTIONS["UPDATE_GROUP"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__UPDATE_NAME:
                self.__update_student_name()
            case self.__UPDATE_GROUP:
                self.__update_student_group()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__update_student()

    def __list_students(self):
        for student in self.__student_services.get_students():
            print(student)
        print()

    def __add_new_assignment(self):
        assignment_id = self.__get_assignment_id()
        description = self.__get_assignment_description()
        deadline = self.__get_assignment_deadline()
        command = Command(self.__assignment_services.add, assignment_id, description, deadline)
        undo_command = Command(self.__assignment_services.remove, assignment_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __remove_assignment(self):
        assignment_id = self.__get_assignment_id()
        try:
            description = self.__assignment_services.get_description(assignment_id)
            deadline = self.__assignment_services.get_deadline(assignment_id)
        except Exception as e:
            print(e)
            return
        command = Command(self.__assignment_services.remove, assignment_id)
        assignment_grades = self.__grade_services.get_assignment_grades(assignment_id)
        undo_command = AddAssignmentWithGrades(assignment_grades, self.__grade_services.add,
                                               self.__assignment_services.add, assignment_id, description, deadline)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_assignment_description(self):
        assignment_id = self.__get_assignment_id()
        new_description = self.__get_assignment_description()
        try:
            old_description = self.__assignment_services.get_description(assignment_id)
        except Exception as e:
            print(e)
            return
        command = Command(self.__assignment_services.update_description, assignment_id, new_description)
        undo_command = Command(self.__assignment_services.update_description, assignment_id, old_description)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_assignment_deadline(self):
        assignment_id = self.__get_assignment_id()
        new_deadline = self.__get_assignment_deadline()
        try:
            old_deadline = self.__assignment_services.get_deadline(assignment_id)
        except Exception as e:
            print(e)
            return
        command = Command(self.__assignment_services.update_deadline, assignment_id, new_deadline)
        undo_command = Command(self.__assignment_services.update_deadline, assignment_id, old_deadline)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_assignment(self):
        print(self.__OPTIONS["UPDATE_DESCRIPTION"])
        print(self.__OPTIONS["UPDATE_DEADLINE"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__UPDATE_DESCRIPTION:
                self.__update_assignment_description()
            case self.__UPDATE_DEADLINE:
                self.__update_assignment_deadline()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__update_assignment()

    def __list_assignments(self):
        for assignment in self.__assignment_services.get_assignments():
            print(assignment)
        print()

    def __give_student(self):
        student_id = self.__get_student_id()
        assignment_id = self.__get_assignment_id()
        command = Command(self.__grade_services.assign, student_id, assignment_id)
        undo_command = Command(self.__grade_services.remove, student_id, assignment_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __give_group(self):
        group = self.__get_student_group()
        assignment_id = self.__get_assignment_id()  # Assignment to be assigned to the group
        command = Assign(self.__grade_services.assign_group, group, assignment_id)
        undo_command = Command(self.__grade_services.remove_group_assignment, group, assignment_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __give(self):
        print(self.__OPTIONS["GIVE_STUDENT"])
        print(self.__OPTIONS["GIVE_GROUP"])
        print(self.__OPTIONS["EXIT"])
        option = input(">")
        match option:
            case self.__GIVE_STUDENT:
                self.__give_student()
            case self.__GIVE_GROUP:
                self.__give_group()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__give()

    def __get_grade(self):
        try:
            grade = int(input("Grade: "))
            return grade
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_grade()

    def __grade(self):
        student_id = self.__get_student_id()
        print("List of the assignments for this student:")
        for assignment in self.__grade_services.get_student_grades(student_id):
            print(assignment)

        print("Select from this list an assignment which is ungraded to grade.")

        assignment_id = self.__get_assignment_id()
        grade = self.__get_grade()

        try:
            old_grade = self.__grade_services.get_grade(student_id, assignment_id)
            command = Command(self.__grade_services.grade_assignment, student_id, assignment_id, grade)
            undo_command = Command(self.__grade_services.grade_assignment, student_id, assignment_id, old_grade)
            full_command = CommandUndoRedo(command, undo_command)  # A command equipped with undo and redo!
            self.__execute_command(full_command)  # execute the doing part of the command
        except Exception as e:
            print(e)

    def __menu(self):
        while (True):
            print(self.__OPTIONS["MANAGE"])
            print(self.__OPTIONS["GIVE"])
            print(self.__OPTIONS["GRADE"])
            print(self.__OPTIONS["STATISTICS"])
            print(self.__OPTIONS["UNDO"])
            print(self.__OPTIONS["REDO"])
            print(self.__OPTIONS["EXIT"])
            option = input("> ")
            match option:
                case self.__MANAGE:
                    self.__manage()
                case self.__GIVE:
                    self.__give()
                case self.__GRADE:
                    self.__grade()
                case self.__STATISTICS:
                    self.__statistics()
                case self.__UNDO:
                    self.__undo()
                case self.__REDO:
                    self.__redo()
                case self.__EXIT:
                    exit(0)
                case _:
                    print(self.__ERRORS["INVALID_INPUT"])

    def __execute_command(self, command: CommandUndoRedo):
        try:
            command.redo()  # basically the base command, that's what we do, then store the whole operation also containing the undo
            self.__history.record(command)
            print("Successfully executed.")
        except Exception as e:
            print(e)

    def __undo(self):
        try:
            self.__history.undo()
            print("Successfully executed.")
        except Exception as e:
            print(e)


    def __redo(self):
        try:
            self.__history.redo()
            print("Successfully executed.")
        except Exception as e:
            print(e)

    def __statistics(self):
        print(self.__OPTIONS["GRADE_DESCENDING"])
        print(self.__OPTIONS["LATE_STUDENTS"])
        print(self.__OPTIONS["BEST_STUDENTS"])
        print(self.__OPTIONS["EXIT"])
        option = input(">")
        match option:
            case self.__GRADE_DESCENDING:
                self.__grade_descending()
            case self.__LATE_STUDENTS:
                self.__late_students()
            case self.__BEST_STUDENTS:
                self.__best_students()
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INPUT"])
                self.__statistics()

    def __grade_descending(self):
        assignment_id = self.__get_assignment_id()
        print(f"The students with the highest grades at assignment {assignment_id}")
        for grade in self.__grade_services.grade_descending(assignment_id):
            print(self.__student_services.get_student(grade.student_id),
                  "; grade =", grade.grade_value)
        print()
    def __late_students(self):
        late_students = self.__grade_services.get_late_student_grades()
        students = []
        assignments = []
        for student_ungraded_grades in late_students:  # student_ungraded_grades is a list of their ungraded grades that are past due!
            # Just get the first grade to get the student first
            print(
                f"{self.__student_services.get_student(student_ungraded_grades[0].student_id)}, who is late for the following assignments: ",
                end="")
            for grade in student_ungraded_grades:
                print(str(grade.assignment_id) + " ", end="")
            print()
        print()

    def __best_students(self):
        best_students_grades = self.__grade_services.get_best_students_grades()
        for student_id in best_students_grades:
            print(f"{self.__student_services.get_student(student_id)}, average grade = {best_students_grades[student_id]}")
        print()
