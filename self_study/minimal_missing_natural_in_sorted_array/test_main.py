import unittest
from unittest import TestCase
import main as mn


class Test(TestCase):
    def test_bin_search_first_greater_than(self):
        arr = [1, 2, 3, 4, 8]
        self.assertEqual(mn.bin_search_first_greater_than(arr, 6), 8, "not good")


if __name__ == '__main__':
    unittest.main()
