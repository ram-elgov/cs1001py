# Skeleton file for HW5 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).

import math
import random


##############
# QUESTION 2 #
##############


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]

    return C


def is_sorted(lst):  # O(n), n is the length of list P
    """ returns True if lst is sorted, and False otherwise """
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True


def modpower(a, b, c):
    """ computes a**b modulo c, using iterated squaring """
    result = 1
    while b > 0:  # while b is nonzero
        if b % 2 == 1:  # b is odd
            result = (result * a) % c
        a = (a * a) % c
        b = b // 2
    return result


def is_prime(m):  # O(n^3)
    """ probabilistic test for m's compositeness """''
    for i in range(0, 100):
        a = random.randint(1, m - 1)  # a is a random integer in [1...m-1]
        if modpower(a, m - 1, m) != 1:
            return False
    return True


class FactoredInteger:

    def __init__(self, factors, verify=True):
        """ Represents an integer by its prime factorization """
        if verify:
            assert is_sorted(factors)  # O(n)
        number = 1
        for p in factors:
            if verify:
                assert (is_prime(p))  # O(pi^3)
            number *= p
        self.number = number
        self.factors = factors

    # 2b
    def __repr__(self):
        s = ""
        if len(self.factors) > 0:
            for i in range(len(self.factors) - 1):
                s += str(self.factors[i]) + '*'
            s += str(self.factors[-1])
        return "<{0}:{1}>".format(str(self.number), s)

    def __eq__(self, other):
        return isinstance(other, FactoredInteger) and self.number == other.number

    def __mul__(self, other):
        if isinstance(other, FactoredInteger):
            return FactoredInteger(merge(self.factors, other.factors))

    def __pow__(self, other):
        if isinstance(other, FactoredInteger):
            res = []
            for i in range(other.number):
                res = merge(res, self.factors)
            return FactoredInteger(res)

    # 2c
    def gcd(self, other):
        if isinstance(other, FactoredInteger):
            res = []
            if len(other.factors) > len(self.factors):
                long = other.factors
                short = self.factors
            else:
                long = self.factors
                short = other.factors
            i, j = 0, 0
            while i < len(short) and j < len(long):
                short_i, long_j = short[i], long[j]
                if short_i == long_j:
                    res.append(short_i)
                    i += 1
                    j += 1
                elif short_i > long_j:
                    j += 1
                else:
                    i += 1
            return FactoredInteger(res)

    # 2d
    def lcm(self, others):  # others is a list of FactoredIntegers
        my_set = set()
        lists = [self.factors] + [x.factors for x in others]  # O(m)
        f_i_d = [{f: 0 for f in x} for x in lists]  # O(m)
        for i in range(len(lists)):  # O(m) overall iterations
            for f in lists[i]:
                my_set.add(f)  # O(1)
                f_i_d[i][f] += 1  # O(1)
        f_m_d = {x: 0 for x in my_set}  # O(m)
        for f_d in f_i_d:  # O(m) overall iterations
            for f in f_d.keys():
                if f_d[f] > f_m_d[f]:
                    f_m_d[f] = f_d[f]  # O(1)
        result = []
        for k, v in f_m_d.items():  # O(m)
            result += [k] * v
        return FactoredInteger(result)  # O(m^3)


##############
# QUESTION 3 #
##############
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(x ** 2 + y ** 2)
        self.theta = math.atan2(y, x)
        if self.theta < 0:
            self.theta += 2 * math.pi

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # 3a_i
    def angle_between_points(self, other):
        if self.theta > other.theta:
            return 2 * math.pi - (self.theta - other.theta)
        else:
            return other.theta - self.theta


# 3a_ii
def find_optimal_angle(trees, alpha):
    if len(trees) == 0:
        return 0
    sorted_trees = sorted(trees, key=lambda x: x.theta)
    first = 0
    last = -1
    while sorted_trees[first].angle_between_points(sorted_trees[last]) > alpha:
        if sorted_trees[first].angle_between_points(sorted_trees[first + 1]) > \
                sorted_trees[last - 1].angle_between_points(sorted_trees[last]):
            first += 1
        else:
            last -= 1
    return sorted_trees[first].theta


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        # return str(self.value)
        # This shows pointers as well for educational purposes:
        return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list:
    def __init__(self, seq=None):
        self.head = None
        self.len = 0
        if seq is not None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.head
        while p is not None:
            out += str(p) + ", "  # str(p) invokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def __len__(self):
        """ called when using Python's len() """
        return self.len

    def add_at_start(self, val):
        """ add node with value val at the list head """
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        self.len += 1

    def find(self, val):
        """ find (first) node with value val in list """
        p = self.head
        # loc = 0     # in case we want to return the location
        while p is not None:
            if p.value == val:
                return p
            else:
                p = p.next
                # loc=loc+1   # in case we want to return the location
        return None

    def __getitem__(self, loc):
        """ called when using L[i] for reading
            return node at location 0<=loc<len """
        assert 0 <= loc < len(self)
        p = self.head
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        """ called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<len """
        assert 0 <= loc < len(self)
        p = self.head
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def insert(self, loc, val):
        """ add node with value val after location 0<=loc<len of the list """
        assert 0 <= loc <= len(self)
        if loc == 0:
            self.add_at_start(val)
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            tmp = p.next
            p.next = Node(val)
            p.next.next = tmp
            self.len += 1

    def delete(self, loc):
        """ delete element at location 0<=loc<len """
        assert 0 <= loc < len(self)
        if loc == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            # p is the element BEFORE loc
            p.next = p.next.next
        self.len -= 1


