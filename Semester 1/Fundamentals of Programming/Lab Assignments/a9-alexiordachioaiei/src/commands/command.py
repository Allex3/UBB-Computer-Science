
class Command:
    def __init__(self, func, *params):
        self.__func = func
        self.__params = params

    def __call(self):
        # self.__params = tuple(k1, k2, ...)
        # *self.__params = k1, k2, k3 given to a function!
        # print(params) = (1, 2, 3)
        # print(*params) = 1, 2, 3, wow
        self.__func(*self.__params)

    def __call__(self, *args, **kwargs):
        self.__call()

# So operation has the function calls for undo and redo of an operation
# with DIFFERENT parameters, it's important for it to be a data structure
# Because in case of remove, the undo is of the whole student or whatever
# But the redo only takes the id needed to be removed!

class Assign:
    def __init__(self, func, *params):
        self.__func = func
        self.__params = params

    def __call(self):
        # self.__params = tuple(k1, k2, ...)
        # *self.__params = k1, k2, k3 given to a function!
        # print(params) = (1, 2, 3)
        # print(*params) = 1, 2, 3, wow
        has_assignment = self.__func(*self.__params)
        if not has_assignment:
            print("Each student in the group received the assignment.")
        else:
            print (f"Students with IDs {set(has_assignment)} from the group already have this assignment")

    def __call__(self, *args, **kwargs):
        self.__call()

class AddAssignmentWithGrades:
    def __init__(self, assignment_grades: list, add_grade, add_assignment, *params):
        self.__assignment_grades = assignment_grades
        self.__add_grade = add_grade
        self.__add_assignment = add_assignment
        self.__params = params

    def __call(self):
        # We basically remove the student like usual with the command from student services
        # But that command also deletes all that student's grades, so to add them back we need a special Add Student command.
        self.__add_assignment(*self.__params)  # Add the student like normal using the addition from student services
        # But now we also have to restore the grades given by that list to this command, being the undo_command of the remove student one
        # So we use the function add_grade to add back the grades one by one to the grades repo
        # That method is given by the function add_grade
        for grade in self.__assignment_grades:
            self.__add_grade(grade.student_id, grade.assignment_id, grade.grade_value)

    def __call__(self, *args, **kwargs):
        self.__call()

class AddStudentWithGrades:
    def __init__(self, student_grades: list, add_grade, add_student, *params):
        self.__student_grades = student_grades
        self.__add_grade = add_grade
        self.__add_student = add_student
        self.__params = params

    def __call(self):
        # We basically remove the student like usual with the command from student services
        # But that command also deletes all that student's grades, so to add them back we need a special Add Student command.
        self.__add_student(*self.__params) # Add the student like normal using the addition from student services
        #But now we also have to restore the grades given by that list to this command, being the undo_command of the remove student one
        # So we use the function add_grade to add back the grades one by one to the grades repo
        # That method is given by the function add_grade
        for grade in self.__student_grades:
            self.__add_grade(grade.student_id, grade.assignment_id, grade.grade_value)

    def __call__(self, *args, **kwargs):
        self.__call()



class CommandUndoRedo:
    def __init__(self, redo_func: Command | Assign | AddStudentWithGrades | AddAssignmentWithGrades, undo_func: Command | Assign | AddStudentWithGrades | AddAssignmentWithGrades):
        self.redo = redo_func
        self.undo = undo_func