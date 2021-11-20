# Skeleton file for HW3 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).
import math
import random

# Q2 - C
def bin_to_fraction(binary):
    pass  # replace this with your code


# Q2 - D
bin_to_float = lambda binary: None # replace None with your code


# Q2 - E
def is_greater_equal(bin1, bin2):
    pass  # replace this with your code


# Q3 - A
def approx_root(x, e):
    pass  # replace this with your code


# Q3 - B
def approx_e(N):
    pass  # replace this with your code


# Q4 - A
def find(lst, s):
    pass  # replace this with your code


# Q4 - B
def sort_from_almost(lst):
    pass  # replace this with your code


# Q4 - C
def find_local_min(lst):
    pass  # replace this with your code


# Q5 - A
def string_to_int(s):
    pass  # replace this with your code


# Q5 - B
def int_to_string(k, n):
    pass  # replace this with your code


# Q5 - C
def sort_strings1(lst, k):
    pass  # replace this with your code


# Q5 - E
def sort_strings2(lst, k):
    pass  # replace this with your code


##########
# Tester #
##########
def test():
    # Q2 - C
    if bin_to_fraction('01101') != 0.40625 or bin_to_fraction('1010000') != 0.625:
        print('error in bin_to_fraction')
    # Q2 - D
    if bin_to_float('00111110001000000000000000000000') != 0.15625:
        print("error in bin_to_float")
    # Q2 - E
    if is_greater_equal('00111110001000000000000000000000', '00111111001000000000000000000000') == True or \
       is_greater_equal('00111110001000000000000000000000', '00111110001000000000000000000000') == False:
        print("error in is_greater_equal")
    # Q3 - A
    if approx_root(2, 0.1) != ([1, 3], 1 + 1/3):
        print("error in approx_root (1)")
    if approx_root(2, 0.02) != ([1, 3, 5], 1 + 1/3 + 1/15):
        print("error in approx_root (2)")
    if approx_root(2, 0.001) != ([1, 3, 5, 5], 1 + 1/3 + 1/15 + 1/75):
        print("error in approx_root (3)")
    # Q3 - B
    if abs(approx_e(1000000) - math.e) > 0.01:
        print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")

    # Q4 - A
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    if find(almost_sorted_lst, 5) != 3:
        print("error in find")
    if find(almost_sorted_lst, 50) != None:
        print("error in find")
    # Q4 - B
    if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        print("error in sort_from_almost")
    # Q4 - C
    lst = [5, 6, 7, 5, 1, 1, 99, 100]
    pos = find_local_min(lst)
    if pos not in (0, 4, 5):
        print("error in find_local_min")

    # Q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")