class Segment:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def intersecting(self, other):
        if (self.point1.x - self.point2.x) == 0:
            return False
        if (other.point1.x - other.point2.x) == 0:
            return False
        self_incline = (self.point1.y - self.point2.y) / (self.point1.x - self.point2.x)
        other_incline = (other.point1.y - other.point2.y) / (other.point1.x - other.point2.x)
        self_b = self.point1.y - self_incline * self.point1.x
        other_b = other.point1.y - other_incline * other.point1.x
        if (self_incline - other_incline) == 0:
            return False
        intersecting_x = (other_b - self_b) / (self_incline - other_incline)
        if ((intersecting_x <= max(min(self.point1.x, self.point2.x), min(other.point1.x, other.point2.x))) or
                (intersecting_x >= min(max(self.point1.x, self.point2.x), max(other.point1.x, other.point2.x)))):
            return False
        else:
            return True


# for 3b_ii
def calculate_angle(p1, p2, p3):
    ang = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    return ang + 360 if ang < 0 else ang


class Polygon:
    def __init__(self, llist):
        self.points_list = llist
        self.point_head = llist.head

    # 3b_ii
    def edges(self):
        angles = []
        curr = self.point_head
        left = curr.next
        right = self.point_head
        while right.next is not None:
            right = right.next
        while left is not None:
            angles.append(calculate_angle(right.value, curr.value, left.value))
            left = left.next
            right = curr
            curr = curr.next
        angles.append(calculate_angle(right.value, curr.value, self.point_head.value))
        if sum(angles) > 180 * (len(angles) - 2):
            for i in range(len(angles)):
                angles[i] = 360 - angles[i]
        return angles

    # 3b_iii
    def simple(self):
        segment_set = set()
        from_point = self.point_head
        if self.point_head is None or self.point_head.next is None:
            return False
        to_point = self.point_head.next
        while to_point is not None:
            segment_set.add(Segment(from_point.value, to_point.value))
            to_point = to_point.next
            from_point = from_point.next
        segment_set.add(Segment(from_point.value, self.point_head.value))

        not_simple = 0
        for s in segment_set:
            for k in segment_set:
                if s.intersecting(k):
                    not_simple = 1
                    break
            if not_simple:
                return False
        return True


##############
# QUESTION 4 #
##############


def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t is None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.right), height(root.left))


def diam_rec(root, diam):
    if root is None:
        return 0, diam
    h_left, diam_left = diam_rec(root.left, diam)
    h_right, diam_right = diam_rec(root.right, diam)

    diam = max(h_left + h_right + 1, max(diam_left, diam_right))
    return max(h_left, h_right) + 1, diam


class Tree_node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree:

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def inorder(self):
        result = []

        def inorder_rec(root):
            if root:
                inorder_rec(root.left)
                result.append((root.key, root.val))
                inorder_rec(root.right)

        inorder_rec(self.root)
        return result

    def lookup(self, key):
        """ return node with key, uses recursion """

        def lookup_rec(node, key):
            if node is None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        """ insert node with key,val into tree, uses recursion """

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left is None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right is None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root is None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    # 4a
    def diam(self):
        return diam_rec(self.root, 0)[1]

    # 4b
    def cumsum(self):
        s = []

        def cumsum_rec(root, st):
            if root is None:
                return
            cumsum_rec(root.left, st)
            st.append(root.key)
            root.key = "".join(st)
            cumsum_rec(root.right, st)

        return cumsum_rec(self.root, s)


############
# QUESTION 5
############

# 5a
def overlap(s1, s2, k):
    for i in range(k):
        if s1[i] != s2[len(s2) - k + i]:
            return False
    return True


def prefix_suffix_overlap(lst, k):
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(n):
            if i != j:
                if overlap(lst[i], lst[j], k):
                    res.append((i, j))
    return res


# 5c
class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):  # O(k)
        """ returns ALL values of key as a list, empty list if none """
        res = []
        for entity in self.table[self.hash_mod(key)]:  # O(1) because by the assumptions there can be only 1 string
            # with the corresponding key (prefix)
            if key == entity[0]:  # O(k)
                res.append(entity[1])  # O(1)
        return res


