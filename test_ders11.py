import unittest
from ders11 import add, multiply, is_even, find_max


# 01
class MyTest(unittest.TestCase):
    def test_positive_add(self):
        result1 = add(4, 6)
        self.assertEqual(result1, 10)

    def test_negative_add(self):
        result2 = add(-4, -6)
        self.assertEqual(result2, -10)

    def test_mixed_add(self):
        result3 = add(4, -6)
        self.assertEqual(result3, -2)
# 02

    def test_positive_multiply(self):
        result4 = multiply(2, 5)
        self.assertEqual(result4, 10)

    def test_negative_multiply(self):
        result5 = multiply(-2, -5)
        self.assertEqual(result5, 10)

    def test_mixed_multiply(self):
        result6 = multiply(-3, 5)
        self.assertEqual(result6, -15)
# 03

    def test_is_even(self):
        result7 = is_even(13)
        self.assertEqual(result7, False)
# 04

    def test_positive_find_max(self):
        result8 = find_max([15, 76, 99, 58])
        self.assertEqual(result8, 99)

    def test_negative_find_max(self):
        result9 = find_max([-3, -1, -77, -100])
        self.assertEqual(result9, -1)

    def test_mixed_find_max(self):
        result10 = find_max([5, -7, 0, -11])
        self.assertEqual(result10, 5)

    def test_recurring_find_max(self):
        result11 = find_max([3, 44, 27, 44, 3])
        self.assertEqual(result11, 44)


if __name__ == '__main__':
    unittest.main()
