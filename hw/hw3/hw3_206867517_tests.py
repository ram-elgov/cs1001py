import math
import unittest

import hw3_206867517 as hw3


class TestHm3(unittest.TestCase):
    def test_bin_to_fraction(self):
        self.assertEqual(0.40625, hw3.bin_to_fraction('01101'))
        self.assertEqual(0.5, hw3.bin_to_fraction('1'))
        self.assertEqual(0.75, hw3.bin_to_fraction('11'))
        self.assertEqual(0.875, hw3.bin_to_fraction('111'))
        self.assertEqual(0.625, hw3.bin_to_fraction('1010000'))

    def test_bin_to_float(self):
        self.assertEqual(0.15625, hw3.bin_to_float('00111110001000000000000000000000'))
        self.assertEqual(2, hw3.bin_to_float('01000000000000000000000000000000'))
        self.assertEqual(-2, hw3.bin_to_float('11000000000000000000000000000000'))
        self.assertEqual(-36893488147419103232, hw3.bin_to_float('11100000000000000000000000000000'))
        self.assertEqual(-118842243771396506390315925504, hw3.bin_to_float('111011111100000000000000000000000'))

    def test_is_greater_equal(self):
        self.assertEqual(False,
                         hw3.is_greater_equal('00111110001000000000000000000000', '00111111001000000000000000000000'))
        self.assertEqual(True,
                         hw3.is_greater_equal('00111110001000000000000000000000', '00111110001000000000000000000000'))
        self.assertEqual(True,
                         hw3.is_greater_equal('11000000010000000000000000000000', '11000000011000000000000000000000'))
        self.assertEqual(False,
                         hw3.is_greater_equal('11000000110000000000000000000000', '11000000011000000000000000000000'))
        self.assertEqual(True,
                         hw3.is_greater_equal('11000000011000000000000000000000', '11000000110000000000000000000000'))
        self.assertEqual(False,
                         hw3.is_greater_equal('11000000110000000000000000000000', '01000000011000000000000000000000'))
        self.assertEqual(True,
                         hw3.is_greater_equal('01000000110000000000000000000000', '11000000011000000000000000000000'))

    def test_approx_root(self):
        self.assertEqual(([1, 3], 1.3333333333333333), hw3.approx_root(2, 0.1))
        self.assertEqual(([1, 1, 5], 2.2), hw3.approx_root(5, 0.1))
        self.assertEqual(([1, 1, 1], 3), hw3.approx_root(9, 0.1))
        self.assertEqual(([1, 1, 3, 3], 2.4444444444444446), hw3.approx_root(6, 0.1))
        self.assertEqual(([1, 1, 2, 2], 2.75), hw3.approx_root(8, 0.1))
        self.assertEqual(([1, 1, 2, 2, 4, 4], 2.828125), hw3.approx_root(8, 0.01))
        self.assertEqual(([1, 3, 5, 5, 16, 18, 78], 1.4142135565052232), hw3.approx_root(2, 0.00000001))
        self.assertEqual(([1, 1, 5, 6, 13, 16, 16, 38, 48, 58], 2.236067977498874),
                         hw3.approx_root(5, 0.00000000001))

    def test_approx_e(self):
        self.assertEqual(True, abs(math.e - hw3.approx_e(100)) < 0.3)
        self.assertEqual(True, abs(math.e - hw3.approx_e(1000)) < 0.2)
        self.assertEqual(True, abs(math.e - hw3.approx_e(10000)) < 0.1)

    def test_find(self):
        self.assertEqual(3, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 5))
        self.assertEqual(0, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 2))
        self.assertEqual(1, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 1))
        self.assertEqual(2, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 3))
        self.assertEqual(4, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 4))
        self.assertEqual(5, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 7))
        self.assertEqual(6, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 6))
        self.assertEqual(7, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 8))
        self.assertEqual(8, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 9))
        self.assertEqual(None, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 0))
        self.assertEqual(None, hw3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 10))
        self.assertEqual(0, hw3.find([2, 1, 3], 2))
        self.assertEqual(3, hw3.find([2, 1, 3, 5], 5))
        self.assertEqual(1, hw3.find([2, 1], 1))

    def test_sort_from_almost(self):
        lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], hw3.sort_from_almost(lst))

        lst = [2, 1, 4, 3, 6, 5, 8, 7, 9]

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], hw3.sort_from_almost(lst))

        lst = [1, 1, 1, 1, 1, 2, 1]

        self.assertEqual([1, 1, 1, 1, 1, 1, 2], hw3.sort_from_almost(lst))

        lst = [2, 1]

        self.assertEqual([1, 2], hw3.sort_from_almost(lst))

    def test_find_local_min(self):
        self.assertEqual(4, hw3.find_local_min([5, 4, 3, 2, 1, 2, 3, 4, 5]))
        self.assertEqual(3, hw3.find_local_min([5, 4, 3, 1, 2, 2.5, 3, 4, 5]))
        self.assertEqual(2, hw3.find_local_min([5, 4, 1, 2, 2.5, 2.75, 3, 4, 5]))
        self.assertEqual(1, hw3.find_local_min([5, 1, 2.1, 2.2, 2.3, 2.4, 3, 4, 5]))
        self.assertEqual(0, hw3.find_local_min([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(6, hw3.find_local_min([7, 6, 5, 4, 3, 2, 1]))

    def test_injective_func(self):
        str1 = 'aaaaaaaaa'
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "abaaaaaaa"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "aacaaaaaa"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "aaadaaaaa"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "aaaaaeaaa"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "aaaaaeeaa"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "aaaaaeaea"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "eaaaaeaae"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "eeeeeeeee"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "ddeeccaab"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "abcdeabcd"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "aede"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "ae"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "a"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "b"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))
        str1 = "e"
        self.assertEqual(str1, hw3.int_to_string(len(str1), hw3.string_to_int(str1)))

    def test_sort_strings1(self):
        lst1 = ["eee", "ddd", "ccc", "bbb", "aaa"]
        self.assertEqual(lst1[::-1], hw3.sort_strings1(lst1, 3))
        lst1 = ["eee", "edc", "ecb", "eba", "eee"]
        self.assertEqual(["eba", "ecb", "edc", "eee", "eee"], hw3.sort_strings1(lst1, 3))
        lst1 = ["eee", "eac", "eab", "eaa", "eee"]
        self.assertEqual(["eaa", "eab", "eac", "eee", "eee"], hw3.sort_strings1(lst1, 3))
        lst1 = ["aae", "aad", "aad", "aac", "aab"]
        self.assertEqual(["aab", "aac", "aad", "aad", "aae"], hw3.sort_strings1(lst1, 3))
        lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
        self.assertEqual(['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea'],
                         hw3.sort_strings1(lst1, 4))
        lst1 = ['aaec', 'abcd', 'dcba', 'bacd', 'cdab', 'cccc', 'cccb', 'eded', 'dede', 'abca']
        self.assertEqual(['aaec', 'abca', 'abcd', 'bacd', 'cccb', 'cccc', 'cdab', 'dcba', 'dede', 'eded'],
                         hw3.sort_strings1(lst1, 4))
        lst1 = ['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']
        self.assertEqual(['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc'],
                         hw3.sort_strings1(lst1, 3))
        lst1 = ['eee', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']
        self.assertEqual(['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'eee'],
                         hw3.sort_strings1(lst1, 3))

    def test_sort_strings2(self):
        lst1 = ["eee", "ddd", "ccc", "bbb", "aaa"]
        self.assertEqual(lst1[::-1], hw3.sort_strings2(lst1, 3))
        lst1 = ["eee", "edc", "ecb", "eba", "eee"]
        self.assertEqual(["eba", "ecb", "edc", "eee", "eee"], hw3.sort_strings2(lst1, 3))
        lst1 = ["eee", "eac", "eab", "eaa", "eee"]
        self.assertEqual(["eaa", "eab", "eac", "eee", "eee"], hw3.sort_strings2(lst1, 3))
        lst1 = ["aae", "aad", "aad", "aac", "aab"]
        self.assertEqual(["aab", "aac", "aad", "aad", "aae"], hw3.sort_strings2(lst1, 3))
        lst1 = ["aae", "aad", "aad", "aac", "aab"]
        self.assertEqual(["aab", "aac", "aad", "aad", "aae"], hw3.sort_strings2(lst1, 3))
        lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
        self.assertEqual(['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea'],
                         hw3.sort_strings2(lst1, 4))
        lst1 = ['aaec', 'abcd', 'dcba', 'bacd', 'cdab', 'cccc', 'cccb', 'eded', 'dede', 'abca']
        self.assertEqual(['aaec', 'abca', 'abcd', 'bacd', 'cccb', 'cccc', 'cdab', 'dcba', 'dede', 'eded'],
                         hw3.sort_strings2(lst1, 4))
        lst1 = ['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']
        self.assertEqual(['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc'],
                         hw3.sort_strings1(lst1, 3))
        lst1 = ['eee', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc']
        self.assertEqual(['abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc', 'eee'],
                         hw3.sort_strings1(lst1, 3))
        lst1 = ['abc']
        self.assertEqual(['abc'],
                         hw3.sort_strings1(lst1, 3))
        lst1 = ['abcde', 'aaaaa']
        self.assertEqual(['aaaaa', 'abcde'],
                         hw3.sort_strings1(lst1, 5))


if __name__ == '__main__':
    unittest.main()
