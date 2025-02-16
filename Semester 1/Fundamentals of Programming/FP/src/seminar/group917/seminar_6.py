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

# List-based: Student = [id, name, grade]
# Dict-based: Student = {"id": id_value, "name": name_value
#                        "grade": grade_value}

def createStudent(id: str, name: str, grade: int):
    if id == "":
        raise ValueError("ID should not be empty")
    elif name == "":
        raise ValueError("Name should not be empty")
    elif grade < 1 or grade > 10:
        raise ValueError("Grade should be between 1 and 10")

    #return [id, name, grade]
    return {"id": id, "name": name, "grade": grade}

def getStudentId(student) -> str:
    #return student[0]
    return student["id"]

def getStudentName(student) -> str:
    return student["name"]

def getStudentGrade(student) -> int:
    return student["grade"]

def to_str(student) -> str:
    return "Student: ID = " + getStudentId(student) + ", Name = " + getStudentName(student) + ", Grade = " + str(getStudentGrade(student))

"""
    Program functionalities (non-UI) are below
"""

def isIdUnavailable(students: list, id: str):
    """

    :param students:
    :param id:
    :return: True when the id has been used
             False otherwise
    """
    hasIdBeenUsed = False
    for index in range(len(students)):
        if getStudentId(students[index]) == id:
            hasIdBeenUsed = True
            break

    return hasIdBeenUsed

def generateId(students: list) -> str:
    # ids are values between 1 and 100000000
    id = str(randint(1, 100000000))

    while isIdUnavailable(students, id) != False:
        id = str(randint(1, 100000000))

    return id


def generateStudents(n: int) -> list:
    """
    Function that generates a list of n student entities
    :param n: the length of the required list
    :return: a list containing n student entities
    """
    result = []
    for i in range(n):
       id = generateId(result)

       namesList = ["Diana", "Violeta", "Patricia", "Maia", "Miriam", "Darius", "Matei", "Andreea", "Luca", "Denis", "Victor", "Lupu"]
       namesIndex = randint(0, len(namesList) - 1)
       name = namesList[namesIndex]

       grade = randint(1, 10)

       student = createStudent(id, name, grade)
       result.append(student)

    return result

def addNewStudent(students, id, name, grade):
    if isIdUnavailable(students, id) == True:
        raise ValueError("ID already exists. Please choose something different")

    grade = int(grade)
    student = createStudent(id, name, grade)
    students.append(student)

    return students

def deleteStudentById(students: list, id: str) -> list:
    if isIdUnavailable(students, id) == False:
        raise ValueError("The student with teh requested ID does not exist")

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
    print("2. Delete a student by ID")
    print("3. Show all students")
    print("4. Show all students in descending order by grade")
    print("5. Filter and sort students by grade (descending)")
    print("0. Exit")

def printStudents(students):
    for i in range(len(students)):
        print(to_str(students[i]))

def addStudent(students):
    id = input("ID = ")
    name = input("Name = ")
    grade = input("Grade = ")

    addNewStudent(students, id, name, grade)

def deleteStudent(students):
    id = input("ID = ")
    deleteStudentById(students, id)

def filterAndSortByGrade(students):
    grade = int(input("Grade = "))
    filteredStudents = filterStudentsByGrade(students, grade)
    return sortStudentsDescendingByGrade(filteredStudents)

def start():
    students = generateStudents(10)
    while True:
        printMenu()

        choice = input("Your choice: ")

        try:
            if choice == "0":
                break
            elif choice == "1":
                addStudent(students)
            elif choice == "2":
                deleteStudent(students)
            elif choice == "3":
                printStudents(students)
            elif choice == "4":
                printStudents(sortStudentsDescendingByGrade(students))
            elif choice == "5":
                printStudents(filterAndSortByGrade(students))
        except (ValueError, TypeError) as error:
            print(error)

def testDeleteOperation():
    students = []
    id = "3"
    name = "Student1"
    grade = 7
    students.append(createStudent(id, name, grade))

    id = "4"
    name = "Student2"
    grade = 9
    students.append(createStudent(id, name, grade))

    id = "5"
    name = "Student3"
    grade = 2
    students.append(createStudent(id, name, grade))

    try:
        deleteStudentById(students, "19")
    except:
        pass
    assert len(students) == 3

    try:
        deleteStudentById(students, "4")
    except:
        pass
    assert len(students) == 2
    assert getStudentId(students[1]) == "5"


testDeleteOperation()
start()