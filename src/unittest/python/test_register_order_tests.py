"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    @freeze_time("2023-03-08")
    def test_CE_V_1(self):
        """Everything is correct"""
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")


        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_NV_2(self):
        """
        product_id is not an EAN number is not valid, as it is not numeric
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="842169142322A",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")

            self.assertEqual(cm.exception.message, "Product Id not valid, id must be numeric")

    @freeze_time("2023-03-08")
    def test_CE_NV_3(self):
        """
        product_id is not an EAN number is not valid, as it is too short
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Product Id not valid, id too short")

    @freeze_time("2023-03-08")
    def test_CE_NV_4(self):
        """
        product_id is not an EAN number is not valid, as it is too short
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220150",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Product Id not valid, id too long")



if __name__ == '__main__':
    unittest.main()


#       with (open(file_store, "r", encoding= "UTF-W", newline="")) as file:
#           data_list = json.load(file)
#       found = False
#       for item in data_list:
#           if item["_OrderRequest__order_id"] == "9bdbf4d0c007547a39ee10b4287b7dc1":
#               found = True
#       self.assertTrue(found)
