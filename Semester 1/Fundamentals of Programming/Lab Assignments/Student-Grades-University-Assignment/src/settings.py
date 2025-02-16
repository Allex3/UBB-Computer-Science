from repository.memory_repo import StudentMemoryRepo, AssignmentMemoryRepo, GradeMemoryRepo
from repository.text_repo import StudentTextRepo, AssignmentTextRepo, GradeTextRepo
from repository.binary_repo import StudentBinaryRepo, AssignmentBinaryRepo, GradeBinaryRepo
from services.grade_services import GradeServices
from services.assignment_services import AssignmentServices
from services.student_services import StudentServices
from services.undo_services import UndoServices
from ui.application import Application
from ui.application_GUI import ApplicationGUI

class Parser:
    def __init__(self, UI_type: str = "UI"):
        self.__UI_type = UI_type

    def parse_settings(self):
        lines = open("settings.properties", "r").read().lower().split("\n")

        MEMORY = "inmemory"
        TEXT = "textfiles"
        BINARY = "binaryfiles"

        student_repo_init = {MEMORY: StudentMemoryRepo,
                             TEXT: StudentTextRepo,
                             BINARY: StudentBinaryRepo}
        assignment_repo_init = {MEMORY: AssignmentMemoryRepo,
                                TEXT: AssignmentTextRepo,
                                BINARY: AssignmentBinaryRepo}
        grade_repo_init = {MEMORY: GradeMemoryRepo,
                           TEXT: GradeTextRepo,
                           BINARY: GradeBinaryRepo}

        repo_type = lines[0].split("=")[1].strip(" ")
        student_file = lines[1].split("=")[1].strip(" ")
        assignment_file = lines[2].split("=")[1].strip(" ")
        grade_file = lines[3].split("=")[1].strip(" ")

        if repo_type == "inmemory":
            student_repo = student_repo_init[repo_type]()
            assignment_repo = assignment_repo_init[repo_type]()
            grade_repo = grade_repo_init[repo_type]()
        else:
            student_repo = student_repo_init[repo_type](student_file)
            assignment_repo = assignment_repo_init[repo_type](assignment_file)
            grade_repo = grade_repo_init[repo_type](grade_file)

        student_services = StudentServices(student_repo, grade_repo)
        assignment_services = AssignmentServices(assignment_repo, grade_repo)
        grade_services = GradeServices(grade_repo, student_repo, assignment_repo)
        undo_services = UndoServices()

        if self.__UI_type == "UI":
            return Application(student_services, assignment_services, grade_services, undo_services)
        elif self.__UI_type == "GUI":
            return ApplicationGUI(student_services, assignment_services, grade_services, undo_services)