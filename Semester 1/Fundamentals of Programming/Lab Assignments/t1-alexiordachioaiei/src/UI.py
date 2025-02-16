# User interface section
#
from venv import create

from operations import *

def main() -> None:
    print("Choose what to do in the warehouse.")
    print("add <product_name> <quantity> <item_price> -> Add a product to the warehouse")
    print("remove <product_name> -> removes a product from the warehouse")
    print("list all -> prints all products in the warehouse")
    print("list total -> prints the total value of the products in the Warehouse\n")

    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]), create_product(["Pizza", 15, 8])]

    while (True):
        command = input("> ")
        if command.strip().lower().split(" ")[0] == "remove":
            command = command.strip().split(" ")
            command[0] = command[0].lower()
        else:
            command = command.strip().lower().split(" ")
        if not (command[0] in ["add", "remove", "list"]):
            print("The command is invalid.")
            continue

        match command[0]:
            case "add":
                add(warehouse, command[1:])
            case "remove":
                if not remove(warehouse, command[1]):
                    print("The product by that name does not exist.")
            case "list":
                if command[1] == "all":
                    descending_order = list_all(warehouse)
                    for product in descending_order:
                        print(product)
                if command[1] == "total":
                    total = list_total(warehouse)
                    print(f"The total value of the items in the warehouse is {total}")