# 5d
def init_prefix_dict(lst, k, n, dict):
    for i in range(n):  # O(n)
        dict.insert(lst[i][:k], i)  # O(k) as hashing takes O(k)


def overlaps(lst, k, n, dict):  # o(nk)
    res = []
    for j in range(n):  # O(n)
        suffix = lst[j][(len(lst[j]) - k):]  # O(1)
        sj_matches = dict.find(suffix)  # list of indices with si's whose prefix equals sj suffix, O(k).
        for i in sj_matches:  # O(1)
            if i != j:  # never executed because by the assumptions there are no overlaps.
                if overlap(lst[i], lst[j], k):
                    res.append((i, j))
    return res


def prefix_suffix_overlap_hash1(lst, k):  # O(nk)
    n = len(lst)
    dict = Dict(n // 2)  # O(n)
    init_prefix_dict(lst, k, n, dict)  # O(nk)
    return overlaps(lst, k, n, dict)  # O(nk)


##########
# TESTER #
##########

def test():
    ##############
    # QUESTION 2 #
    #   TESTER   #
    ##############

    # 2b
    n1 = FactoredInteger([2, 3])  # n1.number = 6
    n2 = FactoredInteger([2, 5])  # n2.number = 10
    n3 = FactoredInteger([2, 2, 3, 5])  # n3.number = 60
    n4 = FactoredInteger([31])  # n4.number = 31
    if str(n3) != "<60:2*2*3*5>" or str(n1) != "<6:2*3>" or str(n2) != "<10:2*5>" or str(n4) != "<31:31>":
        print("2b - error in __repr__")
    if n1 != FactoredInteger([2, 3]):
        print("2b - error in __eq__")
    if n1 * n2 != n3:
        print("2b - error in __mul__")
    if n1 ** n2 != FactoredInteger([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]):
        print("2b - error in __pow__")

    # 2c
    n4 = FactoredInteger([2, 2, 3])  # n4.number = 12
    n5 = FactoredInteger([2, 2, 2])  # n5.number = 8
    n6 = FactoredInteger([2, 2])  # n6.number = 4
    n7 = FactoredInteger([13])
    n8 = FactoredInteger([47])
    empty = FactoredInteger([])
    n9 = FactoredInteger([2, 2, 2, 2, 2])
    n10 = FactoredInteger([2, 2, 2])
    if n4.gcd(n5) != n6 or n7.gcd(n8) != empty or n9.gcd(n10) != n5 or empty.gcd(n9) != empty:
        print("2c - error in gcd")
    n7 = FactoredInteger([2, 3])  # n7.number = 6
    n8 = FactoredInteger([5, 7])  # n8.number = 35
    n9 = FactoredInteger([])  # represents 1
    if n7.gcd(n8) != n9:
        print("2c - error in gcd")
    ##############
    # QUESTION 3 #
    #   TESTER   #
    ##############

    # 3a
    p1 = Point(1, 1)  # theta = pi / 4
    p2 = Point(0, 3)  # theta = pi / 2
    if Point.angle_between_points(p1, p2) != 0.25 * math.pi or \
            Point.angle_between_points(p2, p1) != 1.75 * math.pi or Point.angle_between_points(p2, p2) != 0:
        print("3a_i - error in angle_between_points")

    trees1 = [Point(1, 1)]
    trees2 = [Point(1, 1), Point(-1, 1)]
    trees = [Point(2, 1), Point(-1, 1), Point(-1, -1), Point(0, 3), Point(0, -5), Point(-1, 3)]
    if find_optimal_angle(trees, 0.25 * math.pi) != 0.5 * math.pi or \
            find_optimal_angle(trees1, 0.25 * math.pi) != 0.25 * math.pi or \
            find_optimal_angle(trees2, 0.25 * math.pi) != 0.25 * math.pi or \
            find_optimal_angle([], 0.5 * math.pi) != 0:
        print("3a_ii - error in find_optimal_angle")

    # 3b
    def test_angles(target, output):
        if len(target) != len(output):
            print("3a_ii - error in Polygon.edges")
        for i in range(len(target)):
            if abs(target[i] - output[i]) >= 0.1:  # dealing with floats
                print("3a_ii - error in Polygon.edges")

    parallelogram = Polygon(Linked_list([Point(1, 1), Point(4, 4), Point(8, 4), Point(5, 1)]))
    test_angles(parallelogram.edges(), [45.0, 135.0, 45.0, 135.0])
    parallelogram1 = Polygon(Linked_list([Point(4, 4), Point(8, 4), Point(5, 1), Point(1, 1)]))
    test_angles(parallelogram1.edges(), [135.0, 45.0, 135.0, 45.0])
    parallelogram_reverse = Polygon(Linked_list([Point(5, 1), Point(8, 4), Point(4, 4), Point(1, 1)]))
    test_angles(parallelogram_reverse.edges(), [135.0, 45.0, 135.0, 45.0])
    parallelogram_counter = Polygon(Linked_list([Point(1, 1), Point(5, 1), Point(8, 4), Point(4, 4)]))
    test_angles(parallelogram_counter.edges(), [45.0, 135.0, 45.0, 135.0])
    other_poly = Polygon(Linked_list([Point(1, 1), Point(1, 3), Point(2, 3), Point(3, 1)]))
    test_angles(other_poly.edges(), [90.0, 90.0, 116.5, 63.4])
    other_poly1 = Polygon(Linked_list([Point(2, 3), Point(3, 1), Point(1, 1), Point(1, 3)]))
    test_angles(other_poly1.edges(), [116.5, 63.4, 90.0, 90.0])
    triangle = Polygon(Linked_list([Point(0, 0), Point(0, 1), Point(1, 1)]))
    test_angles(triangle.edges(), [45.0, 90.0, 45.0])
    triangle2 = Polygon(Linked_list([Point(0, 0), Point(1, 0), Point(1, 1)]))
    test_angles(triangle2.edges(), [45.0, 90.0, 45.0])

    not_simple = Polygon(Linked_list([Point(1, 1), Point(8, 4), Point(4, 4), Point(5, 1)]))
    not_simple2 = Polygon(Linked_list([Point(1, 3), Point(2, 5), Point(1.5, 0), Point(3, 3)]))
    not_simple_with_doubling = Polygon(Linked_list([Point(1, 1), Point(8, 4), Point(4, 4), Point(1, 1), Point(4, 4),
                                                    Point(5, 1)]))
    if not_simple.simple():
        print("3a_iii - error in Polygon.simple")
    if not parallelogram.simple():
        print("3a_iii - error in Polygon.simple")
    if not other_poly.simple():
        print("3a_iii - error in Polygon.simple")
    if not_simple2.simple():
        print("3a_iii - error in Polygon.simple")
    if not_simple_with_doubling.simple():
        print("3a_iii - error in Polygon.simple")

    ##############
    # QUESTION 4 #
    #   TESTER   #
    ##############

    # 4a
    t1 = Binary_search_tree()
    t1.insert('e', 10)
    t1.insert('c', 10)
    t1.insert('g', 10)
    t1.insert('z', 10)
    if t1.diam() != 4:
        print("4a - error in diam")

    t2 = Binary_search_tree()
    t2.insert('c', 10)
    t2.insert('a', 10)
    t2.insert('b', 10)
    t2.insert('g', 10)
    t2.insert('e', 10)
    t2.insert('d', 10)
    t2.insert('f', 10)
    t2.insert('h', 10)
    if t2.diam() != 6:
        print("4a - error in diam")

    t3 = Binary_search_tree()
    t3.insert('c', 1)
    t3.insert('g', 3)
    t3.insert('e', 5)
    t3.insert('d', 7)
    t3.insert('f', 8)
    t3.insert('h', 6)
    t3.insert('z', 6)
    if t3.diam() != 5:
        print("4a - error in diam")

    empty_tree = Binary_search_tree()
    if empty_tree.diam() != 0:
        print("4a - error in diam")

    uni_tree = Binary_search_tree()
    uni_tree.insert('a', 10)
    if uni_tree.diam() != 1:
        print("4a - error in diam")

    # 4b
    t3.cumsum()
    if str(t3.inorder()) != "[('c', 1), ('cd', 7), ('cde', 5), ('cdef', 8), ('cdefg', 3), ('cdefgh', 6), ('cdefghz', " \
                            "6)]":
        print("4b - error in cumsum")
    t2.cumsum()
    if str(t2.inorder()) != "[('a', 10), ('ab', 10), ('abc', 10), ('abcd', 10), ('abcde', 10), ('abcdef', 10), " \
                            "('abcdefg', 10), ('abcdefgh', 10)]":
        print("4b - error in cumsum")

    t1.cumsum()
    if str(t1.inorder()) != "[('c', 10), ('ce', 10), ('ceg', 10), ('cegz', 10)]":
        print("4b - error in cumsum")

    empty_tree.cumsum()
    if str(empty_tree.inorder()) != "[]":
        print("4b - error in cumsum")

    uni_tree.cumsum()
    if str(uni_tree.inorder()) != "[('a', 10)]":
        print("4b - error in cumsum")

    ##############
    # QUESTION 5 #
    #   TESTER   #
    ##############
    # 5a
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap")

    # 5c
    d = Dict(3)
    d.insert("a", 56)
    d.insert("a", 34)

    if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
        print("error in Dict.find")
    # 5d
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap_hash1")