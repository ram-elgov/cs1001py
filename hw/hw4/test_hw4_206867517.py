from unittest import TestCase
import hw4_206867517 as hw


class Test(TestCase):

    def test_winnable_mem(self):
        self.assertTrue(hw.winnable_mem([5, 5, 5]))
        self.assertFalse(hw.winnable_mem([5, 5, 3]))
        self.assertFalse(hw.winnable_mem([1]))
        self.assertTrue(hw.winnable_mem([]))
        self.assertTrue(hw.winnable_mem([2]))
        self.assertFalse(hw.winnable_mem([2, 1]))

    def test_h_local(self):
        self.assertEqual(hw.H_local(2, 2, 2), 1)
        self.assertEqual(hw.H_local(0, 0, 0), 0)
        self.assertEqual(hw.H_local(1, 0, 0), 0)
        self.assertEqual(hw.H_local(1, 0, 1), 0)
        self.assertEqual(hw.H_local(1, 1, 0), 0)
        self.assertEqual(hw.H_local(1, 1, 1), 1)
        self.assertEqual(hw.H_local(2, 3, 3), 0)
        self.assertEqual(hw.H_local(2, 2, 3), 1)
        self.assertEqual(hw.H_local(2, 1, 1), 1)
        self.assertEqual(hw.H_local(2, 3, 2), 1)
        self.assertEqual(hw.H_local(2, 1, 2), 0)

    def test_H_complete(self):
        self.assertEqual(hw.H_complete(0), [[0]])
        self.assertEqual(hw.H_complete(1), [[0, 0], [0, 1]])
        self.assertEqual(hw.H_complete(2), [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]])
        self.assertEqual(hw.H_complete(3), [[0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 1, 0, 1, 0, 1, 0, 1],
                                            [0, 0, 1, 1, 0, 0, 1, 1],
                                            [0, 1, 1, 0, 0, 1, 1, 0],
                                            [0, 0, 0, 0, 1, 1, 1, 1],
                                            [0, 1, 0, 1, 1, 0, 1, 0],
                                            [0, 0, 1, 1, 1, 1, 0, 0],
                                            [0, 1, 1, 0, 1, 0, 0, 1]])

    def test_can_create_once(self):
        self.assertTrue(hw.can_create_once(0, []))
        self.assertFalse(hw.can_create_once(-1, []))
        self.assertTrue(hw.can_create_once(5, [5]))
        self.assertTrue(hw.can_create_once(-5, [5]))
        self.assertTrue(hw.can_create_once(-1, [1, 2]))
        self.assertTrue(hw.can_create_once(6, [5, 2, 3]))
        self.assertTrue(hw.can_create_once(-10, [5, 2, 3]))
        self.assertFalse(hw.can_create_once(9, [5, 2, 3]))
        self.assertFalse(hw.can_create_once(7, [5, 2, 3]))

    def test_can_create_twice(self):
        self.assertTrue(hw.can_create_twice(6, [5, 2, 3]))
        self.assertTrue(hw.can_create_twice(6, [5, 2, 3]))
        self.assertTrue(hw.can_create_twice(9, [5, 2, 3]))
        self.assertTrue(hw.can_create_twice(7, [5, 2, 3]))
        self.assertFalse(hw.can_create_twice(19, [5, 2, 3]))
        self.assertFalse(hw.can_create_twice(2, []))
        self.assertTrue(hw.can_create_twice(0, [4]))
        self.assertTrue(hw.can_create_twice(-4, [4]))
        self.assertTrue(hw.can_create_twice(4, [4]))
        self.assertTrue(hw.can_create_twice(0, []))

    def test_valid_braces_placement(self):
        L = [6, '-', 4, '*', 2, '+', 3]
        L2 = [-4, '*', 4]
        L3 = [1, "*", 1, "*", 1]
        self.assertTrue(hw.valid_braces_placement(10, L))
        self.assertTrue(hw.valid_braces_placement(1, L))
        self.assertFalse(hw.valid_braces_placement(5, L))
        self.assertTrue(hw.valid_braces_placement(-16, L2))
        self.assertFalse(hw.valid_braces_placement(16, L2))
        self.assertTrue(hw.valid_braces_placement(1, L3))
        self.assertFalse(hw.valid_braces_placement(0, L3))

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
        self.assertTrue(hw.grid_escape1(B1))
        self.assertFalse(hw.grid_escape1(B2))
        self.assertFalse(hw.grid_escape1(B3))
        self.assertTrue(hw.grid_escape1(B4))
        self.assertFalse(hw.grid_escape1(B5))
        self.assertFalse(hw.grid_escape1(B6))
        self.assertTrue(hw.grid_escape1(B7))
        self.assertFalse(hw.grid_escape1(B8))
        self.assertFalse(hw.grid_escape1(B9))
        self.assertFalse(hw.grid_escape1(B11))

    def test_grid_escape2_rec(self):
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
        self.assertTrue(hw.grid_escape2(B1))
        self.assertTrue(hw.grid_escape2(B2))
        self.assertFalse(hw.grid_escape2(B3))
        self.assertTrue(hw.grid_escape2(B4))
        self.assertFalse(hw.grid_escape2(B5))
        self.assertFalse(hw.grid_escape2(B6))
        self.assertTrue(hw.grid_escape2(B7))
        self.assertFalse(hw.grid_escape2(B8))
        self.assertFalse(hw.grid_escape2(B9))
        self.assertTrue(hw.grid_escape2(B10))
        self.assertTrue(hw.grid_escape2(B11))
