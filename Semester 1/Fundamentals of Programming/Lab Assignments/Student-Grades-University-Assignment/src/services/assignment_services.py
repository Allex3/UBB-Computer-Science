from datetime import datetime

from src.domain.assignment import Assignment
from src.repository.binary_repo import AssignmentBinaryRepo
from src.repository.text_repo import AssignmentTextRepo
from src.repository.memory_repo import AssignmentMemoryRepo

class AssignmentServices(object):
    def __init__(self, assignment_repo, grade_repo):
        self.__assignment_repo = assignment_repo
        self.__grade_repo = grade_repo

    def get_description(self, assignment_id):
        return self.__assignment_repo[assignment_id].description

    def get_deadline(self, assignment_id):
        return self.__assignment_repo[assignment_id].deadline

    def get_assignments(self):
        assignment_list = []
        for assignment in self.__assignment_repo:
            assignment_list.append(assignment)
        return assignment_list

    def add(self, id: int, description: str, deadline: datetime) -> None:
        """
        Adds a student in the memory list of assignments.
        :param id: The assignment id
        :param description: The assignment's description
        :param deadline: The assignment's deadline
        :return: None
        """
        self.__assignment_repo.add(id, description, deadline)

    def remove(self, id: int) -> None:
        """
        Removes an assignment with a specific ID from the list of assignments.
        :param id: The identification ID of the assignment to delete.
        :return: None
        """
        self.__assignment_repo.remove(id)
        self.__grade_repo.remove_assignment(id)

    def update_description(self, id: int, new_description: str) -> None:
        """
        Updates the description of a given assignment by its ID
        :param id: The id of the assignment
        :param new_description: The new description the assignment should have
        :return: None
        """
        self.__assignment_repo.update_description(id, new_description)

    def update_deadline(self, id: int, new_deadline: datetime) -> None:
        """
        Updates the group of a given assignment by its ID
        :param id: The id of the assignment
        :param new_deadline: The new deadline of the assignment
        :return: None
        """
        self.__assignment_repo.update_deadline(id, new_deadline)

