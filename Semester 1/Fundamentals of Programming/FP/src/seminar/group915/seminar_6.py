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

def createStudent(id: str, name: str, grade: int) -> list:
    # student = [id, name, grade]
    if id == "":
        raise ValueError("Id should not be empty")
    elif name == "":
        raise ValueError("Name should not be empty")
    elif grade == "":
        raise ValueError("Grade should not be empty")
    elif type(grade) != int:
        raise TypeError("Grade should be an integer")

    return [id, name, grade]

def getStudentId(student):
    return student[0]

def getStudentName(student):
    return student[1]

def getStudentGrade(student):
    return student[2]

def to_str(student):
    id = getStudentId(student)
    name = getStudentName(student)
    grade = getStudentGrade(student)
    return "Student: ID = " + id + " Name = " + name + ", Grade = " + str(grade)

"""
    Program functionalities (non-UI) are below
"""

def isIdPresent(students: list, id: str):
    idIsPresent = False
    for index in range(len(students)):
        if getStudentId(students[index]) == id:
            idIsPresent = True
            break

    return idIsPresent

def generateStudents(n: int) -> list:
    """
    Generate a list of n Student entities
    :param n: a strictly positive integer, the number of Student entities that need to be generated
    :return: a list of length n of Student entities
    """
    result = []
    for i in range(n):
        # idInterval = (0, 100000000)
        id = str(randint(0, 100000000))
        while isIdPresent(result, id) == True:
            id = str(randint(0, 100000000))

        listOfNames = ["Andrei", "Marius", "Cosmin", "Cezar", "Rares", "Carmen", "Adrian", "Mara", "Alesia", "Taisia", "Raluca", "Veronica", "Alexandru"]
        nameIndex = randint(0, len(listOfNames) - 1)
        name = listOfNames[nameIndex]

        grade = randint(1, 10)

        student = createStudent(id, name, grade)
        result.append(student)

    return result


def filterStudentsByGrade(students: list, grade: int) -> list:
    """
    Filters the list of students by grade
    :param students: the list of students
    :param grade: the minimum grade, an integer
    :return: the list of students that have at least the given grade as a grade
    """
    filteredList = []
    for i in range(len(students)):
        if getStudentGrade(students[i]) >= grade:
            filteredList.append(students[i])

    return filteredList

def sortStudentsByGrade(students: list):
    """

    :param students:
    :return:
    """
    for i in range(len(students) - 1):
        for j in range(i + 1, len(students)):
            if getStudentGrade(students[i]) < getStudentGrade(students[j]):
                students[i], students[j] = students[j], students[i]

    return students

"""
    UI code is below
"""

def printMenu():
    print("1. Add a new student")
    print("2. Delete a student")
    print("3. Show all students")
    print("4. Show students with grade larger than x, in descending order")
    print("0. Exit")

def printStudents(students):
    for i in range(len(students)):
       print(to_str(students[i]))

def addNewStudent(students: list):
    id = input("Student Id = ")
    name = input("Student Name = ")
    try:
        grade = int(input("Student Grade = "))
    except ValueError:
        raise TypeError("Grade could not be converted into an integer")

    if isIdPresent(students, id) == True:
        #id = input("Another Student Id = ")
        raise ValueError("Id should be unique")

    student = createStudent(id, name, grade)
    students.append(student)

def deleteStudent(students: list):
    id = input("Student Id = ")

    if isIdPresent(students, id) == False:
        raise ValueError("Student with given Id does not exist")

    indexToBeRemoved = 0
    for i in range(len(students)):
        if getStudentId(students[i]) == id:
            indexToBeRemoved = i
            break

    students.pop(indexToBeRemoved)

def filterAndSortStudents(students: list):
    try:
        grade = int(input("Grade = "))
    except ValueError:
        raise TypeError("Grade could not be converted into an integer")

    filteredList = filterStudentsByGrade(students, grade)
    finalList = sortStudentsByGrade(filteredList)
    printStudents(finalList)

def testFilter():
    students = generateStudents(10)
    grade = 11
    filtered = filterStudentsByGrade(students, grade)
    assert len(filtered) == 0

    grade = 6
    count = 0

    for i in range(len(students)):
        if getStudentGrade(students[i]) >= grade:
            count += 1

    filtered = filterStudentsByGrade(students, grade)
    assert len(filtered) == count


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
                deleteStudent(students)
            elif choice == "3":
                printStudents(students)
            elif choice == "4":
                filterAndSortStudents(students)
        except (ValueError, TypeError) as error:
            print(error)

if __name__ == "__main__":
    testFilter()
    start()
    