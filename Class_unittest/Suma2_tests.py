import unittest
from Suma2 import suma

class MyTestCase(unittest.TestCase):
    def test_suma_ok(self):
        self.assertEqual(suma(5, 7), 12)

    def test_suma_float(self):
        self.assertAlmostEqual(suma(5.2,7.4),12.6,7)

    def test_suma_nok(self):
        self.assertRaises(TypeError, suma, 5, "a")

if __name__ == '__main__':
    unittest.main()
