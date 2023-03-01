import unittest
from unittest import TestCase
from Subs import substraction
from Subs import MyException

class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print ("Execute setUpClass Classmethod")

    @classmethod
    def tearDownClass(cls):
        print("Execute tearDownClass Classmethod")

    def setUp(self):
        print("Execute setUp")

    def tearDown(self):
        print("Execute tearDown")

    def test_substraction(self):
        self.assertRaises(MyException, substraction, "a", 4)
        print ("Execute substraction")

    def test_substraction2(self):
        with  self.assertRaises(MyException) as cm:
            substraction("a",4)
        self.assertEqual (cm.exception.valor, "Must be int or float")
        print("Execute substraction2")

    def test_substraction3(self):
        self.assertEqual(substraction(5,3),2)
        print("Execute substraction3")

    def test_substraction4(self):
        self.assertAlmostEqual(substraction(15.4,5.1),10.3, 2)
        print("Execute substraction4")


if __name__ == '__main__':
    unittest.main()
