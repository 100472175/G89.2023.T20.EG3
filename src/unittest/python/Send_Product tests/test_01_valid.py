import unittest
import hashlib
import os.path
import unittest
import json
from uc3m_logistics import OrderManager, OrderRequest, OrderManagementException
from freezegun import freeze_time
from pathlib import Path
from datetime import datetime

class MyTestCase(unittest.TestCase):
    def test_01_valid(self):
        my_manager = (self)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
