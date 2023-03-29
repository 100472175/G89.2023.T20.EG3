"""
Test 1 valid test
"""
import os
import os.path
import unittest
from uc3m_logistics import OrderManager, OrderShipping, OrderManagementException
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    """
    Tests class
    """

    @freeze_time("2023-03-08")
    def test_14_deleted(self):
        """
        Testcase test 14 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_14_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_23_deleted(self):
        """
        Testcase test 23 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_23_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_41_deleted(self):
        """
        Testcase test 41 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_41_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_12_duplicated(self):
        """
        Testcase test 12 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_12_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_33_modified(self):
        """
        Testcase test 33 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_33_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_08_deleted(self):
        """
        Testcase test 08 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_08_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_16_duplicated(self):
        """
        Testcase test 16 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_16_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_26_modified(self):
        """
        Testcase test 26 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_26_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_28_duplicated(self):
        """
        Testcase test 28 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_28_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_46_modified(self):
        """
        Code for checking testcase
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_46_modified.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f",
                                    "e@inf.uc3m.es", "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)

    @freeze_time("2023-03-08")
    def test_11_duplicated(self):
        """
        Testcase test 11 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_11_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_11_deleted(self):
        """
        Testcase test 11 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_11_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_06_duplicated(self):
        """
        Testcase test 06 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_06_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_44_deleted(self):
        """
        Testcase test 44 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_44_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_02_duplicated(self):
        """
        Testcase test 02 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_02_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_15_duplicated(self):
        """
        Testcase test 15 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_15_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_08_duplicated(self):
        """
        Testcase test 08 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_08_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_07_modified(self):
        """
        Testcase test 07 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_07_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_21_deleted(self):
        """
        Testcase test 21 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_21_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_16_deleted(self):
        """
        Testcase test 16 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_16_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_43_deleted(self):
        """
        Testcase test 43 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_43_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_22_duplicated(self):
        """
        Testcase test 22 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_22_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_35_modified(self):
        """
        Testcase test 35 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_35_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_45_modified(self):
        """
        Testcase test 45 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_45_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_41_duplicated(self):
        """
        Testcase test 41 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_41_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_50_modified(self):
        """
        Testcase test 50 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_50_modified.json")

        with self.assertRaises(OrderManagementException) as hey:
            OrderManager().send_product(current_path)
        self.assertEqual(hey.exception.message, "Data in JSON has no valid values")
        # self.assertEqual(exception.exception.message, "noup")

        # self.assertEqual("True", "False")

    @freeze_time("2023-03-08")
    def test_02_deleted(self):
        """
        Testcase test 02 deleted
        """

        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_02_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_42_duplicated(self):
        """
        Testcase test 42 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_42_duplicated.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f",
                                    "example@inf.uc3minf.uc3m.es", "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)

    @freeze_time("2023-03-08")
    def test_39_modified(self):
        """
        Testcase test 39 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_39_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_49_modified(self):
        """
        Testcase test 49 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_49_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_29_deleted(self):
        """
        Testcase test 29 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_29_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_25_duplicated(self):
        """
        Testcase test 25 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_25_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_21_duplicated(self):
        """
        Testcase test 21 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_21_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_30_modified(self):
        """
        Testcase test 30 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_30_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_18_duplicated(self):
        """
        Testcase test 18 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_18_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_13_deleted(self):
        """
        Testcase test 13 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_13_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_24_deleted(self):
        """
        Testcase test 24 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_24_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_05_modified(self):
        """
        Testcase test 05 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_05_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_47_modified(self):
        """
        Testcase test 47 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_47_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_37_modified(self):
        """
        Testcase test 37 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_37_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_43_duplicated(self):
        """
        Testcase test 43 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_43_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_19_modified(self):
        """
        Testcase test 19 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_19_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_27_deleted(self):
        """
        Testcase test 27 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_27_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_10_deleted(self):
        """
        Testcase test 10 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_10_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_20_duplicated(self):
        """
        Testcase test 20 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_20_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_24_duplicated(self):
        """
        Testcase test 24 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_24_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_46_modifiednv(self):
        """
        Testcase test 46 modifiedNV
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_46_modifiedNV.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_15_deleted(self):
        """
        Testcase test 15 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_15_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_22_deleted(self):
        """
        Testcase test 22 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_22_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_23_duplicated(self):
        """
        Testcase test 23 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_23_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_09_modified(self):
        """
        Testcase test 09 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_09_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_40_deleted(self):
        """
        Testcase test 40 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_40_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_27_duplicated(self):
        """
        Testcase test 27 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_27_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_18_deleted(self):
        """
        Testcase test 18 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_18_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_44_duplicated(self):
        """
        Testcase test 44 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_44_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_01_valid(self):
        """
        Function 1
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_01_valid.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f",
                                    "example@inf.uc3m.es", "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)

    @freeze_time("2023-03-08")
    def test_04_deleted(self):
        """
        Testcase test 04 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_04_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_32_modified(self):
        """
        Testcase test 32 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_32_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_40_duplicated(self):
        """
        Code for checking testcase
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_40_duplicated.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f",
                                    "exampleexample@inf.uc3minf.uc3m.es", "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)

    @freeze_time("2023-03-08")
    def test_31_modified(self):
        """
        Testcase test 31 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_31_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_03_deleted(self):
        """
        Testcase test 03 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_03_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_28_deleted(self):
        """
        Testcase test 28 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_28_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_48_modified(self):
        """
        Code for function
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_48_modified.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f",
                                    "example@grade.es", "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)

    @freeze_time("2023-03-08")
    def test_14_duplicated(self):
        """
        Testcase test 14 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_14_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_03_duplicated(self):
        """
        Testcase test 03 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_03_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_38_modified(self):
        """
        Testcase test 38 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_38_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_12_deleted(self):
        """
        Testcase test 12 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_12_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_25_deleted(self):
        """
        Testcase test 25 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_25_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_10_duplicated(self):
        """
        Testcase test 10 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_10_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_29_duplicated(self):
        """
        Testcase test 29 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_29_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_17_duplicated(self):
        """
        Testcase test 17 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_17_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_13_duplicated(self):
        """
        Testcase test 13 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_13_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_04_duplicated(self):
        """
        Testcase test 04 duplicated
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_04_duplicated.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_20_deleted(self):
        """
        Testcase test 20 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_20_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_17_deleted(self):
        """
        Testcase test 17 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_17_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_48_modifiednv(self):
        """
        Testcase test 48 modifiedNV
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_48_modifiedNV.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_42_deleted(self):
        """
        Testcase test 42 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_42_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")

    @freeze_time("2023-03-08")
    def test_06_deleted(self):
        """
        Testcase test 06 deleted
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_06_deleted.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Input file has not Json format")

    @freeze_time("2023-03-08")
    def test_34_modified(self):
        """
        Testcase test 34 modified
        """
        current_path = os.path.dirname(__file__)

        json_path = "aux_jsons"
        current_path = os.path.join(current_path, json_path, "test_34_modified.json")

        with self.assertRaises(OrderManagementException) as exception:
            OrderManager().send_product(current_path)
        self.assertEqual(exception.exception.message, "Data in JSON has no valid values")


if __name__ == '__main__':
    unittest.main()
