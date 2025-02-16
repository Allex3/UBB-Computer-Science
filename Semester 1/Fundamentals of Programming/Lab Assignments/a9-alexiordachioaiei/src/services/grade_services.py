from datetime import datetime

from numpy.ma.extras import average

from src.repository.repo_error import RepositoryError
from src.domain.grade import Grade, GradeError
from src.repository.binary_repo import GradeBinaryRepo
from src.repository.text_repo import GradeTextRepo
from src.repository.memory_repo import GradeMemoryRepo, Grade, Assignment, Student

class Success(Exception):
    pass

class GradeServices(object):
    def __init__(self, grade_repo, student_repo, assignment_repo):
        self.__grade_repo = grade_repo
        self.__student_repo = student_repo
        self.__assignment_repo = assignment_repo

    def grade_assignment(self, student_id: int, assignment_id: int, grade: int):
        self.__grade_repo.grade_assignment(student_id, assignment_id, grade)

    def get_student_grades(self, student_id: int):
        student_grades = []
        for grade in self.__grade_repo:
            if grade.student_id == student_id:
                student_grades.append(grade)
        return student_grades

    def get_assignment_grades(self, assignment_id: int):
        """
        Gets all the grades for a specific assignment
        :param assignment_id: The assignment ID
        :return: None
        """
        assignment_grades = []
        for grade in self.__grade_repo:
            if assignment_id == grade.assignment_id:
                assignment_grades.append(grade)
        return assignment_grades

    def get_grade(self, student_id: int, assignment_id: int):
        try:
            return self.__grade_repo[f"{str(student_id)} {str(assignment_id)}"]
        except:
            raise RepositoryError("This student doesn't have such a grade, ungraded or not.")

    def add(self, student_id: int, assignment_id: int, grade_value: int) -> None:
        """
        Adds an assignment, ungraded, for a given student
        :param student_id: The student id
        :param assignment_id: The assignment's id
        :param grade_value: The grade
        :return: None
        """
        is_student = False
        for student in self.__student_repo:
            if student_id == student.id:
                is_student = True
                for assignment in self.__assignment_repo:
                    if assignment_id == assignment.id:
                        self.__grade_repo.add(student_id, assignment_id, grade_value)
                        return

        if is_student is False:
            raise RepositoryError(f"This student ID ({student_id}) does not exist.")
        else:
            raise RepositoryError(f"This assignment ID ({assignment_id}) does not exist.")

    def assign(self, student_id: int, assignment_id: int) -> None:
        """
        Adds an assignment, ungraded, for a given student
        :param student_id: The student id
        :param assignment_id: The assignment's id
        :return: None
        """
        is_student = False
        for student in self.__student_repo:
            if student_id == student.id:
                is_student = True
                for assignment in self.__assignment_repo:
                    if assignment_id == assignment.id:
                        self.__grade_repo.assign(student_id, assignment_id)
                        return

        if is_student is False:
            raise RepositoryError(f"This student ID ({student_id}) does not exist.")
        else:
            raise RepositoryError(f"This assignment ID ({assignment_id}) does not exist.")

    def assign_group(self, group: int, assignment_id: int):
        has_assignment = []
        for student in self.__student_repo:
            if student.group == group:
                try:
                    self.__grade_repo.assign(student.id, assignment_id)
                except RepositoryError: # Student already has assignment
                    has_assignment.append(student.id)

        return has_assignment


    def remove_student(self, student_id: int):
        """
        Remove a whole student
        :param student_id: The student to remove
        :return: None
        """
        self.__grade_repo.remove_student(student_id)

    def remove_assignment(self, assignment_id: int):
        self.__grade_repo.remove_assignment(assignment_id)

    def remove(self, student_id: int, assignment_id: int) -> None:
        """
        Removes a grade from a specific student and an assignment of theirs.
        :param student_id: The identification ID of the student
        :param assignment_id: The assignment ID of the student's assignment
        :return: None
        """
        self.__grade_repo.remove(student_id, assignment_id)

    def remove_group_assignment(self,  group: int, assignment_id: int):
        for student in self.__student_repo:
            if student.group == group:
                try:
                    self.__grade_repo.remove(student.id, assignment_id)
                except Exception as e:
                    continue

    def grade_descending(self, assignment_id: int):
        assignment_grades = self.get_assignment_grades(assignment_id)
        assignment_grades.sort(key = lambda grade: grade.grade_value, reverse=True) # :3
        return assignment_grades

    def get_late_student_grades(self):
        late_students = []
        for student in self.__student_repo:
            # Get this student's assignments and check if they are late for any at this moment in time
            # We check this by checking their 0 graded assignments and if the dates for those assignments are past due
            student_grades = self.get_student_grades(student.id)
            late_student_grades = []
            for grade in student_grades:
                if grade.grade_value == 0: # Check date of the assignment
                    assignment = self.__assignment_repo[grade.assignment_id]
                    if datetime.now() > assignment.deadline:
                        late_student_grades.append(grade) # We append the ungraded (grade) assignment at which this student is late

            if late_student_grades:
                late_students.append(late_student_grades)

        return late_students

    def get_best_students_grades(self):
        average_grades: dict[int, int] = self.__grade_repo.get_average_grades()
        average_grades_sorted = {k: v for k, v in sorted(average_grades.items(), key=lambda item:item[1], reverse=True)}
        # item[1] in pair (key, value) is sorting based on the value from the tuple of dictionary items
        # And for that sorted list of tuples, we reconstruct the dictionary with the key and value from the tuple, this time in order
        return average_grades_sorted

