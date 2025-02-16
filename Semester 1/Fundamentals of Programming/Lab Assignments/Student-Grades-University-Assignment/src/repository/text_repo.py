from datetime import datetime

from src.repository.memory_repo import StudentMemoryRepo, AssignmentMemoryRepo, GradeMemoryRepo, Student, Grade, Assignment, RepositoryError
from src.domain.grade import GradeError


class StudentTextRepo(StudentMemoryRepo):
    def __init__(self, file_path: str):
        super().__init__()
        self.__file_path = file_path
        self.__load()

    def __load(self) -> None:
        fin = open(self.__file_path, "r")
        if fin.read() == "": # If the file is empty DO NOT load from file in memory, but load from the randomly generated students in the file
            fin.close()
            self.__save()
            return
        # Reached here, the file is not empty, so load from file to memory
        fin.close()
        self._students: dict[int, Student] = {}
        fin = open(self.__file_path, "r")
        lines = fin.readlines()
        for line in lines:
            id = int(line.split("-")[0].strip())
            name = line.split("-")[1].strip()
            group = int(line.split("-")[2].strip())
            self._students[id] = Student(id, name, group)
        fin.close()

    def __save(self):
        fout = open(self.__file_path, "w")
        for student in self._students.values():
            fout.write(f"{student}\n")
        fout.close()

    def add(self, id: int, name: str, group: int) -> None:
        """
        Adds a student in the memory list of students.
        :param id: The student id
        :param name: The student name
        :param group: The group of the student
        :return: None
        """
        super().add(id, name, group)
        self.__save()

    def remove(self, id: int):
        super().remove(id)
        self.__save()

    def update_name(self, id: int, new_name: str) -> None:
        super().update_name(id, new_name)
        self.__save()

    def update_group(self, id: int, new_group: int) -> None:
        super().update_group(id, new_group)
        self.__save()

class AssignmentTextRepo(AssignmentMemoryRepo):
    def __init__(self, file_path: str):
        super().__init__()
        self.__file_path = file_path
        self.__load()

    def __load(self) -> None:
        fin = open(self.__file_path, "r")
        if fin.read() == "":  # If the file is empty DO NOT load from file in memory, but load from the randomly generated students in the file
            fin.close()
            self.__save()
            return
        # Reached here, the file is not empty, so load from file to memory
        fin.close()
        self._assignments: dict[int, Assignment] = {}
        fin = open(self.__file_path, "r")
        lines = fin.readlines()
        for line in lines:
            id = int(line.split(";")[0].strip())
            description = line.split(";")[1].strip()
            deadline = datetime.strptime(line.split(";")[2].strip(), "%Y-%m-%d %H:%M:%S")
            self._assignments[id] = Assignment(id, description, deadline)
        fin.close()

    def __save(self):
        fout = open(self.__file_path, "w")
        for assignment in self._assignments.values():
            fout.write(f"{assignment}\n")
        fout.close()

    def add(self, id: int, description: str, deadline: datetime) -> None:
        """
        Adds a student in the memory list of assignments.
        :param id: The assignment id
        :param description: The assignment's description
        :param deadline: The assignment's deadline
        :return: None
        """
        super().add(id, description, deadline)
        self.__save()

    def remove(self, id: int):
        super().remove(id)
        self.__save()

    def update_description(self, id: int, new_description: str) -> None:
        super().update_description(id, new_description)
        self.__save()

    def update_deadline(self, id: int, new_deadline: datetime) -> None:
        super().update_deadline(id, new_deadline)
        self.__save()

class GradeTextRepo(GradeMemoryRepo):
    def __init__(self, file_path: str):
        super().__init__()
        self.__file_path = file_path
        self.__load()

    def __load(self) -> None:
        fin = open(self.__file_path, "r")
        if fin.read() == "":  # If the file is empty DO NOT load from file in memory, but load from the randomly generated students in the file
            fin.close()
            self.__save()
            return
        # Reached here, the file is not empty, so load from file to memory
        fin.close()
        fin = open(self.__file_path, "r")
        lines = fin.readlines()
        self._grades = {}
        for line in lines:
            student_id = int(line.split("-")[0].strip())
            assignment_id = int(line.split("-")[1].strip())
            grade_value = int(line.split("-")[2].strip())
            self._grades[f"{str(student_id)} {str(assignment_id)}"] = Grade(student_id, assignment_id, grade_value)
        fin.close()

        for grade in self._grades.values():
            super()._compute_average(grade.student_id)

    def __save(self):
        fout = open(self.__file_path, "w")
        for grade in self._grades.values():
            fout.write(f"{grade}\n")
        fout.close()

    def assign(self, student_id: int, assignment_id: int) -> None:
        """
        Adds a grade for a given student and assignment in the memory list of grades.
        :param student_id: The student id
        :param assignment_id: The assignment's id
        :return: None
        """
        super().assign(student_id, assignment_id)
        self.__save()

    def add(self, student_id: int, assignment_id: int, grade_value: int) -> None:
        """
        Adds a grade for a given student and assignment in the memory list of grades.
        :param student_id: The student id
        :param assignment_id: The assignment's id
        :param grade_value: The grade value (1-10)
        :return: None
        """
        super().add(student_id, assignment_id, grade_value)
        self.__save()

    def remove(self, student_id: int, assignment_id: int):
        super().remove(student_id, assignment_id)
        self.__save()

    def grade_assignment(self, student_id: int, assignment_id: int, new_grade: int):
        super().grade_assignment(student_id, assignment_id, new_grade)
        self.__save()

    def remove_student(self, student_id: int):
        """
        Remove a whole student
        :param student_id: The student to remove
        :return: None
        """
        super().remove_student(student_id)
        self.__save()

    def remove_assignment(self,assignment_id: int):
        """
        Remove an assignment
        :param assignment_id: The ID of the assignment to remove
        :return: None
        """
        super().remove_assignment(assignment_id)
        self.__save()