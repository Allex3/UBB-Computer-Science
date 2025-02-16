class GradeError(Exception):
    pass

class Grade(object):
    def __init__(self, student_id: int, assignment_id: int, grade_value: int):
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.grade_value = grade_value

    @property
    def assignment_id(self):
        return self.__assignment_id
    @assignment_id.setter
    def assignment_id(self, id: int):
        if id<0:
            raise GradeError("The ID should be a positive integer.")
        self.__assignment_id = id

    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, id: int):
        if id<0:
            raise GradeError("The ID should be a positive integer.")
        self.__student_id = id

    @property
    def grade_value(self):
        return self.__grade_value
    @grade_value.setter
    def grade_value(self, value):
        if not (0<=value<=10):
            raise GradeError("Your grade should be between 1 and 10, integer numbers")
        self.__grade_value = value

    def __str__(self):
        return f"{str(self.__student_id)} - {str(self.__assignment_id)} - {str(self.__grade_value)}"

