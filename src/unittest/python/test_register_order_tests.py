"""class for testing the regsiter_order method"""
import hashlib
import os.path
import unittest
import json
from uc3m_logistics import OrderManager, OrderRequest, OrderManagementException
from freezegun import freeze_time
from pathlib import Path
from datetime import datetime

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    date = "2023-03-08" # wee could do this, to parametrize
    __order_request_json_store: str = None

    @classmethod
    def setUpClass(cls) -> None:
        """setup class"""
        store_path = "../../main/python/stores"
        current_path = os.path.dirname(__file__)
        cls.__order_request_json_store = os.path.join(current_path, store_path, "order_request.json")


    def setUp(self) -> None:
        """Reset the json store"""
        with open(self.__order_request_json_store, "w", encoding="utf-8") as file:
            file.write("[]")

        self.__my_manager = OrderManager()
        self._product_id = "8421691423220"
        self._order_type = "REGULAR"
        self._address = "C/LISBOA,4, MADRID, SPAIN"
        self._phone_number = "654314159"
        self._zip_code = "28005"

    ################################
    # PRODUCT ID VALIDATION TESTS #
    ################################

    @freeze_time("2023-03-08")
    def test_EC_V_1(self) -> str:
        """ID: EC_V_1"""

        self._product_id = "8421691423220"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_NV_2(self):
        """
        ID: EC_NV_2
        product_id is not an EAN number is not valid, as it is not numeric
        """
        self._product_id = "842169142322A"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Product Id not valid, id must be numeric")

    def test_EC_NV_3(self):
        """
        ID: EC_NV_3
        product_id is not an EAN number is not valid, as it is not numeric
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order("8421691423225", self._order_type, self._address,
                                                       self._phone_number, self._zip_code)

            self.assertEqual(exception.exception.message, "Product Id not valid, not an EAN13 code")

    @freeze_time("2023-03-08") #1678233600.0
    def test_BV_NV_4(self):
        """
        ID: BV_NV_4
        product_id is not an EAN number is not valid, as it is too short
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order("8421691", self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Product Id not valid, id too short")

    @freeze_time("2023-03-08") #1678233600.0
    def test_BV_NV_5(self):
        """
        ID: BV_NV_5
        product_id is not an EAN number is not valid, as it is too long
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order("8421691423220150", self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Product Id not valid, id too long")
    
    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_NV_42(self):
        """
        ID: EC_NV_42
        product_id is not an EAN number is not valid, as it is too long
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(None, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Exception: Product Id not valid, id must be a string")

    ##################################
    # ORDER_TYPE ID VALIDATION TESTS #
    ##################################
    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_V_6(self):
        """
        ID: EC_V_6
        ORDER_TYPE VALID REGULAR CASE
        """
        self._order_type = "REGULAR"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_V_7(self):
        """
        ID: EC_V_7
        ORDER_TYPE VALID PREMIUM CASE
        """

        self._order_type = "PREMIUM"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

        my_order_id =self.__my_manager.register_order(self._product_id, "PREMIUM", self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "85472b176bfa29087aeb991f80385f6c")

    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_NV_8(self):
        """
        ID: EC_NV_8
        ORDER_TYPE NOT UPPER_CASE
        """
        self._order_type = "premium"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Order type not valid, must be REGULAR or PREMIUM")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_EC_NV_43(self):
        """
        ID: EC_NV_8
        ORDER_TYPE NOT UPPER_CASE
        """
        self._order_type = "regular"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Order type not valid, must be REGULAR or PREMIUM")

    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_NV_9(self):
        """
        ID: EC_NV_9
        Order_TYPE not a string
        """
        self._order_type = None

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Type of the order_type is not valid, must be a STRING")

    ###############################
    # ADDRESS ID VALIDATION TESTS #
    ###############################

    @freeze_time("2023-03-08") #1678233600.0
    def test_EC_V_10(self):
        """
        ID: EC_V_10
        Address Correct
        """

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08") #1678233600.0
    def test_BV_V_11(self):
        """
        ID: BV_V_11
        Address has two spaces
        """

        self._address = "C/LISBOA,4, MADRID, SPAIN"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08") #1678233600
    def test_EC_V_12(self):
        """
        ID: BV_V_12
        Address valid, contains only one space
        """
        self._address = "C/LISBOA,4, MADRID,SPAIN"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08") #1678233600.0 C/LISBOA4MADRIDSPAIN
    def test_BV_NV_13(self):
        """
        ID: BV_NV_13
        Address has no spaces
        """
        self._address = "C/LISBOA,4,MADRID,SPAIN"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must have a space")

    @freeze_time("2023-03-08")
    def test_EC_NV_14(self):
        """
        ID: EC_NV_14
        Address type is not valid (not a string) None
        """
        self._address = None

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must be a string")

    @freeze_time("2023-03-08")
    def test_BV_NV_15(self):
        """
        ID: BV_NV_15
        Address length is too small
        """
        self._address = "MICASA, MADRID"
        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must have more than 20 characters")

    @freeze_time("2023-03-08")
    def test_BV_NV_16(self):
        """
        ID: BV_NV_16
        Address length is too large
        """
        self._address = "Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid," \
                        " Madrid, Madrid, Madrid, Madrid, Madrid Madrid"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                          self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must have less than 100 characters")
            
    @freeze_time("2023-03-08")
    def test_BV_V_33(self):
        """
        ID: BV_V_33
        ADDRESS LENGTH MAX - 1
        """
        self._address = "Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid," \
                        " Madrid, Madr"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_V_34(self):
        """
        ID: BV_V_34
        ADDRES LENGTH MIN + 1 (21)
        """
        self._address = "MICASA, MADRID, ESPAÑ"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_V_35(self):
        """
        ID: BV_V_35
        ADDRESS LENGTH MAX
        """
        self._address = "Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid, Madrid, Madrid," \
                        " Madrid, Madrid, Madrid, ESPA"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)


    @freeze_time("2023-03-08")
    def test_VE_V_36(self):
        """
        ID: BV_V_36
        ADDRESS LENGTH MIN
        """
        self._address = "ESTE ES UNA DIRECCION"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    ####################################
    # PHONE_NUMBER ID VALIDATION TESTS #
    ####################################

    @freeze_time("2023-03-08")
    def test_EC_V_17(self):
        """
        ID: EC_V_17
        Valid Phone number
        """
        self._phone_number = "654314159"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_EC_NV_18(self):
        """
        ID: EC_NV_18
        Type of phone number is not valid, phone_number = None
        """
        self._phone_number = None

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Phone number not valid, must be numeric")

    @freeze_time("2023-03-08")
    def test_EC_V_19(self):
        """
        ID: EC_V_19
        Type of phone number is valid (+34 + format)
        """
        self._phone_number = "+34654314159"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_NV_20(self):
        """
        ID: BV_NV_20
        Length of phone number is too small
        """
        self._phone_number = "65431415"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                          self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Phone number not valid, must be numeric")

    @freeze_time("2023-03-08")
    def test_BV_NV_21(self):
        """
        ID: BV_NV_21
        Phone number too long
        """
        self._phone_number = "6942069420"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id =self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                          self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Phone number not valid, must have less than 10 characters")

    @freeze_time("2023-03-08")
    def test_BV_V_22(self):
        """
        ID: BV_V_22
        PHONE_NUMBER EXACT SIZE
        """

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    ################################
    # ZIP_CODE ID VALIDATION TESTS #
    ################################

    @freeze_time("2023-03-08")
    def test_EC_V_23(self):
        """
        ID: EC_V_23
        Valid ZIP_CODE
        """

        self._zip_code = "28005"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_NV_24(self):
        """
        ID: BV_NV_24
        ZIP_CODE too low (less than 01000)
        """
        self._zip_code = "00999"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "ZIP_CODE not valid, must be greater or equal than 01000")

    @freeze_time("2023-03-08")
    def test_BV_NV_25(self):
        """
        ID: BV_NV_25
        ZIP_CODE too high (greater than 52999)
        """
        self._zip_code = "53000"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Zip code not valid, must be less than 53000")

    @freeze_time("2023-03-08")
    def test_BV_NV_26(self):
        """
        ID: BV_NV_26
        ZIP_CODE too long
        """
        self._zip_code = "280055"

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            
            self.assertEqual(exception.exception.message, "ZIP_CODE not valid, must have less than 6 characters")

    @freeze_time("2023-03-08")
    def test_BV_NV_27(self):
        """
        ID: BV_NV_27
        ZIP_CODE too short
        """

        self._zip_code = "0011"
        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            
            self.assertEqual(exception.exception.message, "Zip code not valid, must have more than 4 digits")

    @freeze_time("2023-03-08")
    def test_EC_NV_28(self):
        """
        ID: EC_NV_28
        ZIP_CODE NON INTEGER VALUE, None
        """
        self._zip_code = None
        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Zip code not valid, must be numeric in the range {01000-52999}")

    @freeze_time("2023-03-08")
    def test_BV_V_29(self):
        """
        ID: BV_V_29
        ZIP_CODE exactly 01000
        """
        self._zip_code = "01000"

        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_V_30(self):
        """
        ID: BV_V_30
        ZIP_CODE exactly 52999
        """

        self._zip_code = "52999"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_V_31(self):
        """
        ID: BV_V_31
        ZIP_CODE exactly 01001
        """

        self._zip_code = "01001"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_EC_V_32(self):
        """
        ID: EC_V_32
        ZIP_CODE exactly 52998
        """

        self._zip_code = "52998"
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    @freeze_time("2023-03-08")
    def test_BV_V_42(self):
        """
        ID: BV_V_42
        ZIP_CODE good length
        """
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)

    ##################################
    # FILE STORE ID VALIDATION TESTS #
    ##################################
    """    @freeze_time("2023-03-08")
        def test_VE_V_37(self):
            # Este Path es un problema porq pilla las back slash y sino no pilla el archivo (archivo de prueba porque no se cual hay q abrir)
            JSON_FILES_PATH = str(Path.home()) + "G89.2023.T20.EG3\target\reports"
            file_store = JSON_FILES_PATH + "GE3_2023_coverage.json"
            if os.path.isfile(file_store):
                os.remove(file_store)
           self.__my_manager = OrderManager()
            my_order_id =self.__my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")
    #   try:
            with (open(file_store, "r", encoding= "UTF-W", newline="")) as file:
                data_list = json.load(file)
                found = False
                for item in data_list:
                    if item["_OrderRequest__order_id"] == "9bdbf4d0c007547a39ee10b4287b7dc1":
                        found = True
                self.assertTrue(found)
    #   except FileNotFoundError as ex:
    #       raise OrderManagementException("Wromg file or path") from ex
    """

    @freeze_time("2023-03-08")
    def test_EC_NV_37(self):
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            self.assertEqual(len(order_requests), prev_json_items + 1)
            order_requests: dict = order_requests[0]
            self.assertDictEqual(order_requests, {
                "order_id": my_order_id,
                "product_id": self._product_id,
                "order_type": self._order_type,
                "delivery_address": self._address,
                "phone_number": self._phone_number,
                "zip_code": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })
        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, order_id_check.order_id)


    def iterate_json(self, json_file):
        # for json that has a wrong format
        with open(json_file, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            for item in order_requests:
                print(item)



if __name__ == '__main__':
    unittest.main()