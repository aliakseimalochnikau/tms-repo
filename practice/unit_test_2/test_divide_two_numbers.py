import unittest

from practice import divide_two_numbers


class TestDivideTwoNumbers(unittest.TestCase):
    def test_smoke(self):
        result = divide_two_numbers(10, 5)
        self.assertEqual(result, 2)