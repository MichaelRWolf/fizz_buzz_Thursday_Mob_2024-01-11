import unittest
from src.FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_fizz(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(3), "Fizz")
        self.assertEqual(self.fizzbuzz.fizzbuzz(6), "Fizz")

    def test_buzz(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(5), "Buzz")
        self.assertEqual(self.fizzbuzz.fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(self.fizzbuzz.fizzbuzz(30), "FizzBuzz")

    def test_numbers(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(2), "2")
        self.assertEqual(self.fizzbuzz.fizzbuzz(4), "4")


if __name__ == '__main__':
    unittest.main()
