import unittest
from unittest import TestCase
from Suma2 import suma

param_list = [(2, 3, 5), (4, 5, 9), (6, 8, 14)]

class Test(TestCase):
    def test_works_as_expected(self):
        for p1, p2, p3 in param_list:
            with self.subTest():
                self.assertEqual(suma(p1, p2), p3)

    def test_suma(self):
        self.assertEqual(suma(5, 7), 12)

    def test_suma_float(self):
        self.assertAlmostEqual(suma(5.2, 7.4), 12.6, 7)

    def test_suma_error(self):
        self.assertRaises(TypeError, suma, "p", "d")


if __name__ == "__main__":
    unittest.main()