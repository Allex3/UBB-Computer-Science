from datetime import datetime, timedelta
from random import randint
from typing import Any

from jinja2.nodes import Assign

from src.domain.assignment import Assignment, AssignmentError
from src.domain.student import Student, StudentError
from src.domain.grade import Grade, GradeError
from faker import Faker
from src.repository.repo_error import RepositoryError

class SingleRepoIterator(object):
    def __init__(self, data: dict):
        self.__data = data
        self.__index = -1
        self.__ids = list(data.keys())

    def __next__(self):
        self.__index +=1
        if self.__index >= len(self.__data):
            raise StopIteration
        data_point = self.__data[self.__ids[self.__index]]
        return data_point

class StudentMemoryRepo(object):
    def __init__(self):
        self.__fake = Faker()
        self._students : dict[int, Student] = {}

        self.__generate_random_20()

    def __iter__(self):
        return SingleRepoIterator(self._students)
    def __getitem__(self, item):
        return self._students[item]

    def __generate_random_20(self) -> None:
        """
        Generated 20 random students and puts them in memory.
        :return: None
        """
        # Groups will be random from 1 to 4
        for i in range(20):
            # Generating student with ID i
            name = self.__fake.name()
            group = randint(1, 4)
            student : Student = Student(i, name, group)
            # For generating a grade, we take a random assignment and a random student
            # From the ones we generated until now, from 0 to i
            grade: Grade = Grade(randint(0, i), randint(0, i), randint(1, 10))

            self._students[i] = student

    def add(self, id: int, name: str, group: int) -> None:
        """
        Adds a student in the memory list of students.
        :param id: The student id
        :param name: The student name
        :param group: The group of the student
        :return: None
        """
        if id in self._students:
            raise RepositoryError(f"This student ID ({id}) already exists, cannot add student.")
        self._students[id] = Student(id, name, group)

    def remove(self, id: int) -> None:
        """
        Removes a student with a specific ID from the list of students
        :param id: The identification ID of the student to delete.
        :return: None
        """
        if id not in self._students:
            raise RepositoryError(f"This student ID ({id}) does not exist, cannot delete a non-existent student.")
        del self._students[id]

    def update_name(self, id: int, new_name: str) -> None:
        """
        Updates the name of a given student by its ID
        :param id: The id of the student
        :param new_name: The new name the student should have
        :return: None
        """
        if id not in self._students:
            raise RepositoryError(f"This student ID ({id}) does not exist, cannot update a non-existent student.")
        self._students[id].name = new_name

    def update_group(self, id: int, new_group: int) -> None:
        """
        Updates the group of a given student by its ID
        :param id: The id of the student
        :param new_group: The new group the student should have
        :return: None
        """
        if id not in self._students:
            raise RepositoryError(f"This student ID ({id}) does not exist, cannot update a non-existent student.")
        self._students[id].group = new_group


class AssignmentMemoryRepo(object):
    def __init__(self):
        self.__fake = Faker()
        self._assignments: dict[int, Assignment] = {}

        self.__generate_random_20()

    def __generate_random_20(self) -> None:
        """
        Generated 20 random assignments and puts them in memory.
        :return: None
        """
        for i in range(20):
            # Generating Assignment with ID i
            description: str = self.__fake.sentence(nb_words=10)
            deadline: datetime.date = datetime.now() + timedelta(days=randint(4, 10))
            assignment: Assignment = Assignment(i, description, deadline)

            self._assignments[i] = assignment

    def __iter__(self):
        return SingleRepoIterator(self._assignments)

    def __getitem__(self, item):
        return self._assignments[item]

    def add(self, id: int, description: str, deadline: datetime) -> None:
        """
        Adds a student in the memory list of assignments.
        :param id: The assignment id
        :param description: The assignment's description
        :param deadline: The assignment's deadline
        :return: None
        """
        if id in self._assignments:
            raise RepositoryError(f"This assignment ID ({id}) already exists, cannot add assignment.")
        self._assignments[id] = Assignment(id, description, deadline)

    def remove(self, id: int) -> None:
        """
        Removes an assignment with a specific ID from the list of assignments.
        :param id: The identification ID of the assignment to delete.
        :return: None
        """
        if id not in self._assignments:
            raise RepositoryError(f"This assignment ID ({id}) does not exist, cannot delete a non-existent assignment.")
        del self._assignments[id]

    def update_description(self, id: int, new_description: str) -> None:
        """
        Updates the description of a given assignment by its ID
        :param id: The id of the student
        :param new_description: The new description the assignment should have
        :return: None
        """
        if id not in self._assignments:
            raise RepositoryError(f"This assignment ID ({id}) does not exist, cannot update a non-existent assignment.")
        self._assignments[id].description = new_description

    def update_deadline(self, id: int, new_deadline: datetime.date) -> None:
        """
        Updates the group of a given student by its ID
        :param id: The id of the student
        :param new_deadline: The new deadline of the assignment
        :return: None
        """
        if id not in self._assignments:
            raise RepositoryError(f"This assignment ID ({id}) does not exist, cannot update a non-existent assignment.")
        self._assignments[id].deadline = new_deadline


