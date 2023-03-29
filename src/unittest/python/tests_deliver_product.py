"""
Tests of Delivery Product,Validate tracking code and tracking code searcher
"""
import os
import unittest
from uc3m_logistics import OrderManager,OrderManagementException
from freezegun import freeze_time

@freeze_time("2023-03-08")
def set_issue_day(my_order,file_path):
    my_order.send_product(file_path)
class ValidateTrackingCode(unittest.TestCase):
    """
    Class for testing all possible paths of function validate tracking code
    """

    # VALIDATE TRACKING CODE #
    def test_validate_tracking_code_path1(self):
        """
        Valid tracking code Path A-B
        """
        my_order = OrderManager()
        my_order.validate_tracking_code(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
    @freeze_time("2025-03-20")
    def test_validate_tracking_code_path2(self):
        """
        Invalid tracking code Path A-B-C
        """
        my_order = OrderManager()
        my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                "654314159", "28005")
        current_path = os.path.dirname(__file__)
        file_path = os.path.join(current_path, "aux_jsons", "test_deliver_product_path1.json")
        set_issue_day(my_order,file_path)
        with self.assertRaises(OrderManagementException) as hey:
            my_order.validate_tracking_code(
                "56df104b603f55548cdf5fff4bfe")
        self.assertEqual(hey.exception.message, "Internal processing error")

class TrackingCodeSearcher(unittest.TestCase):
    """
    Class for testing all possible paths of function tracking_code_searcher
    """
    def test_tracking_code_searcher_path1(self):
        """
        Valid Path A-B-C-E-G-H-G-H-I-J-K
        """
        my_order = OrderManager()
        my_order.order_shipping_json_store = "aux_jsons/order_shipping.json"
        with self.assertRaises(OrderManagementException) as hey:
            my_order.tracking_code_searcher(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message, "File not found")
    def test_tracking_code_searcher_path2(self):
        """
        Valid Path A-B-C-D
        """
        my_order = OrderManager()
        current_path = os.path.dirname(__file__)
        file_path = os.path.join(current_path, "aux_jsons", "test_deliver_product_path1.json")
        my_order.order_shipping_json_store = file_path
        with self.assertRaises(OrderManagementException) as hey:
            my_order.tracking_code_searcher(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message, "JSON has not the expected structure")
class DeliverProduct(unittest.TestCase):
    """
    Class for testing all possible paths of function deliver_product
    """
    def test_deliver_product_path1(self):
        """
        Valid Path A-B-C-E-G-H-G-H-I-J-K
        """
        return OrderManager.deliver_product(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")


if __name__ == '__main__':
    unittest.main()
