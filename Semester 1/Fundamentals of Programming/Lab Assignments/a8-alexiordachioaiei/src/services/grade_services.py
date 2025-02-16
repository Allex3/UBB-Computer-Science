from src.repository.repo_error import RepositoryError
from src.domain.grade import Grade, GradeError
from src.repository.binary_repo import GradeBinaryRepo
from src.repository.text_repo import GradeTextRepo
from src.repository.memory_repo import GradeMemoryRepo

class GradeServices(object):
    def __init__(self, grade_repo, student_repo, assignment_repo):
        self.__grade_repo = grade_repo
        self.__student_repo = student_repo
        self.__assignment_repo = assignment_repo

    def grade_assignment(self, student_id: int, assignment_id: int, grade: int):
        self.__grade_repo.update_grade(student_id, assignment_id, grade)

    def get_student_assignments(self, student_id: int):
        student_assignments = []
        for student in self.__grade_repo:
            for assignment in list(student.values()):
                if assignment.student_id == student_id:
                    student_assignments.append(assignment)
        return student_assignments
    def add(self, student_id: int, assignment_id: int, grade_value: int) -> None:
        """
        Adds a grade for a given student and assignment in the memory list of grades.
        :param student_id: The student id
        :param assignment_id: The assignment's id
        :param grade_value: The grade value (1-10)
        :return: None
        """
        self.__grade_repo.add(student_id, assignment_id, grade_value)

    def remove_student(self, student_id: int):
        """
        Remove a whole student
        :param student_id: The student to remove
        :return: None
        """
        self.__grade_repo.remove_student(student_id)

    def remove(self, student_id: int, assignment_id: int) -> None:
        """
        Removes a grade from a specific student and an assignment of theirs.
        :param student_id: The identification ID of the student
        :param assignment_id: The assignment ID of the student's assignment
        :return: None
        """
        self.__grade_repo.remove(student_id, assignment_id)

    def update_grade(self, student_id: int, assignment_id: int, new_grade: int):
        self.__grade_repo.update_grade(student_id, assignment_id, new_grade)
