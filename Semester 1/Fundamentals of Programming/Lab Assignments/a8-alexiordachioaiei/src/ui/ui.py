from datetime import datetime
from typing import Any

from src.services.student_services import StudentServices
from src.services.grade_services import GradeServices
from src.services.assignment_services import AssignmentServices
from src.services.repo_error import RepositoryError

class UI(object):
    def __init__(self, student_services: StudentServices, assignment_services: AssignmentServices, grade_services: GradeServices):
        self.__student_services = student_services
        self.__assignment_services = assignment_services
        self.__grade_services = grade_services

        self.__MANAGE = "1"
        self.__GIVE = "2"
        self.__GRADE = "3"

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

        self.__EXIT = "0"

        self.__OPTIONS = {"MANAGE": "1 - Manage students and assignments.",
                          "GIVE": "2 - Give assignments to a student or a group of students.",
                          "GRADE": "3. Grade student for a given assignment.",

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
            # TODO ADD EXIT OPTION FMFMFMFMFMFMM
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
        student_name = self.__get_student_name()
        student_group = self.__get_student_group()
        try:
            self.__student_services.add(student_id, student_name, student_group)
        except Exception as e:
            print(e)

    def __remove_student(self):
        student_id = self.__get_student_id()
        try:
            self.__student_services.remove(student_id)
        except Exception as e:
            print(e)

    def __update_student(self):
        student_id = self.__get_student_id()
        print(self.__OPTIONS["UPDATE_NAME"])
        print(self.__OPTIONS["UPDATE_GROUP"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__UPDATE_NAME:
                new_name = self.__get_student_name()
                try:
                    self.__student_services.update_name(student_id, new_name)
                except Exception as e:
                    print(e)
            case self.__UPDATE_GROUP:
                new_group = self.__get_student_group()
                try:
                    self.__student_services.update_group(student_id, new_group)
                except Exception as e:
                    print(e)
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__update_student()

    def __list_students(self):
        for student in self.__student_services.get_students():
            print(student)

    def __add_new_assignment(self):
        assignment_id = self.__get_assignment_id()
        assignment_description = self.__get_assignment_description()
        assignment_deadline = self.__get_assignment_deadline()
        try:
            self.__assignment_services.add(assignment_id, assignment_description, assignment_deadline)
        except Exception as e:
            print(e)

    def __remove_assignment(self):
        student_id = self.__get_assignment_id()
        try:
            self.__assignment_services.remove(student_id)
        except Exception as e:
            print(e)

    def __update_assignment(self):
        assignment_id = self.__get_assignment_id()
        print(self.__OPTIONS["UPDATE_DESCRIPTION"])
        print(self.__OPTIONS["UPDATE_DEADLINE"])
        print(self.__OPTIONS["EXIT"])
        option = input("> ")
        match option:
            case self.__UPDATE_DESCRIPTION:
                new_description = self.__get_assignment_description()
                try:
                    self.__assignment_services.update_description(assignment_id, new_description)
                except Exception as e:
                    print(e)
            case self.__UPDATE_DEADLINE:
                new_deadline = self.__get_assignment_deadline()
                try:
                    self.__assignment_services.update_deadline(assignment_id, new_deadline)
                except Exception as e:
                    print(e)
            case self.__EXIT:
                exit(0)
            case _:
                print(self.__ERRORS["INVALID_INPUT"])
                self.__update_assignment()

    def __list_assignments(self):
        for assignment in self.__assignment_services.get_assignments():
            print(assignment)


    def __give(self):
        print(self.__OPTIONS["GIVE_STUDENT"])
        print(self.__OPTIONS["GIVE_GROUP"])
        print(self.__OPTIONS["EXIT"])
        option = input(">")
        match option:
            case self.__GIVE_STUDENT:
                student_id = self.__get_student_id()
                assignment_id = self.__get_assignment_id()
                try:
                    self.__grade_services.add(student_id, assignment_id, 0) # Empty grade
                except Exception as e:
                    print(e)
            case self.__GIVE_GROUP:
                group = self.__get_student_group()
                assignment_id = self.__get_assignment_id() # Assignment to be assigned to the group
                for student in self.__student_services.get_group_of_students(group):
                    try:
                        self.__grade_services.add(student.id, assignment_id, 0)
                    except Exception as e:
                        print(e)
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
        # dict[int, dict[int, Grade]], so we get for a given student: assignments (: Grades)
        print("List of the assignments for this student:")
        for assignment in self.__grade_services.get_student_assignments(student_id):
            print(assignment)
        print("Select from this list an assignment which is ungraded to grade.")
        assignment_id = self.__get_assignment_id()
        grade = self.__get_grade()
        try:
            self.__grade_services.update_grade(student_id, assignment_id, grade)
        except Exception as e:
            print(e)

    def __menu(self):
        while (True):
            print(self.__OPTIONS["MANAGE"])
            print(self.__OPTIONS["GIVE"])
            print(self.__OPTIONS["GRADE"])
            print(self.__OPTIONS["EXIT"])
            option = input("> ")
            match option:
                case self.__MANAGE:
                    self.__manage()
                case self.__GIVE:
                    self.__give()
                case self.__GRADE:
                    self.__grade()
                case self.__EXIT:
                    exit(0)
                case _:
                    print(self.__ERRORS["INVALID_INPUT"])


