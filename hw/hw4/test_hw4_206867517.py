import unittest
from unittest import TestCase
import hw4_206867517 as hw4


class Test(TestCase):

    def test_winnable_mem(self):
        self.assertTrue(hw4.winnable_mem([5, 5, 5]))
        self.assertFalse(hw4.winnable_mem([5, 5, 3]))
        self.assertFalse(hw4.winnable_mem([1]))
        self.assertTrue(hw4.winnable_mem([]))
        self.assertTrue(hw4.winnable_mem([2]))
        self.assertFalse(hw4.winnable_mem([2, 1]))
        self.assertEqual(True, hw4.winnable_mem([2, 1, 1]))
        self.assertEqual(False, hw4.winnable_mem([2, 1, 0]))
        self.assertEqual(False, hw4.winnable_mem([1, 0, 0]))
        self.assertEqual(False, hw4.winnable_mem([5, 5, 3]))
        self.assertEqual(True, hw4.winnable_mem([5, 5, 5]))
        self.assertEqual(True, hw4.winnable_mem([2, 1, 1]))
        self.assertEqual(True, hw4.winnable_mem([5] * 4))
        self.assertEqual(True, hw4.winnable_mem([5] * 8))
        self.assertEqual(True, hw4.winnable_mem([5] * 16))

    def test_h_local(self):
        self.assertEqual(hw4.H_local(2, 2, 2), 1)
        self.assertEqual(hw4.H_local(0, 0, 0), 0)
        self.assertEqual(hw4.H_local(1, 0, 0), 0)
        self.assertEqual(hw4.H_local(1, 0, 1), 0)
        self.assertEqual(hw4.H_local(1, 1, 0), 0)
        self.assertEqual(hw4.H_local(1, 1, 1), 1)
        self.assertEqual(hw4.H_local(2, 3, 3), 0)
        self.assertEqual(hw4.H_local(2, 2, 3), 1)
        self.assertEqual(hw4.H_local(2, 1, 1), 1)
        self.assertEqual(hw4.H_local(2, 3, 2), 1)
        self.assertEqual(hw4.H_local(2, 1, 2), 0)
        self.assertEqual(0, hw4.H_local(0, 0, 0))
        self.assertEqual(0, hw4.H_local(1, 0, 0))
        self.assertEqual(1, hw4.H_local(1, 1, 1))
        self.assertEqual(0, hw4.H_local(1, 1, 0))
        self.assertEqual(0, hw4.H_local(2, 0, 0))
        self.assertEqual(1, hw4.H_local(2, 1, 1))
        self.assertEqual(1, hw4.H_local(2, 1, 3))
        self.assertEqual(1, hw4.H_local(2, 3, 2))
        self.assertEqual(0, hw4.H_local(3, 4, 1))
        self.assertEqual(1, hw4.H_local(3, 4, 4))

    def test_H_complete(self):
        self.assertEqual(hw4.H_complete(0), [[0]])
        self.assertEqual(hw4.H_complete(1), [[0, 0], [0, 1]])
        self.assertEqual(hw4.H_complete(2), [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]])
        self.assertEqual(hw4.H_complete(3), [[0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 1, 0, 1, 0, 1, 0, 1],
                                             [0, 0, 1, 1, 0, 0, 1, 1],
                                             [0, 1, 1, 0, 0, 1, 1, 0],
                                             [0, 0, 0, 0, 1, 1, 1, 1],
                                             [0, 1, 0, 1, 1, 0, 1, 0],
                                             [0, 0, 1, 1, 1, 1, 0, 0],
                                             [0, 1, 1, 0, 1, 0, 0, 1]])
        self.assertListEqual([[0]], hw4.H_complete(0))
        self.assertListEqual([[0, 0], [0, 1]], hw4.H_complete(1))
        self.assertListEqual([[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]], hw4.H_complete(2))
        self.assertListEqual(
            [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 1]],
            hw4.H_complete(3))

    def test_can_create_once(self):
        self.assertTrue(hw4.can_create_once(0, []))
        self.assertFalse(hw4.can_create_once(-1, []))
        self.assertTrue(hw4.can_create_once(5, [5]))
        self.assertTrue(hw4.can_create_once(-5, [5]))
        self.assertTrue(hw4.can_create_once(-1, [1, 2]))
        self.assertTrue(hw4.can_create_once(6, [5, 2, 3]))
        self.assertTrue(hw4.can_create_once(-10, [5, 2, 3]))
        self.assertFalse(hw4.can_create_once(9, [5, 2, 3]))
        self.assertFalse(hw4.can_create_once(7, [5, 2, 3]))
        self.assertEqual(False, hw4.can_create_once(7, [5, 2, 3]))
        self.assertEqual(False, hw4.can_create_once(5, [5, 2, 3]))
        self.assertEqual(False, hw4.can_create_once(2, [5, 2, 3]))
        self.assertEqual(True, hw4.can_create_once(10, [5, 2, 3]))
        self.assertEqual(True, hw4.can_create_once(6, [5, 2, 3]))
        self.assertEqual(True, hw4.can_create_once(0, [5, 2, 3]))
        self.assertEqual(True, hw4.can_create_once(4, [5, 2, 3]))
        self.assertEqual(True, hw4.can_create_once(1, [1, 1, 1]))

    def test_can_create_twice(self):
        self.assertTrue(hw4.can_create_twice(6, [5, 2, 3]))
        self.assertTrue(hw4.can_create_twice(6, [5, 2, 3]))
        self.assertTrue(hw4.can_create_twice(9, [5, 2, 3]))
        self.assertTrue(hw4.can_create_twice(7, [5, 2, 3]))
        self.assertFalse(hw4.can_create_twice(19, [5, 2, 3]))
        self.assertFalse(hw4.can_create_twice(2, []))
        self.assertTrue(hw4.can_create_twice(0, [4]))
        self.assertTrue(hw4.can_create_twice(-4, [4]))
        self.assertTrue(hw4.can_create_twice(4, [4]))
        self.assertTrue(hw4.can_create_twice(0, []))
        self.assertEqual(True, hw4.can_create_twice(0, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(-4, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(6, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(2, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(5, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(3, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(1, [1, 2]))
        self.assertEqual(True, hw4.can_create_twice(1, [1, 2, 3]))
        self.assertEqual(True, hw4.can_create_twice(2, [1, 2, 3]))
        self.assertEqual(True, hw4.can_create_twice(3, [1, 2, 3]))
        self.assertEqual(True, hw4.can_create_twice(-1, [1, 2, 3]))
        self.assertEqual(False, hw4.can_create_twice(13, [1, 2, 3]))

    def test_valid_braces_placement(self):
        L = [6, '-', 4, '*', 2, '+', 3]
        L2 = [-4, '*', 4]
        L3 = [1, "*", 1, "*", 1]
        self.assertTrue(hw4.valid_braces_placement(10, L))
        self.assertTrue(hw4.valid_braces_placement(1, L))
        self.assertFalse(hw4.valid_braces_placement(5, L))
        self.assertTrue(hw4.valid_braces_placement(-16, L2))
        self.assertFalse(hw4.valid_braces_placement(16, L2))
        self.assertTrue(hw4.valid_braces_placement(1, L3))
        self.assertFalse(hw4.valid_braces_placement(0, L3))
        lst = [1, '+', 1, '+', 1, '+', 1, '+', 1, '*', 1]
        self.assertEqual(False, hw4.valid_braces_placement(10, lst))

        lst = [2, '*', 1, '+', 2, '*', 1, '+', 2, '*', 1]
        self.assertEqual(True, hw4.valid_braces_placement(6, lst))
        self.assertEqual(True, hw4.valid_braces_placement(18, lst))
        self.assertEqual(True, hw4.valid_braces_placement(10, lst))

        lst = [2, '*', 1, '+', 2, '*', 1, '+', 2, '*', 2]
        self.assertEqual(True, hw4.valid_braces_placement(8, lst))
        self.assertEqual(False, hw4.valid_braces_placement(1, lst))
        self.assertEqual(False, hw4.valid_braces_placement(45, lst))
        self.assertEqual(True, hw4.valid_braces_placement(28, lst))

        lst = [2, '*', 1, '*', 2, '*', 1, '*', 2, '+', 2]
        self.assertEqual(True, hw4.valid_braces_placement(16, lst))

    def test_grid_escape1(self):
        B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
        B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
        B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]
        B4 = [[1]]
        B5 = [[2, 2], [2, 2]]
        B6 = [[1, 0], [0, 1]]
        B7 = [[1, 0], [1, 1]]
        B8 = [[1, 0], [2, 1]]
        B9 = [[0, 1], [1, 1]]
        B10 = []
        B11 = [[2, 2, 1], [0, 0, 0], [0, 1, 0]]
        self.assertTrue(hw4.grid_escape1(B1))
        self.assertFalse(hw4.grid_escape1(B2))
        self.assertFalse(hw4.grid_escape1(B3))
        self.assertTrue(hw4.grid_escape1(B4))
        self.assertFalse(hw4.grid_escape1(B5))
        self.assertFalse(hw4.grid_escape1(B6))
        self.assertTrue(hw4.grid_escape1(B7))
        self.assertFalse(hw4.grid_escape1(B8))
        self.assertFalse(hw4.grid_escape1(B9))
        self.assertFalse(hw4.grid_escape1(B11))
        mat = [[1 for i in range(5)] for j in range(5)]
        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(True, hw4.grid_escape1(mat))

        mat[0][0] = 0
        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(False, hw4.grid_escape1(mat))

        mat[0][0] = 1
        mat[4][3] = 0
        mat[3][3] = 0

        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(True, hw4.grid_escape1(mat))

        mat[3][4] = 0

        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(False, hw4.grid_escape1(mat))

    @staticmethod
    def print_matrix(mat):
        length = len(mat)
        column = "     column  "
        row = "row"
        for i in range(length):
            column += str(i) + "  "

        print(column + "\n" + row)

        for i in range(length):
            st = " " + str(i) + " " + "          "
            for j in range(length):
                st += str(mat[i][j]) + "  "
            print(st)
        print("")

    def test_grid_escape2(self):
        B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
        B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
        B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]
        B4 = [[1]]
        B5 = [[2, 2], [2, 2]]
        B6 = [[1, 0], [0, 1]]
        B7 = [[1, 0], [1, 1]]
        B8 = [[1, 0], [2, 1]]
        B9 = [[0, 1], [1, 1]]
        B10 = []
        B11 = [[2, 2, 1], [0, 0, 0], [0, 1, 0]]
        self.assertTrue(hw4.grid_escape2(B1))
        self.assertTrue(hw4.grid_escape2(B2))
        self.assertFalse(hw4.grid_escape2(B3))
        self.assertTrue(hw4.grid_escape2(B4))
        self.assertFalse(hw4.grid_escape2(B5))
        self.assertFalse(hw4.grid_escape2(B6))
        self.assertTrue(hw4.grid_escape2(B7))
        self.assertFalse(hw4.grid_escape2(B8))
        self.assertFalse(hw4.grid_escape2(B9))
        self.assertTrue(hw4.grid_escape2(B10))
        self.assertTrue(hw4.grid_escape2(B11))
        mat = [[1 for i in range(5)] for j in range(5)]
        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(True, hw4.grid_escape2(mat))

        mat[0][0] = 0
        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(False, hw4.grid_escape2(mat))

        mat[0][0] = 1
        mat[4][3] = 0
        mat[3][3] = 0

        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(True, hw4.grid_escape2(mat))

        mat[3][4] = 0

        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(False, hw4.grid_escape2(mat))

        mat = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(True, hw4.grid_escape2(mat))

        mat = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]

        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(True, hw4.grid_escape2(mat))

        mat = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

        # Optional if you want to see the matrix
        # TestHw4.print_matrix(mat)
        self.assertEqual(False, hw4.grid_escape2(mat))

        def test_test():
            hw4.test()


if __name__ == '__main__':
    unittest.main()
