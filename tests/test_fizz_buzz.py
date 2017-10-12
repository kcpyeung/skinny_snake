import unittest
from fizzbuzz.MyFizzBuzz import MyFizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_1_is_1(self):
        fb = MyFizzBuzz()
        self.assertEqual(1, fb.fizzbuzz(1))
