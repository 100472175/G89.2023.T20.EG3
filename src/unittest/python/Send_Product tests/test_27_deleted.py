"""
Test 27 deleted
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time


class TestCase(unittest.TestCase):
    """
    test 27 deleted class
    """

    @freeze_time("2023-03-08")
    def test_27_deleted(self):
        """
        Testcase test 27 deleted
        """
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_27_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

if __name__ == "__main__":
    unittest.main()
