import unittest
from datetime import datetime

from fontTools.pens.recordingPen import RecordingPen

from src.services.grade_services import GradeServices, GradeBinaryRepo, GradeTextRepo, GradeMemoryRepo, GradeError, \
    Grade
from src.services.assignment_services import AssignmentMemoryRepo, AssignmentServices, Assignment, AssignmentBinaryRepo, \
    AssignmentTextRepo
from src.services.student_services import StudentMemoryRepo, StudentTextRepo, StudentBinaryRepo, StudentServices
from src.repository.repo_error import RepositoryError
from src.domain.assignment import AssignmentError
from src.domain.student import StudentError, Student
from src.services.undo_services import UndoServices, UndoException
from src.commands.command import *

student_memory_repo = StudentMemoryRepo()
assignment_memory_repo = AssignmentMemoryRepo()
grade_memory_repo = GradeMemoryRepo()
student_services = StudentServices(student_memory_repo, grade_memory_repo)
assignment_services = AssignmentServices(assignment_memory_repo, grade_memory_repo)
grade_services = GradeServices(grade_memory_repo, student_memory_repo, assignment_memory_repo)
undo_services = UndoServices()


class TestFirstFunctionality(unittest.TestCase): # pragma: no cover
    def test_domain(self):
        self.assertRaises(AssignmentError, Assignment, -1, "aaa", datetime.now())
        str(Assignment(1, "aaa", datetime.now()))
        self.assertRaises(GradeError, Grade, -1, 1, 3)
        self.assertRaises(GradeError, Grade, 1, -1, 3)
        str(Grade(1, 1, 5))

        self.assertRaises(StudentError, Student, -1, "aa", 3)
        self.assertRaises(StudentError, Student, 1, "aaa", -3)
        str(Student(1, "aaa", 3))
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
        self.assertRaises(RepositoryError, grade_services.add, 300, 2, 4)

        self.assertRaises(RepositoryError, grade_services.add, 1, 1, 100)

        self.assertRaises(RepositoryError, grade_services.add, 30, 10, 5)

        try:
            student_services.add(123, "aaa", 4)
            grade_services.add(123, 2, 5)
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
        grade_services.add(123, 10, 5)
        try:
            grade_services.remove(123, 10)
        except RepositoryError:
            self.fail("Remove grade fail")
        self.assertRaises(RepositoryError, grade_services.remove, 100, 50)
        self.assertRaises(RepositoryError, grade_services.remove, 1, 1)

    def test_grade_assignment(self):
        grade_services.assign(123, 1)
        grade_services.grade_assignment(123, 1, 10)
        self.assertRaises(GradeError, grade_services.grade_assignment, 123, 1, 100)

    def test_assign(self):
        student_services.add(40, "aaa", 3)
        assignment_services.add(40, "aaa", datetime.now())
        grade_services.assign(40, 40)
        self.assertRaises(RepositoryError, grade_services.assign, 100, 5)
        self.assertRaises(RepositoryError, grade_services.assign, 1, 50)

    def test_assign_group(self):
        student_services.add(121, "aaa", 2)
        grade_services.assign_group(2, 6)
        grade_services.assign_group(2, 6)
        grade_services.assign_group(2, 7)
        grade_services.remove_student(121)
        grade_services.remove_assignment(6)
        grade_services.remove_group_assignment(2, 7)
        self.assertRaises(RepositoryError, grade_services.add, 1, 319439, 2)

    def test_statistics(self):
        grade_services.get_late_student_grades()
        grade_services.get_student_grades(2)
        grade_services.get_assignment_grades(2)
        grade_services.get_best_students_grades()
        grade_services.grade_descending(6)
        grade_services.get_grade(40, 40)

        self.assertRaises(RepositoryError, grade_services.get_grade, 1312, 1321)
        student_services.add(1, "aaa", 3)
        student_services.get_student(1)
        student_services.get_students()
        student_services.get_group(1)
        student_services.get_name(1)
        assignment_services.add(25, "aaa", datetime.now())
        assignment_services.get_assignments()
        assignment_services.get_deadline(25)
        assignment_services.get_description(25)
        student_services.get_group_of_students(1)

    def test_undo(self):
        add_student_command = Command(student_services.add, 666, "Alex", 3)
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        add_student_command()
        undo_services.undo()

        undo_services.redo()
        self.assertRaises(UndoException, undo_services.redo)
        undo_services.undo()
        self.assertRaises(UndoException, undo_services.undo)

        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))
        add_student_command()
        undo_services.undo()
        undo_services.record(CommandUndoRedo(add_student_command, Command(student_services.remove, 666)))

    def test_commands(self):
        assign = Assign(grade_services.assign_group, 2, 1)
        assign()
        assign()

        assign_grades = AddAssignmentWithGrades([Grade(1, 222, 5)], grade_services.add, assignment_services.add, 222,
                                                "aaa", datetime.now())
        assign_grades()

        student_grades = AddStudentWithGrades([Grade(222, 222, 5)], grade_services.add, student_services.add, 222,
                                              "alex", 3)
        student_grades()

    def test_repo_exceptions(self):
        self.assertRaises(RepositoryError, student_memory_repo.update_name,1234, "aaaa")

        self.assertRaises(RepositoryError, student_memory_repo.update_group, 1234, 5)

        self.assertRaises(RepositoryError, assignment_memory_repo.update_description, 1234, "aaaa")

        self.assertRaises(RepositoryError, assignment_memory_repo.update_deadline, 1234, datetime.now())

        student_services.add(456, "aaa", 3)
        assignment_services.add(456, "aaa", datetime.now())
        grade_services.assign(456, 456)
        self.assertRaises(RepositoryError, grade_services.add, 456, 456, 5)

        grade_services.remove(456, 456)
        self.assertRaises(RepositoryError, grade_services.add, 456, 456, 100)




if __name__ == "__main__":
    unittest.main()
