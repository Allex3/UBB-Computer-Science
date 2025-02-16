import unittest

from src.repository import TextRepo, MemoryRepo, RepositoryError
from src.services import Services
from src.domain import Order, Driver, OrderError

class Tests(unittest.TestCase):
    def test_add_order(self):
        memo_repo = MemoryRepo()
        try:
            memo_repo.add_driver(1, "Alex")
            memo_repo.add_order(1, 3)
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)

        self.assertRaises(RepositoryError, memo_repo.add_order, 2, 3)
        self.assertRaises(OrderError, memo_repo.add_order, 1, 0)

    def test_add_order_to_file(self):
        text_repo = TextRepo("test_orders.txt", "test_drivers.txt")
        try:
            text_repo.add_driver(1, "Alex")
            text_repo.add_order(1, 3)
            self.assertTrue(True)
        except RepositoryError:
            self.assertTrue(False)

        self.assertRaises(RepositoryError, text_repo.add_order, 2, 3)
        self.assertRaises(OrderError, text_repo.add_order, 1, 0)

        orders = text_repo.get_orders()
        for order in orders:
            if order.driver_id == 1 and order.lineage == 3:
                self.assertTrue(True)
                return

        self.assertTrue(False)





if __name__ == '__main__':
    unittest.main()