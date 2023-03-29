"""
Tests of Delivery Product,Validate tracking code and tracking code searcher
"""
import os
import unittest
from uc3m_logistics import OrderManager,OrderManagementException
from freezegun import freeze_time


class ValidateTrackingCode(unittest.TestCase):
    """
    Class for testing all possible paths of function validate tracking code
    """
    @freeze_time("2023-03-08")
    def setUp(self) -> None:

        self.my_order = OrderManager()
        self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")

        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_validate_tracking_code.json")
        self.my_order.send_product(self.file_path)

    def tearDown(self) -> None:
        """Reset the json store"""
        store_path = "../../main/python/stores"
        current_path = os.path.dirname(__file__)
        self.__order_request_json_store = os.path.join(current_path, store_path,
                                                       "order_request.json")
        self.__order_shipping_json_store = os.path.join(current_path, store_path,
                                                       "order_shipping.json")
        with open(self.__order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(self.__order_shipping_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
    # VALIDATE TRACKING CODE #
    def test_validate_tracking_code_path1(self):
        """
        Valid tracking code Path A-B
        """
        self.my_order.validate_tracking_code(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
    @freeze_time("2023-03-08")
    def test_validate_tracking_code_path2(self):
        """
        Invalid tracking code Path A-B-C
        """
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.validate_tracking_code(
                "56df104b603f55548cdf5fff4bfe")
        self.assertEqual(hey.exception.message, "Internal processing error")

class TrackingCodeSearcher(unittest.TestCase):
    """
    Class for testing all possible paths of function tracking_code_searcher
    """

    @freeze_time("2023-03-08")
    def setUp(self) -> None:
        self.my_order = OrderManager()
        self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")

        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_deliver_product_path1.json")
        self.my_order.send_product(self.file_path)

    def tearDown(self) -> None:
        """Reset the json store"""
        store_path = "../../main/python/stores"
        current_path = os.path.dirname(__file__)
        self.__order_request_json_store = os.path.join(current_path, store_path,
                                                       "order_request.json")
        self.__order_shipping_json_store = os.path.join(current_path, store_path,
                                                        "order_shipping.json")
        with open(self.__order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(self.__order_shipping_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
################################################################################### CHECK THE TEST1 (ITERATE TWO TIMES)
    @freeze_time("2023-03-08")
    def test_tracking_code_searcher_path1(self):
        """
        Valid tracking code Path A-B-C-E-G-H-G-H-I-J-K
        """
        my_track_code = self.my_order.tracking_code_searcher(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(my_track_code,{'delivery_day': 1678838400.0,
                                        'delivery_email': '100472175@alumnos.uc3m.es',
                                        'issued_at': 1678233600.0,
                                        'order_id': 'e01521684a7f9535e9fa098a2b86565f',
                                        'product_id': '8421691423220',
                                        'tracking_code': '56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe'})
    def test_tracking_code_searcher_path2(self):
        """
        Invalid Path A-B-C-D
        """
        self.my_order.order_shipping_json_store = "aux_jsons/order_shipping.json"
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.tracking_code_searcher(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message, "File not found")

    def test_tracking_code_searcher_path3(self):
        """
        Invalid Path A-B-C-E-F
        """
        # self.my_order.order_shipping_json_store = "aux_jsons/test_tracking_code_searcher_path3.json"
        current_path = os.path.dirname(__file__)
        self.my_order.order_shipping_json_store = os.path.join(current_path, "aux_jsons", "test_tracking_code_searcher_path3.json")
        # self.file_path = '/Users/edu/PycharmProjects/MUERTOS_G89.2023.T20.EG3/src/unittest/python/aux_jsons/test_tracking_code_searcher_path3.json'
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.tracking_code_searcher(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message, "JSON has not the expected structure")

    def test_tracking_code_searcher_path4(self):
        """
        Invalid Path A-B-C-E-G-J-K
        """
        my_order = OrderManager()
        my_order.order_shipping_json_store = "aux_jsons/test_tracking_code_searcher_path4.json"

        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.tracking_code_searcher(
                "fabada4b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message,
                         "Tracking code not found in the database of requests")

    def test_tracking_code_searcher_path5(self):
        """
        Invalid Path A-B-C-E-F-G-H-I-J-K
        """
        # self.my_order.order_shipping_json_store = "aux_jsons/test_tracking_code_searcher_path5.json"
        current_path = os.path.dirname(__file__)
        self.my_order.order_shipping_json_store = os.path.join(current_path, "aux_jsons", "test_tracking_code_searcher_path3.json")
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.tracking_code_searcher(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message, "JSON has not the expected structure")


    def test_tracking_code_searcher_path6(self):
        """
        Invalid path A-B-C-E-G-H-G-H-I-J-L
        """
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.tracking_code_searcher(
                "56df104b603f5fac5190b2225a5548cdf5fff4d7775f277c28295b1e11aa0bfe")
        self.assertEqual(hey.exception.message,
                         "Tracking code not found in the database of requests")




class DeliverProduct(unittest.TestCase):
    """
    Class for testing all possible paths of function deliver_product
    """

    @freeze_time("2023-03-08")
    def setUp(self) -> None:
        self.my_order = OrderManager()
        self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")

        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_deliver_product_path1.json")
        self.my_order.send_product(self.file_path)


    @freeze_time("2023-03-15")
    def test_deliver_product_path1(self):
        """
        Valid Path A-B-D
        """
        self.assertTrue(self.my_order.deliver_product(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe"))


    def test_deliver_product_path2(self):
        """
        Valid Path A-B-C
        """
        my_order = OrderManager()
        tracking_code = "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe"
        with self.assertRaises(OrderManagementException) as error:
            my_order.deliver_product(tracking_code)

        self.assertEqual(error.exception.message, "The data has been modified")




if __name__ == '__main__':
    unittest.main()
