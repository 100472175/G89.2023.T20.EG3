"""
Test 46 modifiedNV
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time


class TestCase(unittest.TestCase):
    """
    test 46 modifiedNV class
    """

    @freeze_time("2023-03-08")
    def test_46_modifiednv(self):
        """
        Testcase test 46 modifiedNV
        """
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_46_modifiedNV.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

if __name__ == "__main__":
    unittest.main()
