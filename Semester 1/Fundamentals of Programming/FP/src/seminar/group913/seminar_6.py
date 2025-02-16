"""
Write an application that manages a number of cities
Each city has a unique name (string), a county (string) and a population (integer).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a city
        - adds the city with the given id, county and population to the list.
        - error if giving the existing name, the name, county are empty or population is negative

    2. Delete a city
        - deletes the city with the given name from the list
        - error if non-existing name is provided

    3. Show all cities
        - shows all cities in descending order of their population

    4. Show cities whose population is > than given one, ordered in descending order of population

    5. exit
        - exit the program

    Observations:
        - Add 10 random cities at program startup
        - Create a list-based and a dict-based representation of the City entity
        - Write specifications for non-UI functions
        - Write tests for the non-trivial, non-UI functions
        - Use TypeError and ValueError to handle input and program errors
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the city's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""
from random import choice, randint

"""
    City representation functions are below 
"""


def create_city(city_name: str, city_county: str, population: int):
    """
    Function to create a city
    :param city_name: City name, must be at least 3 characters in length
    :param city_county: The county in which the city is in
    :param population: Population should be at least 1_000
    :return: The City entity
    """
    if len(city_name) < 3:
        raise ValueError("City name must have at least 3 characters")
    if population < 1_000:
        raise ValueError("City population must be at least 1_000")
    # return {"name": city_name, "county": city_county, "population": population}
    return [city_name, city_county, population]


def get_city_name(city) -> str:
    """
    Return the city's name
    :param city: The city
    :return:
    """
    # return city["name"]
    return city[0]


def get_city_county(city) -> str:
    # return city["county"]
    return city[1]


def get_city_population(city) -> str:
    # return city["population"]
    return city[2]


def to_str(city) -> str:
    return get_city_name(city) + " is in county " + get_city_county(city) + " with population " + str(
        get_city_population(
            city))


"""
    Test function should not take any parameters and should not return anything. The reason is that test functions
    should be runnable in any order and should not depend on anything external
    
    How a test function should behave:
        - if everything is ok, it should be silent
        - if something is wrong, they should raise an AssertionError (use the assert keyword)
"""


def test_city():
    city = create_city("Simeria", "Hunedoara", 12_000)
    assert get_city_name(city) == "Simeria"  # was the city's name set correctly?
    assert get_city_county(city) == "Hunedoara"
    assert get_city_population(city) == 12_000
    """
    How does the assert keyword work?
        assert <condition>
        
        if <condition> is True, nothing happens
        if <condition> is False, get an AssertionError
    """

    try:
        city = create_city("X", "Hunedoara", 12_000)
        assert False  # if execution reaches this point, there was no ValueError raised in the function!!
    except ValueError:
        assert True  # The point is to show whoever is reading the code that this is expected


test_city()

"""
What happens in case the city name < 3 characters?
    1. The ValueError in the first if statement is raised
    2. The function create_city(...), currently on top of the call stack exits :(
    3. The assignment city_x = create_city(...) does not take place!
    4. There is no try ... except block that catches a ValueError, so the program exists with an error 
"""
# city_x = create_city("Si", "Hunedoara", 12_000)
# print(city_x)

# try:
#     city_x = create_city("Simeria", "Hunedoara", 12_000)
#     print(city_x)
# except ValueError as ve:  # the "as" keyword creates an alias of the ValueError under the name of ve
#     print(ve)

"""
    Program functionalities (non-UI) are below
"""


def generate_cities(n: int) -> list:
    counties = ["Alba", "Mures", "Tulcea", "Iasi", "Bistrita-Nasaud", "Cluj"]
    base_name = ["Baia", "Satu", "Poarta", "Salajul"]
    modifier_name = ["Mare", "Mic", "Alb", "Mijlociu"]

    data = []
    while n > 0:
        city_name = choice(base_name) + " " + choice(modifier_name)
        city_county = choice(counties)
        population = randint(1, 500) * 1_000
        data.append(create_city(city_name, city_county, population))
        n -= 1
    return data


def delete_city(cities_list: list, city_name: str) -> None:
    """
    Delete the city with the given name
    :param cities_list: The list of all cities
    :param city_name: The name of the city to delete
    :return: -
    Raises a ValueError if city with given name does not exist
    """
    for city in cities_list:
        if city_name == get_city_name(city):
            cities_list.remove(city)
            return
    raise ValueError("City with the given name does not exist")


"""
    UI code is below
"""


def display_all_cities(cities_list: list) -> None:
    for c in cities_list:
        print(to_str(c))


def delete_city_ui(cities_list: list) -> None:
    city_name = input("What city would you like to delete ")
    delete_city(cities_list, city_name)


def print_menu():
    print("1. Display all cities")
    print("2. Delete a city")
    print("0. Exit")


def start():
    # Here we keep the list of all cities in the program
    cities_list = generate_cities(10)

    while True:
        try:
            print_menu()
            option = input(">")

            if option == "1":
                display_all_cities(cities_list)
            elif option == "2":
                delete_city_ui(cities_list)
            elif option == "0":
                return
            else:
                print("Not a valid menu option")
        except ValueError as ve:
            print(ve)


start()
