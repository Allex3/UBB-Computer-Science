class AverageGrade:
    def __init__(self, student_id, grades: dict[int, int]):
        # dict[assignment_id] = grade_value
        self.__student_id = student_id
        self.__average = None
        self.grades = grades
        self.compute_average()

    @property
    def student_id(self):
        return self.__student_id

    def compute_average(self):
        if len(self.grades) == 0:
            self.__average = 0
            return

        average = 0
        for grade in self.grades.values():
            average += grade

        average = round(average / len(self.grades), 2)
        self.__average = average

    @property
    def average(self):
        return self.__average