class GradeMemoryRepo(object):
    def __init__(self):
        self.__fake = Faker()
        self._grades: dict[int, dict[int, Grade]] = {}

        self.__generate_random_20()

    def __generate_random_20(self) -> None:
        """
        Generated 20 random grades and puts them in memory.
        :return: None
        """
        for i in range(20):
            # For generating a grade, we take a random assignment for all the students
            # From 0 to 19, because that is the number of students and assignments
            grade: Grade = Grade(i, randint(0, 19), randint(1, 10))
            self._grades[grade.student_id] = {} # define the dictionary of the assignments of a student
            self._grades[grade.student_id][grade.assignment_id] = grade

    def __getitem__(self, item):
        return self._grades[item]

    def add(self, student_id: int, assignment_id: int, grade_value: int) -> None:
        """
        Adds a grade for a given student and assignment in the memory list of grades.
        :param student_id: The student id
        :param assignment_id: The assignment's id
        :param grade_value: The grade value (1-10)
        :return: None
        """
        # Check if the assignment we want to grade is already graded (already in the list of assignments of that student basically, only graded assignments are in the list of assignments of a student)
        if student_id not in self._grades:
            raise RepositoryError(f"This student ID ({student_id}) does not exist, cannot add an assignment to a non-existent student.")
        if assignment_id in self._grades[student_id]:
            raise RepositoryError(f"This assignment ID ({assignment_id}) is already added for the student (ID {student_id}), cannot add a new grade for it.")
        self._grades[student_id][assignment_id] = Grade(student_id, assignment_id, grade_value)

    def remove(self, student_id: int, assignment_id: int) -> None:
        """
        Removes a grade from a specific student and an assignment of theirs.
        :param student_id: The identification ID of the student
        :param assignment_id: The assignment ID of the student's assignment
        :return: None
        """
        if student_id not in self._grades:
            raise RepositoryError(f"This student ID ({student_id}) does not exist, cannot delete an assignment from a non-existent student.")
        if assignment_id not in self._grades[student_id]:
            raise RepositoryError(
                f"This assignment ID ({assignment_id}) does not exist, cannot delete an assignment that is not given to this student (student ID = {student_id}).")
        del self._grades[student_id][assignment_id]

    def update_grade(self, student_id: int, assignment_id: int, new_grade: int):
        if student_id not in self._grades:
            raise RepositoryError(f"This student ID ({student_id}) does not exist, cannot delete an assignment from a non-existent student.")
        if assignment_id not in self._grades[student_id]:
            raise RepositoryError(f"Student {student_id} doesn't have this assignment with ID {assignment_id}")

        if self._grades[student_id][assignment_id].grade_value != 0:
            raise GradeError("Grade already given for this student (!=0)")
        self._grades[student_id][assignment_id].grade_value = new_grade

    def __iter__(self):
        return SingleRepoIterator(self._grades)

    def remove_student(self, student_id: int):
        """
        Remove a whole student
        :param student_id: The student to remove
        :return: None
        """
        del self._grades[student_id]

    def remove_assignment(self, student_id: int, assignment_id: int):
        """
        Remove a whole student
        :param student_id: The student to remove
        :param assignment_id: The ID of the assignment to remove
        :return: None
        """
        del self._grades[student_id][assignment_id]