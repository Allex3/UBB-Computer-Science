import unittest
from datetime import datetime

from src.services.grade_services import GradeServices, GradeBinaryRepo, GradeTextRepo, GradeMemoryRepo, GradeError, Grade
from src.services.assignment_services import AssignmentMemoryRepo, AssignmentServices, Assignment, AssignmentBinaryRepo, AssignmentTextRepo
from src.services.student_services import StudentMemoryRepo, StudentTextRepo, StudentBinaryRepo, StudentServices
from src.repository.repo_error import RepositoryError
from src.domain.assignment import AssignmentError
from src.domain.student import StudentError

student_memory_repo = StudentMemoryRepo()
assignment_memory_repo = AssignmentMemoryRepo()
grade_memory_repo = GradeMemoryRepo()
student_services = StudentServices(student_memory_repo, grade_memory_repo)
assignment_services = AssignmentServices(assignment_memory_repo, grade_memory_repo)
grade_services = GradeServices(grade_memory_repo, student_memory_repo, assignment_memory_repo)

class TestFirstFunctionality(unittest.TestCase):
    def test_add_student(self):
        try:
            student_memory_repo.add(1, "Alex", 4)
            student_services.add(1, "Alex", 4)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            student_services.add(30, "Alex", 4)
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)

    def test_add_assignment(self):
        try:
            assignment_memory_repo.add(1, "Alex", datetime.now())
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            assignment_services.add(1, "Alex", datetime.now())
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            assignment_services.add(30, "Alex", datetime.now())
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)

    def test_add_grade(self):
        try:
            grade_memory_repo.add(300, 2, 4)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            grade_memory_repo.add(1, 1, 100)
            self.assertTrue(False)
        except GradeError:
            self.assertTrue(True)

        try:
            grade_services.add(30, 10, 5)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            grade_services.add(30, 10, 5)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            grade_services.add(1, 1, 5)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def test_remove_student(self):
        try:
            student_services.remove(66)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)
        try:
            student_services.remove(1)
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)
    def test_remove_assignment(self):
        try:
            assignment_services.remove(100)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

    def test_remove_grade(self):
        try:
            grade_services.remove(100, 50)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)
    def test_update_student(self):
        student_services.update_group(4, 3)
        self.assertTrue(student_memory_repo[4].group == 3)
        student_services.update_name(4, "aaa")
        self.assertTrue(student_memory_repo[4].name == "aaa")

    def test_update_assignment(self):
        assignment_services.update_description(5, "aaa")
        self.assertTrue(assignment_memory_repo[5].description == "aaa")
        date = datetime.now()
        assignment_services.update_deadline(5, date)
        self.assertTrue(assignment_memory_repo[5].deadline == date)

    def test_update_grade(self):
        grade_services.add(6, 5, 10)
        try:
            grade_services.update_grade(6, 5,5)
            self.assertTrue(False)
        except GradeError:
            self.assertTrue(True)

        try:
            grade_services.add(6, 5, 10)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)


if __name__=="__main__":
    unittest.main()