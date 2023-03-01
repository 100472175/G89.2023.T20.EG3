import unittest
from unittest import TestCase
from Subs import substraction
from Subs import MyException

class Test(TestCase):
    def test_substraction(self):
        self.assertRaises(MyException, substraction, "a",4 )

    def test_substraction2(self):
        with  self.assertRaises(MyException) as cm:
            substraction("a",4)
        self.assertEqual (cm.exception.valor, "Must be int or float")

    def test_substraction3(self):
        self.assertEqual(substraction(5,3),2)

    def test_substraction4(self):
        self.assertAlmostEqual(substraction(15.4,5.1),10.3, 2)


if __name__ == '__main__':
    unittest.main()
