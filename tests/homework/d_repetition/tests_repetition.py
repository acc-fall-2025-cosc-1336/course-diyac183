import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(0), 1)
        self.assertEqual(get_factorial(1), 1)
        self.assertEqual(get_factorial(3), 6)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(10), 25)  # 1 + 3 + 5 + 7 + 9 = 25
        self.assertEqual(sum_odd_numbers(1), 1)    # Only 1 is odd
        self.assertEqual(sum_odd_numbers(0), 0)    # No odd numbers
        self.assertEqual(sum_odd_numbers(15), 64)  # 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64