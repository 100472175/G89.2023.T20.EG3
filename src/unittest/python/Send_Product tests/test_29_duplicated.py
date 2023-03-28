"""
Test 29 duplicated
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time


class TestCase(unittest.TestCase):
    """
    test 29 duplicated class
    """

    @freeze_time("2023-03-08")
    def test_29_duplicated(self):
        """
        Testcase test 29 duplicated
        """
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_29_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

if __name__ == "__main__":
    unittest.main()
