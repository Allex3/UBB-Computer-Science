"""
Main file of project
My problem: 2
"""
from jinja2.nodes import Assign

"""
Tests & Specifications
    - For the 1st functionality NON-Ui functions 
    PyUnit

User input validation
    - The program does not crash
    - Entity list should make sense ?
    create Exception Classes: ValidateError, RepoException
"""

from repository.memory_repo import StudentMemoryRepo, AssignmentMemoryRepo, GradeMemoryRepo
from repository.text_repo import StudentTextRepo, AssignmentTextRepo, GradeTextRepo
from repository.binary_repo import StudentBinaryRepo, AssignmentBinaryRepo, GradeBinaryRepo
from services.grade_services import GradeServices
from services.assignment_services import AssignmentServices
from services.student_services import StudentServices
from ui.ui import UI


def parse_settings():
    fin = open("settings.properties", "r")
    lines = fin.readlines()

    repo_type = lines[0].strip("\n").split("=")[1].strip(" ")
    student_file = lines[1].strip("\n").split("=")[1].strip(" ")
    assignment_file = lines[2].strip("\n").split("=")[1].strip(" ")
    grade_file = lines[3].strip("\n").split("=")[1].strip(" ")
    match repo_type:
        case "inmemory":
            student_repo = StudentMemoryRepo()
            assignment_repo = AssignmentMemoryRepo()
            grade_repo = GradeMemoryRepo()
            student_services = StudentServices(student_repo, grade_repo)
            assignment_services = AssignmentServices(assignment_repo, grade_repo)
            grade_services = GradeServices(grade_repo, student_repo, assignment_repo)
            return UI(student_services, assignment_services, grade_services)
        case "textfiles":
            student_services = StudentServices(StudentTextRepo(student_file), GradeTextRepo(grade_file))
            assignment_services = AssignmentServices(
                AssignmentTextRepo(assignment_file), GradeTextRepo(grade_file))
            grade_services = GradeServices(GradeTextRepo(grade_file), StudentTextRepo(student_file), AssignmentTextRepo(assignment_file))
            return UI(student_services, assignment_services, grade_services)
        case "binaryfiles":
            student_services = StudentServices(StudentBinaryRepo(student_file), GradeBinaryRepo(grade_file))
            assignment_services = AssignmentServices(
                AssignmentBinaryRepo(assignment_file), GradeBinaryRepo(grade_file))
            grade_services = GradeServices(GradeBinaryRepo(grade_file), StudentBinaryRepo(student_file), AssignmentBinaryRepo(assignment_file))
            return UI(student_services, assignment_services, grade_services)


if __name__ == "__main__":
    UI = parse_settings()
    UI.open_menu()
