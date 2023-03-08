"""class for testing the regsiter_order method"""
import unittest
import freezegun
from uc3m_logistics import OrderManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    @freeze_time("2023-03-08")
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
