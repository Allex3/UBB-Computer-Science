"""
Write an application that manages a group of students.
Each student has a unique id (string), a name (string) and a grade (integer).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a student
        - adds the student with the given id, name and grade to the list.
        - error if giving existing id, the name or grade fields not given or
        empty

    2. Delete a student
        - deletes the student with the given id from the list
        - error if non-existing id given

    3. Show all students
        - shows all students in descending order of their grade

    4. Show students whose grade is > than given one, ordered in descending order of grade

    5. exit
        - exit the program

    Observations:
        - Add 10 random students at program startup
        - Create a list-based and a dict-based representation of the Student entity
        - Write specifications for non-UI functions
        - Write tests for the non-trivial, non-UI functions
        - Use TypeError and ValueError to handle input and program errors
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the student's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""

from random import randint

"""
    Student representation functions are below 
"""

# Student = {"id": id_value, "name": name_value, "grade": grade_value}
# Student = [id, name, grade]

def createStudent(id: str, name: str, grade: int):
    if id == "":
        raise ValueError("Student Id should not be empty")
    elif name == "":
        raise ValueError("Student Name should not be empty")
    elif grade < 1 or grade > 10:
        raise ValueError("Grade is not in [1, 10] interval")

    return {"id": id, "name": name, "grade": grade}

def getStudentId(student) -> str:
    #return student[0]
    return student["id"]

def getStudentName(student) -> str:
    return student["name"]

def getStudentGrade(student) -> int:
    return student["grade"]

def to_str(student):
    return "Student: Id = " + getStudentId(student) + ", Name = " + getStudentName(student) + ", Grade = " + str(getStudentGrade(student))

"""
    Program functionalities (non-UI) are below
"""

def checkId(students: list, id: str):
    """
    Fucntion that checks if the given id has already been used.
    :param students: the list of students
    :param id: the given id
    :return: True if the given id has been used, False otherwise
    """

    hasIdBeenUsed = False
    for i in range(len(students)):
        if getStudentId(students[i]) == id:
            hasIdBeenUsed = True
            break

    return hasIdBeenUsed

def generateStudents(n: int) -> list:
    """
    Generate n students
    :param n: a strictly positive integer, the number of students we need to generate
    :return: a list of length n, of student entities
    """

    result = []
    for i in range(n):
        # we can start from an id equal to 1, and increment it, this way we'll never get the same id
        # our ids will be between 0 and 100000000
        id = str(randint(0, 100000000))

        while checkId(result, id) != False:
            id = str(randint(0, 100000000))

        namesList = ["Andrei", "Tibi","Darius", "Alex", "Tudor", "Eduard", "Vancea", "Somesan", "Cristina", "Stelian", "Steliana", "Marcel", "Marcela"]
        nameIndex = randint(0, len(namesList) - 1)
        name = namesList[nameIndex]

        grade = randint(1, 10)

        student = createStudent(id, name, grade)
        result.append(student)

    return result

def addStudent(students: list, id: str, name: str, grade: int) -> list:
    student = createStudent(id, name, grade)
    students.append(student)

    return students

def removeStudentById(students: list, id: str):
    indexToBeRemoved = 0
    for i in range(len(students)):
        if getStudentId(students[i]) == id:
            indexToBeRemoved = i
            break

    students.pop(indexToBeRemoved)

    return students

def sortStudentsDescendingByGrade(students: list):
    for i in range(len(students) - 1):
        for j in range(i, len(students)):
            if getStudentGrade(students[i]) < getStudentGrade(students[j]):
                students[i], students[j] = students[j], students[i]

    return students

def filterStudentsByGrade(students: list, grade: int) -> list:
    """
    Function that filters the students list by grade
    :param students: the list of students
    :param grade: an integer from [1, 10], the minimum grade
    :return: a list containing students who have grades at least given grade
    """
    filteredList = []
    for i in range(len(students)):
        if getStudentGrade(students[i]) >= grade:
            filteredList.append(students[i])

    return filteredList

"""
    UI code is below
"""

def printMenu():
    print("1. Add a new student")
    print("2. Delete a student")
    print("3. Show all students")
    print("4. Show all students in descending order by their grade")
    print("5. Filter and Sort students by their grade")
    print("0. Exit")

def printStudents(students):
    for i in range(len(students)):
        print(to_str(students[i]))

def addNewStudent(students):
    id = input("Student Id = ")
    if checkId(students, id) == True:
        raise ValueError("Id already existing")

    name = input("Student Name = ")
    #try:
    grade = int(input("Student Grade = "))
    addStudent(students, id, name, grade)
    #except:
        #raise TypeError("Cannot convert given value to integer. Please insert an integer. If it's between 1 and 10, it would be amazing :)")

def deleteStudentById(students):
    id = input("Student Id = ")
    if checkId(students, id) == False:
        raise ValueError("Student with given Id does not exist")

    students = removeStudentById(students, id)

def filterAndSortStudents(students: list):
    grade = int(input("Grade = "))

    if grade < 1 or grade > 10:
        raise ValueError("Grade should be in [1, 10] interval")

    filteredList = filterStudentsByGrade(students, grade)
    return sortStudentsDescendingByGrade(filteredList)


def start():
    students = generateStudents(10)
    while True:
        printMenu()

        choice = input("Your choice: ")
        try:
            if choice == "0":
                break
            elif choice == "1":
                addNewStudent(students)
            elif choice == "2":
                deleteStudentById(students)
            elif choice == "3":
                printStudents(students)
            elif choice == "4":
                printStudents(sortStudentsDescendingByGrade(students))
            elif choice == "5":
                printStudents(filterAndSortStudents(students))
        except (ValueError, TypeError) as error:
            print(error)

"""
Testing functions need to have a separate/new block
"""
def testAddOperation():
    students = []
    id = "1"
    name = "Student1"
    grade = 7
    addStudent(students, id, name, grade)

    assert len(students) == 1
    assert getStudentGrade(students[0]) == grade
    assert getStudentName(students[0]) == name
    assert getStudentId(students[0]) == id

testAddOperation()
start()