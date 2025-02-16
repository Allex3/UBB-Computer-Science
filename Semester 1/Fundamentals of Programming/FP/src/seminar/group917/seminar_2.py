"""
After the seminar, you will be able to:
    - write a menu-driven application
    - work with Python lists and dictionaries
    - manage program entities
        - representation
        - manipulation

A program that manages a list of cities
A city is defined by its name (string) and population (integer)
    - See all the cities
    - Add a city from the console
    - Generate random cities
    - Sort the list by population
    - Exit the program
"""

# A city = [name, population]
# A city = {"name" : name, "population" : population}

import random

def createCity(name, population):
    return [name, population]
    #return {"name" : name, "population" : population}

def getCityName(city):
    #return city["name"]
    return city[0]

def getCityPopulation(city):
    #return city["population"]
    return city[1]

def setCityName(city, name):
    city[0] = name

def printCities(listOfCities):
    for i in range(len(listOfCities)):
        #print("City's Name = ", listOfCities[i][0], " | Population = ", listOfCities[i][1])
        print("City's Name = ", getCityName(listOfCities[i]), " | Population = ", getCityPopulation(listOfCities[i]))

def generateNRandomCities(listOfCities, n):
    """
    :param listOfCities:
    :param n:
    :return:
    """
    cityNames = ["Cluj-Napoca", "Vaslui", "Bacau", "Braila", "Iasi", "Constanta", "Bistrita", "Debrecen", "Paris", "Londra", "Brasov", "Caracal"]
    for i in range(n):
        population = random.randint(0, 4000000)
        nameIndex = random.randint(0, len(cityNames) - 1)
        listOfCities.append(createCity(cityNames[nameIndex], population))

def sortingCities(listOfCities):
    for i in range(len(listOfCities)-1):
        for j in range(i+1,len(listOfCities)):
            if getCityPopulation(listOfCities[i]) >= getCityPopulation(listOfCities[j]):
            #if listOfCities[i][1] >= listOfCities[j][1]:
                aux = listOfCities[i]
                listOfCities[i] = listOfCities[j]
                listOfCities[j] = aux

def increment(var):
    var += 1
    return var, var + 1, var + 2

def specificCopyFunction(listOfCities):
    newList = []
    for i in range(len(listOfCities)):
        newList.append(listOfCities)

    return newList

def printMenu():
    print("1. See all cities")
    print("2. Add a city")
    print("3. Generate n random cities")
    print("4. Sort by population")
    print("5. See copies")
    print("0. Exit")

def main():
    listOfCities = []

    var = 2
    increment(var)
    print(var)

    while True:
        printMenu()
        option = input("Choose an option ")
        if option == "0":
            break
        elif option == "1":
            printCities(listOfCities)
        elif option == "2":
            name = input("Name = ")
            population = int(input("Population = "))
            listOfCities.append(createCity(name, population))
        elif option == "3":
            n = int(input("N = "))
            generateNRandomCities(listOfCities, n)
        elif option == "4":
            sortingCities(listOfCities)
        elif option == "5":
            regularCopy = listOfCities.copy()
            specificCopy = specificCopyFunction(listOfCities)

            print(id(listOfCities))
            print(id(regularCopy))
            print(id(specificCopy))

            print("First element ", id(listOfCities[0]))
            print("First element ", id(regularCopy[0]))
            print("First element ", id(specificCopy[0]))


main()


