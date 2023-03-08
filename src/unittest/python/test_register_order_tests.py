"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    @freeze_time("2023-03-08")
    def test_something( self ):
        """dummy test"""
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        print(my_order_id)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

        # with (open(file_store)



if __name__ == '__main__':
    unittest.main()
