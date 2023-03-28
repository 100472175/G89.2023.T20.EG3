"""
Test 50 modified
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time


class TestCase(unittest.TestCase):
    """
    test 50 modified class
    """

    @freeze_time("2023-03-08")
    def test_50_modified(self):
        """
        Testcase test 50 modified
        """
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_50_modified.json")

        with self.assertRaises(OrderManagementException) as hey:
            OrderManager().send_product(current_path)
        self.assertEqual(hey.exception.message, "Data in JSON has no valid values")
        # self.assertEqual(exception.exception.message, "noup")

        # self.assertEqual("True", "False")
if __name__ == "__main__":
    unittest.main()
