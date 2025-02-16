import unittest
from datetime import datetime

from fontTools.pens.recordingPen import RecordingPen

from src.services.grade_services import GradeServices, GradeBinaryRepo, GradeTextRepo, GradeMemoryRepo, GradeError, Grade
from src.services.assignment_services import AssignmentMemoryRepo, AssignmentServices, Assignment, AssignmentBinaryRepo, AssignmentTextRepo
from src.services.student_services import StudentMemoryRepo, StudentTextRepo, StudentBinaryRepo, StudentServices
from src.repository.repo_error import RepositoryError
from src.domain.assignment import AssignmentError
from src.domain.student import StudentError
from src.services.undo_services import UndoServices, UndoException
from src.commands.command import *

student_memory_repo = StudentMemoryRepo()
assignment_memory_repo = AssignmentMemoryRepo()
grade_memory_repo = GradeMemoryRepo()
student_services = StudentServices(student_memory_repo, grade_memory_repo)
assignment_services = AssignmentServices(assignment_memory_repo, grade_memory_repo)
grade_services = GradeServices(grade_memory_repo, student_memory_repo, assignment_memory_repo)
undo_services = UndoServices()

class TestFirstFunctionality(unittest.TestCase):
    def test_add_student(self):
        student_memory_repo.add(20, "Alex", 4)
        try:
            student_services.add(20, "Alex", 4)
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            student_services.add(30, "Alex", 4)
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)

    def test_add_assignment(self):
        assignment_memory_repo.add(20, "Alex", datetime.now())
        try:
            assignment_memory_repo.add(20, "Alex", datetime.now())
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            assignment_services.add(20, "Alex", datetime.now())
            self.assertTrue(False)
        except RepositoryError:
            self.assertTrue(True)

        try:
            assignment_services.add(30, "Alex", datetime.now())
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)

    def test_add_grade(self):
        self.assertRaises(RepositoryError, grade_services.add,300, 2, 4)

        self.assertRaises(RepositoryError, grade_services.add, 1, 1, 100)

        self.assertRaises(RepositoryError, grade_services.add, 30, 10, 5)

        try:
            grade_services.add(1, 2, 5)
        except:
            self.fail("Add grade fail")

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
        grade_services.add(3, 3, 10)
        self.assertRaises(RepositoryError, grade_services.grade_assignment, 100, 5, 5)

    def test_remove_student(self):
        self.assertRaises(RepositoryError, student_services.remove, 66)
        try:
            student_services.remove(1)
        except RepositoryError:
            self.fail("Remove student fail")
    def test_remove_assignment(self):
        self.assertRaises(RepositoryError, assignment_services.remove, 100)
        try:
            assignment_services.remove(1)
        except RepositoryError:
            self.fail("Remove assignment fail")

    def test_remove_grade(self):
        grade_services.add(10, 10, 5)
        try:
            grade_services.remove(10, 10)
        except RepositoryError:
            self.fail("Remove grade fail")
        self.assertRaises(RepositoryError, grade_services.remove, 100, 50)
        self.assertRaises(RepositoryError, grade_services.remove, 1, 1)

    def test_grade_assignment(self):
        grade_services.assign(1, 1)
        grade_services.grade_assignment(1, 1, 10)
        self.assertRaises(GradeError, grade_services.grade_assignment, 1, 1, 100)

    def test_assign(self):
        student_services.add(40, "aaa", 3)
        assignment_services.add(40, "aaa", datetime.now())
        grade_services.assign(40, 40)
        self.assertRaises(RepositoryError, grade_services.assign, 100, 5)
        self.assertRaises(RepositoryError, grade_services.assign, 1, 50)

    def test_assign_group(self):
        grade_services.assign_group(2, 6)

    def test_statistics(self):
        grade_services.get_late_student_grades()
        grade_services.get_student_grades(2)
        grade_services.get_assignment_grades(2)
        grade_services.get_best_students_grades()
        grade_services.grade_descending(6)
        grade_services.get_grade(40, 40)

    def test_undo(self):
        add_student_command = Command(student_services.add,666, "Alex", 3)
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        add_student_command()
        undo_services.undo()

        undo_services.redo()
        undo_services.undo()
        self.assertRaises(UndoException, undo_services.undo)

        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        add_student_command()
        undo_services.undo()
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))

if __name__=="__main__":
    unittest.main()