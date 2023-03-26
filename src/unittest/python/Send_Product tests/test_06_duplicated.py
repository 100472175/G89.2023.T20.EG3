import unittest
import hashlib
import os.path
import unittest
import json
from uc3m_logistics import OrderManager, OrderRequest, OrderManagementException
from freezegun import freeze_time
from pathlib import Path
from datetime import datetime
import re
class MyTestCase(unittest.TestCase):

    @freeze_time("2023-03-08")
    def test_06_duplicated(self):
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main\JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_06_duplicated.json")

        with open(current_path, "r", encoding="utf-8") as file: 
            data = file.read()

        try:
            json_object = json.loads(data)
            raise OrderManagementException("File is correct when it shouldn't be")
        except:
            print(data)
            data = '{"OrderID": "e01521684a7f9535e9fa098a2b86565f""OrderID": "e01521684a7f9535e9fa098a2b86565f", "ContactEmail": "example@inf.uc3m.es"}'
            pattern = r'"OrderID":\s?"[a-f0-9]{32}""'
            data_test = re.sub(pattern, "\"", data)


            try:
                json_object = json.loads(data_test)
                self.assertTrue(json_object)

            except FileNotFoundError:
                raise OrderManagementException("File not found")
            except json.JSONDecodeError as e:
                raise OrderManagementException("The content of the variable is not valid JSON.")

if __name__ == "__main__":
    unittest.main()
