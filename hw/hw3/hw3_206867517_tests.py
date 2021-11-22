import unittest
import hw3_206867517 as hw3


class MyTestCase(unittest.TestCase):
    # Q2 - c
    def test_bin_to_fraction(self):
        self.assertEqual(0.40625, hw3.bin_to_fraction('01101'))
        self.assertEqual(0.5, hw3.bin_to_fraction('1'))
        self.assertEqual(0.75, hw3.bin_to_fraction('11'))
        self.assertEqual(0.875, hw3.bin_to_fraction('111'))
        self.assertEqual(0.625, hw3.bin_to_fraction('1010000'))

        # Q2 - D
    def test_bin_to_float(self):
            self.assertEqual(0.15625, hw3.bin_to_float('00111110001000000000000000000000'))
            self.assertEqual(2, hw3.bin_to_float('01000000000000000000000000000000'))
            self.assertEqual(-2, hw3.bin_to_float('11000000000000000000000000000000'))
            self.assertEqual(-36893488147419103232, hw3.bin_to_float('11100000000000000000000000000000'))
            self.assertEqual(-118842243771396506390315925504, hw3.bin_to_float('111011111100000000000000000000000'))

        # # Q2 - E
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

        # # Q3 - A
        # if approx_root(2, 0.1) != ([1, 3], 1 + 1 / 3):
        #     print("error in approx_root (1)")
        # if approx_root(2, 0.02) != ([1, 3, 5], 1 + 1 / 3 + 1 / 15):
        #     print("error in approx_root (2)")
        # if approx_root(2, 0.001) != ([1, 3, 5, 5], 1 + 1 / 3 + 1 / 15 + 1 / 75):
        #     print("error in approx_root (3)")
        # # Q3 - B
        # if abs(approx_e(1000000) - math.e) > 0.01:
        #     print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")
        #
        # # Q4 - A
        # almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
        # if find(almost_sorted_lst, 5) != 3:
        #     print("error in find")
        # if find(almost_sorted_lst, 50) != None:
        #     print("error in find")
        # # Q4 - B
        # if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        #     print("error in sort_from_almost")
        # # Q4 - C
        # lst = [5, 6, 7, 5, 1, 1, 99, 100]
        # pos = find_local_min(lst)
        # if pos not in (0, 4, 5):
        #     print("error in find_local_min")
        #
        # # Q5
        # lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
        # for i in lst_num:
        #     s = int_to_string(4, i)
        #     if s is None or len(s) != 4:
        #         print("error in int_to_string")
        #     if string_to_int(s) != i:
        #         print("error in int_to_string and/or in string_to_int")
        #
        # lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
        # if sort_strings1(lst1, 4) \
        #         != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        #     print("error in sort_strings1")
        #
        # if sort_strings2(lst1, 4) \
        #         != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        #     print("error in sort_strings2")


if __name__ == '__main__':
    unittest.main()
