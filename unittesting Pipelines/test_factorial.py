#test_factorial.py

import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_two(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_of_three(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_of_four(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_of_five(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
