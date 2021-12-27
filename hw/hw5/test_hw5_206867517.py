import math
import unittest
import hw5_206867517 as hw5
from hw5_206867517 import Point
from hw5_206867517 import Polygon
from hw5_206867517 import Linked_list
from hw5_206867517 import Node
from numpy import *
import numpy as np
from hw5_206867517 import FactoredInteger
from hw5_206867517 import Point
from hw5_206867517 import Binary_search_tree
from hw5_206867517 import Dict


class TestHw5(unittest.TestCase):
    ##############
    # QUESTION 2 #
    ##############

    def test_repr(self):
        number1 = "<12:2*2*3>"
        number2 = "<1:>"
        number3 = "<64:2*2*2*2*2*2>"
        number4 = "<97:97>"
        number5 = "<48:2*2*2*2*3>"

        num1 = FactoredInteger([2, 2, 3])  # 12
        num2 = FactoredInteger([])  # 1
        num3 = FactoredInteger([2, 2, 2, 2, 2, 2])  # 64
        num4 = FactoredInteger([97])  # 97
        num5 = FactoredInteger([2, 2, 2, 2, 3])  # 48

        self.assertEqual(number1, str(num1))
        self.assertEqual(number2, str(num2))
        self.assertEqual(number3, str(num3))
        self.assertEqual(number4, str(num4))
        self.assertEqual(number5, str(num5))

    def test_equals(self):
        num1 = FactoredInteger([2, 2, 3])
        num2 = FactoredInteger([])
        num3 = FactoredInteger([2, 2, 2, 2, 2, 2])

        num11 = FactoredInteger([2, 2, 3])
        num22 = FactoredInteger([])
        num33 = FactoredInteger([2, 2, 2, 2, 2, 2])

        self.assertEqual(True, num1 == num11)
        self.assertEqual(False, num1 == num2)
        self.assertEqual(True, num3 == num33)
        self.assertEqual(False, num2 == num33)
        self.assertEqual(True, num2 == num2)
        self.assertEqual(False, num2 == num11)

    def test_mul(self):
        num12 = FactoredInteger([2, 2, 3])
        num1 = FactoredInteger([])  # 1
        num64 = FactoredInteger([2, 2, 2, 2, 2, 2])
        num97 = FactoredInteger([97])
        num48 = FactoredInteger([2, 2, 2, 2, 3])

        number12 = FactoredInteger([2, 2, 3])
        number768 = FactoredInteger([2, 2, 2, 2, 2, 2, 2, 2, 3])
        number1164 = FactoredInteger([2, 2, 3, 97])
        number1 = FactoredInteger([])

        self.assertEqual(True, num12 * num1 == num12)
        self.assertEqual(True, num1 * num12 == num12)
        self.assertEqual(False, num1 * num64 == num12)
        self.assertEqual(True, num12 * num64 == number768)
        self.assertEqual(True, num1 * num1 == number1)
        self.assertEqual(True, num12 * num97 == number1164)

    def test_pow(self):
        number12 = FactoredInteger([2, 2, 3])
        number1 = FactoredInteger([])  # 1
        number2 = FactoredInteger([2])
        number3 = FactoredInteger([3])
        number97 = FactoredInteger([97])

        number144 = FactoredInteger([2, 2, 2, 2, 3, 3])  # 12**2
        number9409 = FactoredInteger([97, 97])  # 97**2

        number8 = FactoredInteger([2, 2, 2])
        num43 = FactoredInteger([97, 97, 97])

        self.assertEqual(True, number1 ** number1 == number1)
        self.assertEqual(True, number2 ** number1 == number2)
        self.assertEqual(True, number97 ** number3 == num43)
        self.assertEqual(True, number2 ** number3 == number8)
        self.assertEqual(True, number12 ** number2 == number144)
        self.assertEqual(True, number97 ** number2 == number9409)

    def test_gcd(self):
        number54 = FactoredInteger([2, 3, 3, 3])
        number24 = FactoredInteger([2, 2, 2, 3])
        number6 = FactoredInteger([2, 3])

        number97 = FactoredInteger([97])
        number3 = FactoredInteger([3])
        number1 = FactoredInteger([])

        self.assertEqual(True, number54.gcd(number24) == number6)
        self.assertEqual(True, number24.gcd(number54) == number6)
        self.assertEqual(True, number97.gcd(number3) == number1)
        self.assertEqual(True, number3.gcd(number97) == number1)
        self.assertEqual(True, number97.gcd(number97) == number97)

    ##############
    # QUESTION 3 #
    ##############

    def test_angle_between_points(self):
        p = Point(1, 0)
        q = Point(0, 1)
        self.assertAlmostEqual(0.5 * math.pi, p.angle_between_points(q), 1)
        self.assertAlmostEqual((3 / 2) * math.pi, q.angle_between_points(p), 1)

        p = Point(1, 1)
        q = Point(0, 1)
        self.assertAlmostEqual(0.25 * math.pi, p.angle_between_points(q), 1)
        self.assertAlmostEqual((7 / 4) * math.pi, q.angle_between_points(p), 1)

        p = Point(-1, -1)
        q = Point(0, 1)
        self.assertAlmostEqual((5 / 4) * math.pi, p.angle_between_points(q), 1)
        self.assertAlmostEqual((3 / 4) * math.pi, q.angle_between_points(p), 1)

    def test_find_optimal_angle(self):
        trees = [Point(2, 1), Point(0, 3), Point(-1, 3), Point(-1, 1), Point(-1, -1), Point(0, -5)]
        self.assertAlmostEqual(1.570, hw5.find_optimal_angle(trees, 0.25 * math.pi), 2)

        trees = [Point(0.5, 1), Point(1, 1), Point(0, 1), Point(-1, 0)]
        self.assertAlmostEqual(0.25 * math.pi, hw5.find_optimal_angle(trees, 0.25 * math.pi), 2)

        trees = [Point(0.5, 1), Point(1, 1), Point(0, 1), Point(-1, 0), Point(-1, 1), Point(-1, 0.75), Point(-1, 0.5)]
        self.assertAlmostEqual((3 / 4) * math.pi, hw5.find_optimal_angle(trees, 0.25 * math.pi), 2)

    def test_edges(self):
        isosceles_triangle1 = Polygon(Linked_list([Point(0, 0), Point(6, 0), Point(3, 3 ** 0.5 * 0.5 * 6)]))
        isosceles_triangle2 = Polygon(Linked_list([Point(0, 0), Point(3, 3 ** 0.5 * 0.5 * 6), Point(6, 0)]))
        isosceles_triangle3 = Polygon(Linked_list([Point(3, 3 ** 0.5 * 0.5 * 6), Point(0, 0), Point(6, 0)]))
        isosceles_triangle4 = Polygon(Linked_list([Point(3, 3 ** 0.5 * 0.5 * 6), Point(6, 0), Point(0, 0)]))
        angles = [60.0, 60.0, 60.0]
        np.testing.assert_almost_equal(angles, isosceles_triangle1.edges(), 1)
        np.testing.assert_almost_equal(angles, isosceles_triangle2.edges(), 1)
        np.testing.assert_almost_equal(angles, isosceles_triangle3.edges(), 1)
        np.testing.assert_almost_equal(angles, isosceles_triangle4.edges(), 1)

        square1 = Polygon(Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]))
        square2 = Polygon(Linked_list([Point(1, 0), Point(1, 1), Point(0, 1), Point(0, 0)]))
        square3 = Polygon(Linked_list([Point(1, 1), Point(0, 1), Point(0, 0), Point(1, 0)]))
        square4 = Polygon(Linked_list([Point(0, 1), Point(0, 0), Point(1, 0), Point(1, 1)]))
        angles = [90.0, 90.0, 90.0, 90.0]
        np.testing.assert_almost_equal(angles, square1.edges(), 1)
        np.testing.assert_almost_equal(angles, square2.edges(), 1)
        np.testing.assert_almost_equal(angles, square3.edges(), 1)
        np.testing.assert_almost_equal(angles, square4.edges(), 1)

        pentagon1 = Polygon(
            Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0.5, 3 ** 0.5 * 0.5 + 1), Point(0, 1)]))
        angles = [90.0, 90.0, 150.0, 60.0, 150.0]
        np.testing.assert_almost_equal(angles, pentagon1.edges(), 1)

    def test_simple(self):
        square1 = Polygon(Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]))
        square2 = Polygon(Linked_list([Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0)]))
        # square3 = Polygon(Linked_list([Point(1, 1), Point(2, 2), Point(2, 0), Point(3, 1)]))
        pentagon1 = Polygon(Linked_list([Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0), Point(2, 0.5)]))

        self.assertEqual(True, square1.simple())
        self.assertEqual(False, square2.simple())
        # self.assertEqual(False, square3.simple())
        self.assertEqual(False, pentagon1.simple())

    ##############
    # QUESTION 4 #
    ##############

    def test_diam(self):
        t1 = Binary_search_tree()
        t1.insert('e', 1)
        t1.insert('c', 1)
        t1.insert('d', 1)
        t1.insert('b', 1)
        t1.insert('a', 1)
        self.assertEqual(4, t1.diam())
        t1.insert('m', 1)
        self.assertEqual(5, t1.diam())
        t1.insert('j', 1)
        self.assertEqual(6, t1.diam())
        t1.insert('i', 1)
        t1.insert('h', 1)
        t1.insert('g', 1)
        t1.insert('f', 1)
        t1.insert('n', 1)
        t1.insert('o', 1)
        t1.insert('p', 1)
        self.assertEqual(10, t1.diam())

    def test_cumsum(self):
        t1 = Binary_search_tree()
        t1.insert('ea', 1)
        t1.insert('e', 1)
        t1.insert('eb', 1)
        t1.insert('f', 1)
        t1.insert('i', 1)
        t1.insert('gi', 1)
        t1.insert('j', 1)
        t1.cumsum()
        self.assertEqual(
            [('e', 1), ('eea', 1), ('eeaeb', 1), ('eeaebf', 1), ('eeaebfgi', 1), ('eeaebfgii', 1), ('eeaebfgiij', 1)],
            t1.inorder())

        t2 = Binary_search_tree()
        t2.insert('ea', 1)

        t2.insert('eb', 1)
        t2.insert('f', 1)
        t2.insert('i', 1)
        t2.insert('gi', 1)
        t2.insert('j', 1)
        t2.cumsum()
        self.assertEqual([('ea', 1), ('eaeb', 1), ('eaebf', 1), ('eaebfgi', 1), ('eaebfgii', 1), ('eaebfgiij', 1)],
                         t2.inorder())

    ##############
    # QUESTION 5 #
    ##############

    def test_prefix_suffix_overlap(self):
        s = ['aba', 'bab', 'a', 'b', 'cca', 'ccab', 'aaaa']
        self.assertEqual(sorted(
            [(0, 2), (0, 4), (0, 6), (1, 3), (1, 5), (2, 0), (2, 4), (2, 6), (3, 1), (3, 5), (6, 0), (6, 2), (6, 4)]),
            sorted(hw5.prefix_suffix_overlap(s, 1)))
        s = ['aba', 'bab', 'ab', 'ab', 'cca', 'ccab', 'aaaa']
        self.assertEqual(sorted(
            [(0, 1), (0, 2), (0, 3), (0, 5), (1, 0), (2, 1), (2, 3), (2, 5), (3, 1), (3, 2), (3, 5)]),
            sorted(hw5.prefix_suffix_overlap(s, 2)))

    def test_find(self):
        d = Dict(7)
        s = ['aba', 'bab', 'a', 'b', 'cca', 'ccab', 'aaaa']

        for i in range(len(s)):
            d.insert(s[i][:1], i)
        self.assertEqual(sorted([0, 2, 6]), sorted(d.find('a')))
        self.assertEqual(sorted([1, 3]), sorted(d.find('b')))
        self.assertEqual(sorted([4, 5]), sorted(d.find('c')))
        self.assertEqual(sorted([]), sorted(d.find('d')))
        self.assertEqual(sorted([]), sorted(d.find('aa')))
        self.assertEqual(sorted([]), sorted(d.find('h')))

        s = ['aba', 'bab', 'ab', 'ab', 'cca', 'ccab', 'aaaa']
        d2 = Dict(7)
        for i in range(len(s)):
            d2.insert(s[i][:2], i)

        self.assertEqual(sorted([]), sorted(d2.find('a')))
        self.assertEqual(sorted([]), sorted(d2.find('b')))
        self.assertEqual(sorted([0, 2, 3]), sorted(d2.find('ab')))
        self.assertEqual(sorted([1]), sorted(d2.find('ba')))
        self.assertEqual(sorted([6]), sorted(d2.find('aa')))
        self.assertEqual(sorted([]), sorted(d2.find('h')))
        self.assertEqual(sorted([4, 5]), sorted(d2.find('cc')))
        self.assertEqual(sorted([]), sorted(d2.find('ccc')))

    def test_prefix_suffix_overlap_hash1(self):

        s = ['aba', 'bab', 'a', 'b', 'cca', 'ccab', 'aaaa']

        s1 = ['aba', 'bab', 'ab', 'ab', 'cca', 'ccab', 'aaaa']

        self.assertEqual(sorted(
            [(0, 2), (0, 4), (0, 6), (1, 3), (1, 5), (2, 0), (2, 4), (2, 6), (3, 1), (3, 5), (6, 0), (6, 2), (6, 4)]),
            sorted(hw5.prefix_suffix_overlap_hash1(s, 1)))

        self.assertEqual(sorted(
            [(0, 1), (0, 2), (0, 3), (0, 5), (1, 0), (2, 1), (2, 3), (2, 5), (3, 1), (3, 2), (3, 5)]),
            sorted(hw5.prefix_suffix_overlap_hash1(s1, 2)))

    def test(self):
        hw5.test()


if __name__ == "__main__":
    unittest.main()