"""
Tests of Delivery Product,Validate tracking code and tracking code searcher
"""
import unittest
from uc3m_logistics import OrderManager

class MyTestCase(unittest.TestCase):
    """
    Class for teststing all possible paths of the three trees
    """

    # VALIDATE TRACKING CODE #
    def test_validate_tracking_code_path1(self):
        """
        Valid tracking code Path A-B-D
        """
        OrderManager.validate_order_type(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
    def test_validate_tracking_code_path2(self):
        """
        Invalid tracking code Path A-B-C-D
        """
        OrderManager.validate_order_type(
            "56df104b603f55548cdf5fff4d62c5f277c28295b1e11aa0bfe")
    # TRACKING CODE SEARCHER #
    def test_tracking_code_searcher_path1(self):
        """
        Valid Path A-B-D-F-H-I-J-K-L-N
        """
        return OrderManager.tracking_code_searcher("56df104b603f55548cdf5fff4d62c5f277c28295b1e11aa0bfe")

    # DELIVER PRODUCT #
    def test_deliver_product_path1(self):
        """
        Valid Path A-B-C-E-G-H-G-H-I-J-K
        """
        return OrderManager.deliver_product("56df104b603f55548cdf5fff4d62c5f277c28295b1e11aa0bfe")


if __name__ == '__main__':
    unittest.main()
