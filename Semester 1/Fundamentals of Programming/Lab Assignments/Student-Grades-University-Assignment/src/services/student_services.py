from src.repository.binary_repo import StudentBinaryRepo
from src.repository.text_repo import StudentTextRepo
from src.repository.memory_repo import StudentMemoryRepo

class StudentServices(object):
    def __init__(self, student_repo: StudentBinaryRepo | StudentMemoryRepo | StudentTextRepo, grades_repo):
        self.__student_repo = student_repo
        self.__grades_repo = grades_repo

    def get_student(self, student_id: int):
        return self.__student_repo[student_id]

    def get_name(self, student_id: int):
        return self.__student_repo[student_id].name

    def get_group(self, student_id: int):
        return self.__student_repo[student_id].group

    def get_students(self):
        student_list = []
        for student in self.__student_repo:
            student_list.append(student)
        return student_list

    def get_group_of_students(self, group):
        student_list = []
        for student in self.__student_repo:
            if student.group == group:
                student_list.append(student)
        return student_list

    def add(self, id: int, name: str, group: int):
        """
        Adds a student in the memory list of students.
        :param id: The student id
        :param name: The student name
        :param group: The group of the student
        :return: None
        """
        self.__student_repo.add(id, name, group)

    def remove(self, id: int):
        """
        Removes a student with a specific ID from the list of students
        :param id: The identification ID of the student to delete.
        :return: None
        """
        self.__student_repo.remove(id)
        self.__grades_repo.remove_student(id)

    def update_name(self, id: int, new_name: str) -> None:
        """
        Updates the name of a given student by its ID
        :param id: The id of the student
        :param new_name: The new name the student should have
        :return: None
        """
        self.__student_repo.update_name(id, new_name)

    def update_group(self, id: int, new_group: int) -> None:
        """
        Updates the group of a given student by its ID
        :param id: The id of the student
        :param new_group: The new group the student should have
        :return: None
        """
        self.__student_repo.update_group(id, new_group)

