import unittest
from unittest import TestCase
from Subs import substraction
from Subs import MyException

param_list = [("a", 4), (15, "b"), ("7", 1)]

class Test(TestCase):
    def test_wrong_values(self):
        for p1, p2 in param_list:
            with self.subTest():
                with  self.assertRaises(MyException) as cm:
                    substraction(p1,p2)
                self.assertEqual (cm.exception.valor, "Must be int or float")

    def test_substraction3(self):
        self.assertEqual(substraction(5,3),2)

    def test_substraction4(self):
        self.assertAlmostEqual(substraction(15.4,5.1),10.3, 2)


if __name__ == '__main__':
    unittest.main()
