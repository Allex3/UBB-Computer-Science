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
    - Sort the list by population
    - Exit the program
"""

# A city: [name, population]
# A city: {"name": name, "population" : population}

import random

def createCity(name, population):
     return [name, population]
    #return {"name": name, "population" : population}

def getCityName(city):
    #return city["name"]
    return city[0]

def getCityPopulation(city):
    #return city["population"]
    return city[1]

def setCityPopulation(city, population):
    city[1] = population

def printCities(listOfCities):
    for i in range(len(listOfCities)):
        print("City's Name = ", getCityName(listOfCities[i]), " | Population = ", getCityPopulation(listOfCities[i]))

def generateNRandomCities(n, listOfCities):
    cityNames = ["Cluj-Napoca", "Oradea", "Sibiu", "Alba Iulia", "Zalau", "Suceava", "Valencia", "Constanta", "Iasi", "Timisoara", "Bistrita"]
    for i in range(n):
        population = random.randint(0, 5000000)
        nameIndex = random.randint(0, len(cityNames) - 1)
        listOfCities.append(createCity(cityNames[nameIndex], population))

def sortCities(listOfCities):
    """
    Function that sorts the list of cities in ascending order by population
    :param listOfCities: list of values to be sorted by population
    :return: none
    """
    ok = 0
    while(ok == 0):
        ok = 1
        for i in range (0, len(listOfCities) - 1):
            if(getCityPopulation(listOfCities[i]) > getCityPopulation(listOfCities[i+1])):
                '''
                helper = listOfCities[i+1]
                listOfCities[i+1]= listOfCities[i]
                listOfCities[i]= helper
                '''
                listOfCities[i], listOfCities[i + 1] = listOfCities[i + 1], listOfCities[i]
                ok = 0

def increment(var):
    var += 1

def printMenu():
    print("1. See all cities")
    print("2. Add a city")
    print("3. Generate random cities")
    print("4. Sort the list of cities by population")
    print("0. Exit")

def main():
    listOfCities = []

    while True:
        printMenu()
        option = input("Choose an option: ")
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
            generateNRandomCities(n, listOfCities)
        elif option == "4":
            sortCities(listOfCities)

'''
var = 2
increment(var)
print(var)
'''

import copy

listOfNames = ["Cluj-Napoca", "Oradea", "Sibiu", "Alba Iulia", "Zalau", "Suceava", "Valencia", "Constanta", "Iasi",
             "Timisoara", "Bistrita"]
newList = listOfNames.copy()
deepCopyList = copy.deepcopy(listOfNames)

deepCopyList[2] = "Botosani"
newList[2] = "Barcelona"

print(listOfNames)
print(deepCopyList)
print(newList)

print(id(listOfNames))
print(id(newList))
print(id(deepCopyList))

print(type(listOfNames))
print(type(newList))
print(type(deepCopyList))

print(id(listOfNames[0]))
print(id(newList[0]))
print(id(deepCopyList[0]))

#main()

