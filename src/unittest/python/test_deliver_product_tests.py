"""
Tests of Delivery Product,Validate tracking code and tracking code searcher
"""
import os
import unittest
import json

from uc3m_logistics import OrderManager, OrderManagementException
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
        file_path = os.path.join(current_path, "aux_jsons", "test_validate_tracking_code.json")
        self.my_order.send_product(file_path)

    def tearDown(self) -> None:
        """Reset the json store"""
        store_path = "../../main/python/stores"
        current_path = os.path.dirname(__file__)
        order_request_json_store = os.path.join(current_path, store_path, "order_request.json")
        order_shipping_json_store = os.path.join(current_path, store_path, "order_shipping.json")
        with open(order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(order_shipping_json_store, "w", encoding="utf-8") as file:
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


class HashChecker(unittest.TestCase):
    """
    Class for testing all possible paths of function hash_checker
    """

    @freeze_time("2023-03-08")
    def setUp(self) -> None:
        self.my_order = OrderManager()
        self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")

        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_deliver_product_path1.json")
        self.my_order.send_product(self.file_path)
        self.my_order_shipping = self.my_order.tracking_code_searcher("56df104b603f5fac5190b2225a55"
                                                                      "48cdf5fff4d62c5f277c28295b1e"
                                                                      "11aa0bfe")

    def tearDown(self) -> None:
        """Reset the json store"""
        store_path = "../../main/python/stores"
        current_path = os.path.dirname(__file__)
        order_request_json_store = os.path.join(current_path, store_path, "order_request.json")
        order_shipping_json_store = os.path.join(current_path, store_path, "order_shipping.json")
        with open(order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(order_shipping_json_store, "w", encoding="utf-8") as file:
            file.write("[]")

    @freeze_time("2023-03-08")
    def test_hash_checker_path1(self):
        """
        Valid tracking code Path A-C-E-F-E-F-G-H-J-L-M-N-O
        Iterate twice
        """
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_hash_checker_path1.json")
        self.my_order.send_product(self.file_path)
        my_order_shipping = self.my_order.tracking_code_searcher("45c825c1ebbb0fdae6c62a00b7e19fc5"
                                                                 "c1d7b4c256ddb1793394e1cccf117a8b")
        self.assertTrue(self.my_order.hash_checker(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b", my_order_shipping))

    def test_hash_checker_path2(self):
        """
        Invalid Path A-B
        order_request not found
        """
        self.my_order.order_request_json_store = "aux_jsons/order_request.json"
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.hash_checker(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe",
                self.my_order_shipping)
        self.assertEqual(hey.exception.message, "File not found")

    def test_hash_checker_path3(self):
        """
        Invalid Path A-C-D
        Error loading data
        """
        current_path = os.path.dirname(__file__)
        self.my_order.order_request_json_store = os.path.join(current_path, "aux_jsons",
                                                              "test_hash_checker_path3.json")
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.hash_checker(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe",
                self.my_order_shipping)
        self.assertEqual(hey.exception.message, "JSON has not the expected structure")

    def test_hash_checker_path4(self):
        """
        Invalid Path A-C-E-H-I
        no data in order_request
        """
        current_path = os.path.dirname(__file__)
        self.my_order.order_request_json_store = os.path.join(current_path, "aux_jsons",
                                                              "test_tracking_code_searcher_path4"
                                                              ".json")
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.hash_checker(
                "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe",
                self.my_order_shipping)
        self.assertEqual(hey.exception.message,
                         "Order id not found in the database of requests")

    def test_hash_checker_path5(self):
        """
        Valid Path A-C-E-F-G-H-J-K-M-N-O
        loop once
        """
        my_order_shipping = self.my_order.tracking_code_searcher(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        self.assertTrue(self.my_order.hash_checker(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe", my_order_shipping))

    @freeze_time("2023-03-08")
    def test_hash_checker_path6(self):
        """
        Invalid path A-C-E-F-G-H-I
        """
        # Adding the second order
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")

        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_hash_checker_path6.json")
        self.my_order.send_product(self.file_path)
        data = None
        # Changing the order id of all the entries in the order_request.json
        with open(self.my_order.order_request_json_store, "r", encoding="UTF-8") as file:
            data = json.load(file)
            for i in data:
                i["order_id"] = "fabadafabadafabadafabadafabada69"
        with open(self.my_order.order_request_json_store, "w", encoding="UTF-8") as file2:
            json.dump(data, file2, indent=4)

        # Searching for the tracking code
        my_order_shipping = self.my_order.tracking_code_searcher(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe")
        # Found the tracking code, the hash is not valid
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.hash_checker("56df104b603f5fac5190b2225a5548cdf5ff"
                                       "f4d62c5f277c28295b1e11aa0bfe",
                                       my_order_shipping)
        self.assertEqual(hey.exception.message,
                         "Order id not found in the database of requests")

    @freeze_time("2023-03-08")
    def test_hash_checker_path7(self):
        """
        Valid path A-C-E-F-E-F-G-H-J-K-M-N-O
        Iterate twice but  Days = 7
        """
        self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                     "698765119", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_hash_checker_path5.json")
        self.my_order.send_product(self.file_path)
        my_order_shipping = self.my_order.tracking_code_searcher(
            "76866c4e46c8e46cfc5707988823c835f79e5709fc0082aa48119920a824b4b8")
        my_track_code = self.my_order.hash_checker(
            "76866c4e46c8e46cfc5707988823c835f79e5709fc0082aa48119920a824b4b8", my_order_shipping)
        self.assertTrue(my_track_code)

    @freeze_time("2023-03-08")
    def test_hash_checker_path8(self):
        """
        Valid path A-C-E-F-E-F-G-H-J-L-M-N-P
        Data has been modified
        """
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_hash_checker_path8.json")
        self.my_order.send_product(self.file_path)
        my_order_shipping = self.my_order.tracking_code_searcher(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b")
        with self.assertRaises(OrderManagementException) as hey:
            self.my_order.hash_checker("fabada4b603f5fac5190b2225a5548cdf5"
                                       "fff4d62c5f277c28295b1e11aa0bfe",
                                       my_order_shipping)
        self.assertEqual(hey.exception.message,
                         "The data has been modified")

    @freeze_time("2023-03-08")
    def test_hash_checker_path9(self):  # Max - 1 -> Max = 10
        """
        Valid path A-C-E-F-E-F-E-F-E-F-E-F-E-F-E-F-E-F-E-F-G-H-J-L-M-N-P
        """
        # 7 equal orders + the one in setup + the one we want
        for _ in range(7):
            self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                         "654314159", "28005")
            self.my_order.send_product(self.file_path)
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_hash_checker_path8.json")
        self.my_order.send_product(self.file_path)
        my_order_shipping = self.my_order.tracking_code_searcher(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b")
        my_track_code = self.my_order.hash_checker(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b", my_order_shipping)
        self.assertTrue(my_track_code)

    @freeze_time("2023-03-08")
    def test_hash_checker_path10(self):  # Max -> Max = 10
        """
        Valid path A-C-E-F-E-F-E-F-E-F-E-F-E-F-E-F-E-F-E-F-E-F-G-H-J-L-M-N-P
        """
        # 7 equal orders + the one in setup + the one we want
        for _ in range(8):
            self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                         "654314159", "28005")
            self.my_order.send_product(self.file_path)
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons", "test_hash_checker_path8.json")
        self.my_order.send_product(self.file_path)
        my_order_shipping = self.my_order.tracking_code_searcher(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b")
        my_track_code = self.my_order.hash_checker(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b", my_order_shipping)
        self.assertTrue(my_track_code)

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
        order_request_json_store = os.path.join(current_path, store_path,
                                                "order_request.json")
        order_shipping_json_store = os.path.join(current_path, store_path,
                                                 "order_shipping.json")
        with open(order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(order_shipping_json_store, "w", encoding="utf-8") as file:
            file.write("[]")

    @freeze_time("2023-03-08")
    def test_tracking_code_searcher_path1(self):
        """
        Valid tracking code Path A-B-C-E-G-H-G-H-I-J-K
        """
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons",
                                      "test_tracking_code_searcher_path1.json")
        self.my_order.send_product(self.file_path)
        my_track_code = self.my_order.tracking_code_searcher(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b")
        self.assertEqual(my_track_code, {"product_id": "8421691423220",
                                         "order_id": "85472b176bfa29087aeb991f80385f6c",
                                         "delivery_email": "example@alumnos.uc3m.es",
                                         "issued_at": 1678233600.0,
                                         "delivery_day": 1678320000.0,
                                         "tracking_code":
                                             "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4"
                                             "c256ddb1793394e1cccf117a8b"
                                         })

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
        current_path = os.path.dirname(__file__)
        self.my_order.order_shipping_json_store = os.path.join(current_path, "aux_jsons",
                                                               "test_tracking_code_searcher_path3"
                                                               ".json")
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
        current_path = os.path.dirname(__file__)
        self.my_order.order_shipping_json_store = os.path.join(current_path, "aux_jsons",
                                                               "test_tracking_code_searcher_path3."
                                                               "json")
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


    @freeze_time("2023-03-08")
    def test_tracking_code_searcher_path7(self): # Max - 1 -> Max = 10
        """
        Valid tracking code Path A-B-C-E-G-H-G-H-G-H-G-H-G-H-G-H-G-H-G-H-G-H-I-J-K
        """
        for _ in range(7):
            self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                         "654314159", "28005")
            self.my_order.send_product(self.file_path)
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons",
                                      "test_tracking_code_searcher_path1.json")
        self.my_order.send_product(self.file_path)
        my_track_code = self.my_order.tracking_code_searcher(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b")
        self.assertEqual(my_track_code, {"product_id": "8421691423220",
                                         "order_id": "85472b176bfa29087aeb991f80385f6c",
                                         "delivery_email": "example@alumnos.uc3m.es",
                                         "issued_at": 1678233600.0,
                                         "delivery_day": 1678320000.0,
                                         "tracking_code":
                                             "45c825c1ebbb0fdae6c62a00b7e19fc"
                                             "5c1d7b4c256ddb1793394e1cccf117a8b"
                                         })
    @freeze_time("2023-03-08")
    def test_tracking_code_searcher_path8(self): # Max -> Max = 10
        """
        Valid tracking code Path A-B-C-E-G-H-G-H-G-H-G-H-G-H-G-H-G-H-G-H-G-H-I-J-K
        """
        for _ in range(8):
            self.my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                         "654314159", "28005")
            self.my_order.send_product(self.file_path)
        self.my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN",
                                     "654314159", "28005")
        current_path = os.path.dirname(__file__)
        self.file_path = os.path.join(current_path, "aux_jsons",
                                      "test_tracking_code_searcher_path1.json")
        self.my_order.send_product(self.file_path)
        my_track_code = self.my_order.tracking_code_searcher(
            "45c825c1ebbb0fdae6c62a00b7e19fc5c1d7b4c256ddb1793394e1cccf117a8b")
        self.assertEqual(my_track_code, {"product_id": "8421691423220",
                                         "order_id": "85472b176bfa29087aeb991f80385f6c",
                                         "delivery_email": "example@alumnos.uc3m.es",
                                         "issued_at": 1678233600.0,
                                         "delivery_day": 1678320000.0,
                                         "tracking_code":
                                             "45c825c1ebbb0fdae6c62a00b7e19fc"
                                             "5c1d7b4c256ddb1793394e1cccf117a8b"
                                         })


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

    def tearDown(self) -> None:
        """Reset the json store"""
        store_path = "../../main/python/stores"
        current_path = os.path.dirname(__file__)
        order_request_json_store = os.path.join(current_path, store_path,
                                                "order_request.json")
        order_shipping_json_store = os.path.join(current_path, store_path,
                                                 "order_shipping.json")
        order_delivery_json_store = os.path.join(current_path, store_path,
                                                 "order_delivery.json")
        with open(order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(order_shipping_json_store, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(order_delivery_json_store, "w", encoding="utf-8") as file:
            file.write("[]")

    @freeze_time("2023-03-15")
    def test_deliver_product_path1(self):
        """
        Valid Path A-B-C-E-F
        """

        self.assertTrue(self.my_order.deliver_product(
            "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe"))

    def test_deliver_product_path2(self):
        """
        Invalid Path A-B-C-D
        """
        my_order = OrderManager()
        tracking_code = "56df104b603f5fac5190b2225a5548cdf5fff4d62c5f277c28295b1e11aa0bfe"
        with self.assertRaises(OrderManagementException) as error:
            my_order.deliver_product(tracking_code)

        self.assertEqual(error.exception.message, "The product has not been delivered yet")


if __name__ == '__main__':
    unittest.main()
