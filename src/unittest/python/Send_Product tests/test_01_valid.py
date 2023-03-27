import unittest
import hashlib
import os.path
import unittest
import json
import os
import re
from uc3m_logistics import OrderManager, OrderRequest,OrderShipping, OrderManagementException
from freezegun import freeze_time
from pathlib import Path
from datetime import datetime

class MyTestCase(unittest.TestCase):

    @freeze_time("2023-03-08")
    def test_01_valid(self):
        order = None

        # Path to The Json test
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_01_valid.json")

        # Path to the order_request & order_shipping jsons
        json_store_path = os.path.dirname(__file__)
        json_store_path = current_path[:-34]
        json_path = "main\python\stores"
        json_store_path = os.path.join(json_store_path,json_path,"order_request.json")

        json_order_shipping = os.path.join(os.path.dirname(__file__)[:-34],json_path,"order_shipping.json")

        # input_file = "..\..\..\..\main/JsonFiles\\test_01_valid.json"
        try:
            with open(current_path, "r+", encoding="utf-8") as file:
                data_og_json = json.load(file)
                data_og = str(data_og_json)
                pattern = r"[0-9a-f]{32}"
                match = re.finditer(pattern, data_og)
                for m in match:
                    order = m.group(0)
        except FileNotFoundError:
            raise OrderManagementException("Input File not Found")
        except json.decoder.JSONDecodeError:
            raise OrderManagementException("Input file has not Json format")

        saved = None
        # Check the data has not been modified
        try:
            with open(json_store_path, "r+", encoding="utf-8") as file:
                data = json.load(file)
                data2 = str(data)
                pattern = r"[0-9a-f]{32}"
                match = re.finditer(pattern, data2)
                for m in match:
                    if m.group(0) == order:
                        order_hash = m.group(0)
                        break

                for i in data:
                    for j, k in i.items():
                        if j == "order_id" and k == order_hash:
                            saved = i
                            break
        except FileNotFoundError:
            raise OrderManagementException("Order_Request not Found")
        except json.decoder.JSONDecodeError:
            raise OrderManagementException("JSON has not the expected stucture")

        # print("hey", saved)
        if not saved:
            raise OrderManagementException("Data in Json has no valid values")

        Order_manager_tests_verificator = OrderManager()
        Order_manager_tests_verificator.validate_order_type(saved["order_type"])
        Order_manager_tests_verificator.validate_address(saved["delivery_address"])
        Order_manager_tests_verificator.validate_phone_number(saved["phone_number"])
        Order_manager_tests_verificator.validate_zip_code(saved["zip_code"])
        Order_manager_tests_verificator.validate_ean13(saved["product_id"])

        checker = f'OrderRequest:{{"_OrderRequest__product_id": "{saved["product_id"]}", "_OrderRequest__delivery_address":' \
                  f' "{saved["delivery_address"]}", "_OrderRequest__order_type": "{saved["order_type"]}",' \
                  f' "_OrderRequest__phone_number": "{saved["phone_number"]}", ' \
                  f'"_OrderRequest__zip_code": "{saved["zip_code"]}", "_OrderRequest__time_stamp": {saved["time_stamp"]}}}'
        # print(a)
        checker = hashlib.md5(checker.encode(encoding="utf-8")).hexdigest()
        # print(a)
        if checker != order:
            raise OrderManagementException("The data has been modified")

        # Generate an instance of the class OrderShipping
        # Email check:
        pattern = r'[A-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}'
        match = re.finditer(pattern, data_og)
        for m in match:
            email = m.group(0)
        order_shipping = OrderShipping(saved["product_id"], saved["order_id"], email, saved["order_type"])
        # print tracking_code or signature string or tracking_code:
        tracking_code = order_shipping.tracking_code
        self.validate_tracking_code(tracking_code)
        # Save the order_shipping into the file
        try:
            with open(json_order_shipping, "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.append(order_shipping.to_json())
                file.seek(0)
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            raise OrderManagementException("Order file has not been found")
        my_order_shipping = OrderShipping("8421691423220","e01521684a7f9535e9fa098a2b86565f","example@inf.uc3m.es","REGULAR")
        our_tracking_code = my_order_shipping.tracking_code
        self.assertEqual(tracking_code,our_tracking_code)

    def validate_tracking_code(self, sha256):
        pattern = r'[a-f0-9]{64}'
        match = re.fullmatch(pattern, sha256)
        if not match:
            raise OrderManagementException("Internal processing error")


if __name__ == '__main__':
    unittest.main()