"""
What do we practice today?
    - Write a menu-based program
    - Practice Python list, dict types
    - How to represent program entities? -- list. vs dict
    - How to structure the program

Problem statement
    -- Manage a list of cities. Each city has a name, population and a county
Program requirements
    -- Sort them by any of their features (name, pop or county)
    -- Add a city from the console
    -- Generate some random cities :)
    -- Search for a city, using case-insensitive partial string matching
    -- Exit the program
"""


# --- Functions that deal with how a city is represented

# A city represented using a Python list
# my_city = ["Constanta", 200_000, "Constanta"]

# A dict is a set of key-to-value mappings; keys must be unique, values not necesarely
# A city represented using a Python dict
# my_city = {"name": "Braila", "population": 150_000, "county": "Braila"}


def create_city(name: str, population: int, county: str):
    # list representation
    # return [name, population, county]
    # dict representation
    return {"name": name, "population": population, "county": county}


def get_name(city) -> str:
    # list representation
    # return city[0]
    # dict representation
    return city["name"]


def get_population(city) -> int:
    # return city[1]
    return city["population"]


def get_county(city) -> str:
    # return city[2]
    return city["county"]


def to_str(city) -> str:
    return get_name(city) + " with population of " + str(get_population(city)) + " is in " + get_county(city)


def cmp_by_name(city_one, city_two) -> bool:
    # We use this function to compare city names
    return get_name(city_one) > get_name(city_two)


# --- Functions that implement program requirements
def sort_cities(city_list: list, cmp_function) -> None:
    sort_flag = False
    while sort_flag is False:
        sort_flag = True
        for i in range(0, len(city_list) - 1):
            # if get_name(city_list[i]) > get_name(city_list[i + 1]):
            # NOTE This allows us to implement a small function to create additional search criteria
            if cmp_function(city_list[i], city_list[i + 1]) is True:
                # swap
                city_list[i], city_list[i + 1] = city_list[i + 1], city_list[i]
                sort_flag = False


# --- User interface functions
# NOTE The only place where we are allowed to write print(), input() statements

# my_city = create_city("Braila", 150_000, "Braila")
# print(get_name(my_city), get_population(my_city))
# print(to_str(my_city))

def show_all_cities(city_list: list) -> None:
    print("List of cities")
    for city in city_list:
        print(to_str(city))


def add_city(city_list: list) -> None:
    # TODO Make sure we can't add the same city twice
    print("Add a new city")
    name = input("City name =")

    while True:
        try:
            pop = int(input("City population ="))
            break
        except ValueError:  # ValueError is the type of the error when failing to convert an str to an int
            print("Population must be an integer!")

    county = input("County =")
    city_list.append(create_city(name, pop, county))


def search_for_city(city_list: list) -> None:
    search_term = input("What city to search for =").upper()

    results = []
    for city in city_list:
        if search_term in get_name(city).upper():
            results.append(city)

    # display the cities
    for city in results:
        print(to_str(city))


def start():
    # NOTE We don't use global variables
    cities_list = []  # empty list

    # add a few cities
    cities_list.append(create_city("Roman", 40_000, "Neamt"))
    cities_list.append(create_city("Braila", 150_000, "Braila"))

    while True:
        print("1. Show all cities")
        print("2. Add a city")
        print("3. Search for a city")
        print("4. Sort cities by name")
        print("0. Exit")

        command = input(">")

        if command == "1":
            # NOTE We write functions so that the main loop is not too complicated
            show_all_cities(cities_list)
        elif command == "2":
            add_city(cities_list)
        elif command == "3":
            search_for_city(cities_list)
        elif command == "4":
            sort_cities(cities_list, cmp_by_name)
        elif command == "0":
            # return
            # exit(0)
            break
        else:
            print("Bad command or file name")


# print(locals())
start()
