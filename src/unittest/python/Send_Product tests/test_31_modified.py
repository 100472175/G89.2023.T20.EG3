"""
Test 31 modified
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time


class TestCase(unittest.TestCase):
    """
    test 31 modified class
    """

    @freeze_time("2023-03-08")
    def test_31_modified(self):
        """
        Testcase test 31 modified
        """
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_31_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

if __name__ == "__main__":
    unittest.main()
