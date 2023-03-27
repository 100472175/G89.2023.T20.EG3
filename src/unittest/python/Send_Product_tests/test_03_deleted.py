import unittest
import hashlib
import os.path
import unittest
import json
import os
import re
from uc3m_logistics import OrderManager, OrderRequest, OrderManagementException
from freezegun import freeze_time
from pathlib import Path
from datetime import datetime

class MyTestCase(unittest.TestCase):

    @freeze_time("2023-03-08")
    def test_03_deleted(self):
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_03_deleted.json")

        with open(current_path, "r", encoding="utf-8") as file: 
            data = file.read()

        try:
            json_object = json.loads(data)
            raise OrderManagementException("File is correct when it shouldn't be")
        except:
            data_test = '{}'
            self.assertEqual(data_test, data)


if __name__ == "__main__":
    unittest.main()