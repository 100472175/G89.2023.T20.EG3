import unittest
from unittest import TestCase
from calculator import sum
from calculator import CalculatorException


class TestCalculator(TestCase):
    @classmethod
    def setUpClass(cls):
        print("Execute setUpClass Classmethod")

    @classmethod
    def tearDownClass(cls):
        print("Execute tearDownClass Classmethod")

    def setUp(self):
        print("Execute setUp")

    def tearDown(self):
        print("Execute tearDown")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_sum_validcase(self):
        self.assertEqual(9, sum(5, 4))

    def test_sum_invalidcase_b(self):
        with self.assertRaises(CalculatorException) as cm:
            sum_result = sum(5, 'a')
        self.assertEqual("Invalid datatype in sum parameter", cm.exception.value)

    def test_sum_invalidcase_a(self):
        with self.assertRaises(CalculatorException) as cm:
            sum_result = sum('a', 5)
        self.assertEqual("Invalid datatype in sum parameter", cm.exception.value)

    def test_sum_invalidcase_both(self):
        self.assertRaises(CalculatorException, sum, 'a', 'b')


if __name__ == '__main__':
    unittest.main()
