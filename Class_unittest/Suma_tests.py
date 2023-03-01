import unittest
from unittest import TestCase
from Suma import sum

# test very simple

class TestEjemplo(TestCase):
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)

if __name__ == "__main__":
    unittest.main()
