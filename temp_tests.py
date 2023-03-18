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

    def test_CE_V_1(self) -> str:
        """ID: CE_V_1"""

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
                "zipcode": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })

        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)

        self.assertEqual(my_order_id, order_id_check)

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_V_1(self):
        """ID: CE_V_1"""
        justnow = datetime.utcnow()
        dictionary = {
            "_OrderRequest__product_id": self._product_id,
            "_OrderRequest__delivery_address": self._address,
            "_OrderRequest__order_type": self._order_type,
            "_OrderRequest__phone_number": self._phone_number,
            "_OrderRequest__zip_code": self._zip_code,
            "_OrderRequest__time_stamp": datetime.timestamp(justnow)
        }
        baseline = "OrderRequest:" + json.dumps(dictionary)
        hashed_baseline = hashlib.md5(baseline.encode(encoding="utf-8")).hexdigest()

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, hashed_baseline)

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_NV_2(self):
        """
        product_id is not an EAN number is not valid, as it is not numeric
        """

        # What we change
        self._product_id = "842169142322A"
        message = ""

        # The test:
        prev_json_items = 0
        with open(self.__order_request_json_store, "r", encoding="utf-8") as file:
            order_requests = json.load(file)
            prev_json_items = len(order_requests)

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, self._zip_code)
        self.assertEqual(exception.exception.message, message)

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
                "zipcode": self._zip_code,
                "time_stamp": datetime.strptime("2023-03-08", "%Y-%m-%d").timestamp()
            })

        order_id_check = OrderRequest(self._product_id, self._order_type, self._address,
                                      self._phone_number, self._zip_code)

        self.assertEqual(my_order_id, order_id_check)
        # ----------

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order("842169142322A", self._order_type, self._address,
                                                           self._phone_number, self._zip_code)

            self.assertEqual(exception.exception.message, "Product Id not valid, id must be numeric")

    def test_CE_NV_3(self):
        """
        product_id is not an EAN number is not valid, as it is not numeric
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order("8421691423225", self._order_type, self._address,
                                                           self._phone_number, self._zip_code)

            self.assertEqual(exception.exception.message, "Product Id not valid, not an EAN13 code")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_NV_4(self):
        """
        product_id is not an EAN number is not valid, as it is too short
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order("8421691", self._order_type, self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Product Id not valid, id too short")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_NV_5(self):
        """
        product_id is not an EAN number is not valid, as it is too long
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order("8421691423220150", self._order_type, self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Product Id not valid, id too long")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_NV_42(self):
        """
        product_id is not an EAN number is not valid, as it is too long
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(None, self._order_type, self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Exception: Product Id not valid, id must be a string")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_V_6(self):
        """
        ORDER_TYPE VALID REGULAR CASE
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_V_7(self):
        """
        ORDER_TYPE VALID PREMIUM CASE
        """

        my_order_id = self.__my_manager.register_order(self._product_id, "PREMIUM", self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "85472b176bfa29087aeb991f80385f6c")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_NV_8(self):
        """
        ORDER_TYPE NOT UPPER_CASE
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, "premium", self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Order type not valid, must be REGULAR or PREMIUM")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_NV_9(self):
        """
        Order_ID not a string
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, 123, self._address,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Type of the order_type is not valid, must be a STRING")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_V_10(self):
        """
        Address Correct
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")  # 1678233600.0
    def test_CE_V_11(self):
        """
        Address has two spaces
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, "C/LISBOA,4, MADRID, SPAIN",
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")  # 1678233600
    def test_CE_NV_12(self):
        """
        Address valid, contains only one space
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, "C/LISBOA,4, MADRID,SPAIN",
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "f35f1b805782b06cfa6d7808dcc63fde")

    @freeze_time("2023-03-08")  # 1678233600.0 C/LISBOA4MADRIDSPAIN
    def test_CE_NV_13(self):
        """
        Address has no spaces
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type,
                                                           "C/LISBOA,4,MADRID,SPAIN",
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must have a space")

    @freeze_time("2023-03-08")
    def test_CE_NV_14(self):
        """
        Address type is not valid (not a string)
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, None,
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must be a string")

    @freeze_time("2023-03-08")
    def test_CE_NV_15(self):
        """
        Address length is too small
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, "MICASA, MADRID",
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must have more than 20 characters")

    @freeze_time("2023-03-08")
    def test_LV_NV_16(self):
        """
        Address length is too large
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type,
                                                           "Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid,"
                                                           " Madrid, Madrid, Madrid, Madrid, Madrid Madrid",
                                                           self._phone_number, self._zip_code)
            self.assertEqual(exception.exception.message, "Address not valid, must have less than 100 characters")

    @freeze_time("2023-03-08")
    def test_CE_V_33(self):
        """
        ADDRESS LENGTH MAX - 1
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type,
                                                       "Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid,"
                                                       " Madrid, Madrid, Madrid, Madrid, Madrid, Madr",
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "682a8cc1839e55baa794fc4e485e66c4")

    @freeze_time("2023-03-08")
    def test_CE_V_34(self):
        """
        ADDRES LENGTH MIN + 1 (21)
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, "MICASA, MADRID, ESPAÑ",
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "68b0b2f592fcada21987acb8526bf01d")

    @freeze_time("2023-03-08")
    def test_VL_V_35(self):
        """
        ADDRESS LENGTH MAX
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type,
                                                       "Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, ESPA",
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "f0930f6ba28b377ace6a0980af15d9ba")

    @freeze_time("2023-03-08")
    def test_VE_V_36(self):
        """
        ADDRESS LENGTH MIN
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, "ESTE ES UNA DIRECCION",
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "149965baa3bd537a24a8357d9713304c")

    @freeze_time("2023-03-08")
    def test_CE_V_17(self):
        """
        Valid Phone number
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_NV_18(self):
        """
        Type of phone number is not valid
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           None, self._zip_code)
            self.assertEqual(exception.exception.message, "Phone number not valid, must be numeric")

    @freeze_time("2023-03-08")
    def test_CE_V_19(self):
        """
        Type of phone number is valid (+34 + format)
        """
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       "+34654314159", self._zip_code)

    @freeze_time("2023-03-08")
    def test_CE_NV_20(self):
        """
        Length of phone number is too small
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           "65431415", self._zip_code)
            self.assertEqual(exception.exception.message, "Phone number not valid, must be numeric")

    @freeze_time("2023-03-08")
    def test_CE_NV_21(self):
        """
        Phone number too long
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           "6942069420", self._zip_code)
            self.assertEqual(exception.exception.message, "Phone number not valid, must have less than 10 characters")

    @freeze_time("2023-03-08")
    def test_VL_V_22(self):
        """
        PHONE_NUMBER EXACT SIZE
        """
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_V_23(self):
        """
        Valid ZIP_CODE
        """

        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, self._zip_code)
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_NV_24(self):
        """
        ZIP_CODE too low (less than 01000)
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, "00999")
            self.assertEqual(exception.exception.message, "ZIP_CODE not valid, must be greater or equal than 01000")

    @freeze_time("2023-03-08")
    def test_CE_NV_25(self):
        """
        ZIP_CODE too high (greater than 52999)
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, "53000")
            self.assertEqual(exception.exception.message, "Zip code not valid, must be less than 53000")

    @freeze_time("2023-03-08")
    def test_LV_NV_26(self):
        """
        ZIP_CODE too long
        """

        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, "280055")

            self.assertEqual(exception.exception.message, "ZIP_CODE not valid, must have less than 6 characters")

    @freeze_time("2023-03-08")
    def test_LV_NV_27(self):
        """
        ZIP_CODE too short
        """
        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, "0011")

            self.assertEqual(exception.exception.message, "Zip code not valid, must have more than 4 digits")

    @freeze_time("2023-03-08")
    def test_LV_NV_28(self):
        """
        ZIP_CODE NON INTEGER VALUE
        """
        with self.assertRaises(OrderManagementException) as exception:
            my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                           self._phone_number, None)
            self.assertEqual(exception.exception.message,
                             "Zip code not valid, must be numeric in the range {01000-52999}")

    @freeze_time("2023-03-08")
    def test_CE_V_29(self):
        """
        ZIP_CODE exactly 01000
        """
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, "01000")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_V_30(self):
        """
        ZIP_CODE exactly 52999
        """
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, "52999")

        self.assertEqual(my_order_id, "c0319417d34c8557fccb6f91fbb0da17")

    @freeze_time("2023-03-08")
    def test_CE_V_31(self):
        """
        ZIP_CODE exactly 01001
        """
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, "01001")

        self.assertEqual(my_order_id, "2a1b18902f4123138915a587163e66f9")

    @freeze_time("2023-03-08")
    def test_CE_V_32(self):
        """
        ZIP_CODE exactly 52998
        """
        my_order_id = self.__my_manager.register_order(self._product_id, self._order_type, self._address,
                                                       self._phone_number, "52998")

        self.assertEqual(my_order_id, "dcc9c110047037fe863f9a949871984b")


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

if __name__ == '__main__':
    unittest.main()