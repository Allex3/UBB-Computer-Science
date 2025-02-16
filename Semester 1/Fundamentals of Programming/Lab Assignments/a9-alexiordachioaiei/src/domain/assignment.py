from datetime import datetime

class AssignmentError(Exception):
    pass

class Assignment(object):
    def __init__(self, assignment_id: int, description: str, deadline: datetime.date):
        self.id = assignment_id
        self.description = description
        self.deadline = deadline

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        if id<0:
            raise AssignmentError("The ID should be a positive integer.")
        self.__id = id

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def deadline(self):
        return self.__deadline
    @deadline.setter
    def deadline(self, deadline: datetime.date):
        self.__deadline = deadline

    def __str__(self):
        return f"{str(self.__id)} ; {self.__description} ; {self.__deadline.strftime("%Y-%m-%d %H:%M:%S")}"




