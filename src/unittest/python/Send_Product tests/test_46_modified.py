import os.path
import unittest
import os
from uc3m_logistics import OrderManager,OrderShipping
from freezegun import freeze_time

class MyTestCase(unittest.TestCase):

    @freeze_time("2023-03-08")
    def test_46_modified(self):
        current_path = os.path.dirname(__file__)
        current_path = current_path[:-34]
        json_path = "main/JsonFiles"
        current_path = os.path.join(current_path, json_path, "test_46_modified.json")

        my_order = OrderManager()
        my_tracking_code = my_order.send_product(current_path)

        my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f", "e@inf.uc3m.es",
                                    "REGULAR").tracking_code
        self.assertEqual(my_shipping, my_tracking_code)


if __name__ == "__main__":
    unittest.main()
