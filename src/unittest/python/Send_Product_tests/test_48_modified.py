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
    def test_48_modified(self):
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_48_modified.json")

        with open(current_path, "r", encoding="utf-8") as file:
            data = file.read()

        pattern = r'{"OrderID":\s?"[a-f0-9]{32}",\s?"ContactEmail":\s?"[A-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}"}'
        match = re.search(pattern, data)
        self.assertNotEqual(match, None)


if __name__ == "__main__":
    unittest.main()
