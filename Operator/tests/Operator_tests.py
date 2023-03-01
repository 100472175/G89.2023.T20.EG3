import unittest
from unittest import TestCase

from Class_unittest_more.Operator.Operator import operator
from Class_unittest_more.Operator.Exception_error import MyException

param_list = [(2, 3, 5), (4, 5, 9), (6, 8, 14)]
param_list_wrong = [("a", 3), (4, "b"), ("2", "!")]

class Testoperator(TestCase):
    def test_suma_works_as_expected(self):
        for p1, p2, p3 in param_list:
            with self.subTest():
                self.assertEqual(operator.suma(p1, p2), p3)

    def test_suma_float(self):
        self.assertAlmostEqual(operator.suma(5.2, 7.4), 12.6, 7)

    def test_suma_error(self):
        self.assertRaises(MyException, operator.suma, "p", "d")

    def test_suma_wrong_values(self):
        for p1, p2 in param_list_wrong:
            with self.subTest():
                with  self.assertRaises(MyException) as cm:
                    operator.suma(p1, p2)
                self.assertEqual(cm.exception.valor, "Error Summa, values must be int or float")

    def test_div_works_as_expected(self):
        self.assertEqual(operator.div(10, 2), 5)

    def test_div_error(self):
        self.assertRaises(Exception, operator.div, 10, 0)

    def test_div_error(self):
        #this test print the exception
        with self.assertRaises(Exception) as cm:
            operator.div(10, 0)
        print("test_div_error ", cm.exception.__str__())
        print(self.id(), cm.exception.__str__())

if __name__ == '__main__':
    unittest.main()
