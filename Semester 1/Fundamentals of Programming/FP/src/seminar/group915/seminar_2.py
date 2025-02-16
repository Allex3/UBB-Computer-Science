"""
After the seminar, you will be able to:
    - write a menu-driven application
    - work with Python lists and dictionaries
    - manage program entities
        - representation
        - manipulation

A program that manages a list of cities
A city is defined by its name (string) and population (integer)
    - See all cities
    - Add a city from the console
    - Generate random cities
    - Sort the list by population (in ascending order)
    - Exit the program
"""

"""
A city : {"name": name, "population": population}
A city : [name, population]
"""

import random

def createCity(name, population):
    return {"name": name, "population": population}
    #return [name, population]

def getName(city):
    #return city[0]
    return city["name"]

def getPopulation(city):
    #return city[1]
    return city["population"]

def printCities(listOfCities):
    for i in range(len(listOfCities)):
        #print("City's Name = ", listOfCities[i]["name"], " | Population = ", listOfCities[i]["population"])
        #print("City's Name = ", listOfCities[i][0], " | Population = ", listOfCities[i][1])
        print("City's Name = ", getName(listOfCities[i]), " | Population = ", getPopulation(listOfCities[i]))

def generateNCities(n, listOfCities):
    cities = ["Cluj-Napoca", "Bucuresti", "Iasi", "Zalau", "Constanta", "Bacau", "Baia Mare", "Alba Iulia", "Suceava", "Bistrita", "Timisoara"]
    for i in range(n):
        population = random.randint(0, 5000000)
        nameIndex = random.randint(0, len(cities) - 1)
        name = cities[nameIndex]

        listOfCities.append(createCity(name, population))

def sort_list(cities):
    """
    Function that sorts the list of cities by their population, in ascending order (bouble sort)
    :param cities: the list of cities
    :return: None
    """
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(cities) - 1):
            if cities[i]["population"] > cities[i + 1]["population"]:
                aux = cities[i]
                cities[i] = cities[i + 1]
                cities[i + 1] = aux
                swapped = True
    """

    for i in range(0, len(cities) - 1):
        for j in range(i + 1, len(cities)):
            if getPopulation(cities[i]) > getPopulation(cities[j]):
                """
                aux = cities[i]
                cities[i] = cities[j]
                cities[j] = aux
                """
                cities[i], cities[j] = cities[j], cities[i]

def printMenu():
    print("1. See all cities")
    print("2. Add a city")
    print("3. Generate n random cities")
    print("4. Sort the list of cities by population")
    print("0. Exit the program")

def main():
    listOfCities = []

    while True:
        printMenu()
        option = input("Choose an option ")

        if option == "0":
            break
        elif option == "1":
            printCities(listOfCities)
        elif option == "2":
            name = input("City's name = ")
            population = int(input("City's population = "))

            listOfCities.append(createCity(name, population))
        elif option == "3":
            n = int(input("N = "))
            generateNCities(n, listOfCities)
        elif option == "4":
            sort_list(listOfCities)

def increment(i):
    i += 1

def swapExercies():
    a = 3
    b = 4
    a, b = b, a
    print(a)
    increment(a)
    print(a)
    print(b)

#main()
swapExercies()