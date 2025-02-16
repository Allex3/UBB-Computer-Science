class StudentError(Exception):
    pass

class Student(object):
    def __init__(self, student_id: int, name: str, group: int):
        self.id = student_id
        self.name = name
        self.group = group

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        if id<0:
            raise StudentError("The ID should be a positive integer.")
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, group: int):
        if group<0:
            raise StudentError("The group should be a positive integer.")
        self.__group = group

    def __str__(self):
        return f"{str(self.__id)} - {self.__name} - {str(self.__group)}"


