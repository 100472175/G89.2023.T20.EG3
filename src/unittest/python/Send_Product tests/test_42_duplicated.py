"""
Test 42 duplicated
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager,OrderShipping
from freezegun import freeze_time

class TestCase(unittest.TestCase):
    """
    test 42 duplicated class
    """

    @freeze_time("2023-03-08")
    def test_42_duplicated(self):
        """
        Testcase test 42 duplicated
        """
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_42_duplicated.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f",
                                    "example@inf.uc3minf.uc3m.es", "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)


if __name__ == "__main__":
    unittest.main()
