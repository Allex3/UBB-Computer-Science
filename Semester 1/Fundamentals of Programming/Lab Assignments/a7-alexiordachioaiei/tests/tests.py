import json
import pickle

from src.repository.repository import MemoryRepository, TextFileRepository, BinaryRepository, JSONRepository
from src.domain.expense import Expense
from src.services.services import Services

def test_add_expense():
    expense = Expense(1, 100, "o")
    try:
        expense = Expense(45, 999, "d")
        assert False
    except ValueError:
        assert True
    try:
        expense = Expense(-1, 999, "d")
        assert False
    except ValueError:
        assert True

def test_add_memory():
    mem_repo = MemoryRepository(10, "test.txt", "\\test.bin", "test.json", "test.plm")

    assert len(mem_repo) == 10

    mem_repo.add(10, 5, "k")
    exp_test = Expense(10, 5, "k")
    assert mem_repo[-1].day == 10
    assert mem_repo[-1].amount == 5
    assert mem_repo[-1].type == "k"
    assert len(mem_repo) == 11

def test_add_text():
    # Text repo
    text_repo = TextFileRepository("test.txt")
    text_file = open("test.txt", "r")
    old_expenses_text = text_file.readlines()
    text_file.close()

    exp_test = Expense(1, 100, "l")
    text_repo.add(1, 100, "l")
    with open("test.txt", "r") as text:
        lines = text.readlines()
        assert lines[-1].strip("\n") == str(exp_test)
        for i in range(len(old_expenses_text)):
            assert lines[i].strip("\n") == old_expenses_text[i].strip("\n")

def test_add_binary():
    # Binary repo
    binary_repo = BinaryRepository("test.bin")

    bin_file = open("test.bin", "rb")
    old_expenses_bin = pickle.load(bin_file)
    bin_file.close()

    exp_test = Expense(2, 100, "l")
    binary_repo.add(2, 100, "l")

    bin_file = open("test.bin", "rb")
    expenses_bin = pickle.load(bin_file)
    bin_file.close()
    assert old_expenses_bin[-1].day == expenses_bin[-1].day and old_expenses_bin[-1].amount == expenses_bin[
        -1].amount and old_expenses_bin[-1].type == expenses_bin[-1].type
    for i in range(len(old_expenses_bin)):
        assert old_expenses_bin[i].day == expenses_bin[i].day and old_expenses_bin[i].amount == expenses_bin[
            i].amount and old_expenses_bin[i].type == expenses_bin[i].type

def test_add_JSON():
    # JSON Repo
    json_repo = JSONRepository("test.json")

    json_file = open("test.json", "r")
    old_expenses_json = json.load(json_file)["expenses"]
    old_expenses_json_list = [Expense(int(e["day"]), int(e["amount"]), e["type"]) for e in old_expenses_json]
    json_file.close()

    json_repo.add(3, 100, "m")
    json_file = open("test.json", "r")
    expenses_json = json.load(json_file)["expenses"]
    expenses_json_list = [Expense(int(e["day"]), int(e["amount"]), e["type"]) for e in old_expenses_json]
    json_file.close()

    assert expenses_json_list[-1].day == 3 and expenses_json_list[-1].amount == 100 and expenses_json_list[
        -1].type == "m"
    for i in range(len(old_expenses_json_list)):
        assert old_expenses_json_list[i].day == expenses_json_list[i].day and old_expenses_json_list[i].amount == expenses_json_list[i].amount and old_expenses_json_list[i].type == expenses_json_list[i].type

# Since we tested for the add implementation for all types of repositories
# And in the services class, add_expense clearly has one of those adds, so don't test it again
# The other line in add_expense is related to history, so test that, let's say with a memory repo

def test_add_services() -> None:

    # Test the services class
    services = Services("memory", "test.txt", "\\test.bin", "test.json", "TODO")

    # Since we initialized the services right now, we should have a list with 10 Expenses in memory
    assert len(services.repository) == 10
    assert not services.history #history is empty
    old_expenses = []
    for expense in services.repository:
        old_expenses.append(expense)

    services.add_expense(1, 100, "k")
    assert services.repository[-1].day == 1 and services.repository[-1].amount == 100 and services.repository[-1].type == "k"
    for i in range(len(services.history[-1])): # history is equal to old_expenses
        assert services.history[-1][i].day == old_expenses[i].day and services.history[-1][i].amount == old_expenses[i].amount and services.history[-1][i].type == old_expenses[i].type



test_add_expense()
test_add_memory()
test_add_text()
test_add_binary()
test_add_JSON()
test_add_services()


