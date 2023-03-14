"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    @freeze_time("2023-03-08") #1678237200
    def test_CE_V_1(self):
        """Everything is correct"""
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")

        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08") #1678237200
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

    def test_CE_NV_3(self):
        """
        product_id is not an EAN number is not valid, as it is not numeric
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423225",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")

            self.assertEqual(cm.exception.message, "Product Id not valid, not an EAN13 code")

    @freeze_time("2023-03-08") #1678237200
    def test_CE_NV_4(self):
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

    @freeze_time("2023-03-08") #1678237200
    def test_CE_NV_5(self):
        """
        product_id is not an EAN number is not valid, as it is too long
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220150",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Product Id not valid, id too long")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_V_6(self):
        """
        ORDER_TYPE VALID
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_V_7(self):
        """
        ORDER_TYPE VALID
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="PREMIUM",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "85472b176bfa29087aeb991f80385f6c")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_NV_8(self):
        """
        ORDER_TYPE NOT UPPER_CASE
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="premium",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Order type not valid, must be REGULAR or PREMIUM")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_NV_9(self):
        """
        Order_ID not a string
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type=123,
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Type of the order_type is not valid, must be a STRING")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_V_10(self):
        """
        Address Correct
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type= "REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_V_11(self):
        """
        Address has two spaces
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08") #1678233600
    def test_CE_NV_12(self):
        """
        Address valid, contains only one space
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID,SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "f35f1b805782b06cfa6d7808dcc63fde")

    @freeze_time("2023-03-08") #1678233600 C/LISBOA4MADRIDSPAIN
    def test_CE_NV_13(self):
        """
        Address has no spaces
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4,MADRID,SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Address not valid, must have a space")

    @freeze_time("2023-03-08")
    def test_CE_NV_14(self):
        """
        Address type is not valid (not a string)
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address=123456,
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Address not valid, must be a string")

    @freeze_time("2023-03-08")
    def test_CE_NV_15(self):
        """
        Address length is too small
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="MICASA, MADRID",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Address not valid, must be a string")

    @freeze_time("2023-03-08")
    def test_LV_NV_16(self):
        """
        Address length is too small
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid,"
                                                            " Madrid, Madrid, Madrid, Madrid, Madrid Madrid",
                                                    phone_number="654314159",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Address not valid, must have less than 100 characters")

    @freeze_time("2023-03-08")
    def test_CE_V_17(self):
        """
        Valid Phone number
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_NV_18(self):
        """
        Type of phone number is not valid
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="DEATH_STAR",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Phone number not valid, must be numeric")

    @freeze_time("2023-03-08")
    def test_CE_V_19(self):
        """
        Type of phone number is valid (+34 + format)
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="+34654314159",
                                                zip_code="28005")


    @freeze_time("2023-03-08")
    def test_CE_NV_20(self):
        """
        Length of phone number is too small
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="65431415",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Phone number not valid, must be numeric")


    @freeze_time("2023-03-08")
    def test_CE_NV_21(self):
        """
        Phone number too long
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="6942069420",
                                                    zip_code="28005")
            self.assertEqual(cm.exception.message, "Phone number not valid, must have less than 10 characters")

    @freeze_time("2023-03-08")
    def test_VL_V_22(self):
        """
        PHONE_NUMBER EXACT SIZE
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_V_23(self):
        """
        Valid ZIP_CODE
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_NV_24(self):
        """
        ZIP_CODE too low (less than 01000)
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="00999")
            self.assertEqual(cm.exception.message, "ZIP_CODE not valid, must be greater or equal than 01000")

    @freeze_time("2023-03-08")
    def test_CE_NV_25(self):
        """
        ZIP_CODE too high (greater than 52999)
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="53000")
            self.assertEqual(cm.exception.message, "Zip code not valid, must be less than 53000")

    @freeze_time("2023-03-08")
    def test_LV_NV_26(self):
        """
        ZIP_CODE too long
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="280055")
            self.assertEqual(cm.exception.message, "ZIP_CODE not valid, must have less than 6 characters")

    @freeze_time("2023-03-08")
    def test_LV_NV_27(self):
        """
        ZIP_CODE too short
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="0011")
            self.assertEqual(cm.exception.message, "Zip code not valid, must have more than 4 digits")

    @freeze_time("2023-03-08")
    def test_LV_NV_28(self):
        """
        ZIP_CODE NON INTEGER VALUE
        """
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order_id = my_manager.register_order(product_id="8421691423220",
                                                    order_type="REGULAR",
                                                    address="C/LISBOA,4, MADRID, SPAIN",
                                                    phone_number="654314159",
                                                    zip_code="La casa de paco")
            self.assertEqual(cm.exception.message, "Zip code not valid, must be numeric in the range {01000-52999}")

    @freeze_time("2023-03-08")
    def test_CE_V_29(self):
        """
        ZIP_CODE exactly 01000
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "e01521684a7f9535e9fa098a2b86565f")

    @freeze_time("2023-03-08")
    def test_CE_V_30(self):
        """
        ZIP_CODE exactly 52999
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="52999")
        self.assertEqual(my_order_id, "c0319417d34c8557fccb6f91fbb0da17")

    @freeze_time("2023-03-08")
    def test_CE_V_31(self):
        """
        ZIP_CODE exactly 01001
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="01001")
        self.assertEqual(my_order_id, "2a1b18902f4123138915a587163e66f9")

    @freeze_time("2023-03-08")
    def test_CE_V_32(self):
        """
        ZIP_CODE exactly 52998
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="C/LISBOA,4, MADRID, SPAIN",
                                                phone_number="654314159",
                                                zip_code="52998")
        self.assertEqual(my_order_id, "dcc9c110047037fe863f9a949871984b")


    @freeze_time("2023-03-08")
    def test_CE_V_33(self):
        """
        ADDRESS LENGTH MAX - 1
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid,"
                                                        " Madrid, Madrid, Madrid, Madrid, Madrid, Madr",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "682a8cc1839e55baa794fc4e485e66c4")

    @freeze_time("2023-03-08")
    def test_CE_V_34(self):
        """
        ADDRES LENGTH MIN + 1 (21)
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="MICASA, MADRID, ESPAÑ",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "68b0b2f592fcada21987acb8526bf01d")

    @freeze_time("2023-03-08")
    def test_VL_V_35(self):
        """
        ADDRESS LENGTH MAX
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="Calle de la Gran Via de Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, Madrid, ESPA",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "f0930f6ba28b377ace6a0980af15d9ba")


    @freeze_time("2023-03-08")
    def test_VE_V_36(self):
        """
        ADDRESS LENGTH MIN
        """
        my_manager = OrderManager()
        my_order_id = my_manager.register_order(product_id="8421691423220",
                                                order_type="REGULAR",
                                                address="ESTE ES UNA DIRECCION",
                                                phone_number="654314159",
                                                zip_code="28005")
        self.assertEqual(my_order_id, "149965baa3bd537a24a8357d9713304c")



if __name__ == '__main__':
    unittest.main()


#       with (open(file_store, "r", encoding= "UTF-W", newline="")) as file:
#           data_list = json.load(file)
#       found = False
#       for item in data_list:
#           if item["_OrderRequest__order_id"] == "9bdbf4d0c007547a39ee10b4287b7dc1":
#               found = True
#       self.assertTrue(found)
