# Skeleton file for HW3 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).
import math
import random


# Q2 - C
def bin_to_fraction(binary):
    result = 0
    for i in range(len(binary)):
        result += int(binary[i]) * 2 ** (-i - 1)
    return result


# Q2 - D
bin_to_float = lambda binary: (-1) ** int(binary[0], 2) * (2 ** ((int(binary[1:9], 2)) - 127)) * (
        1 + bin_to_fraction(binary[9:]))


# Q2 - E
def is_greater_equal(bin1, bin2):
    if bin1[0] == "1" and bin2 == "0":
        return False
    exp1, exp2 = 0, 0
    fraction_plus_one1, fraction_plus_one2 = 1.0, 1.0
    for i in range(1, 9):
        digit1 = 1 if bin1[i] == "1" else 0
        digit2 = 1 if bin2[i] == "1" else 0
        exp1 += digit1 * 2 ** (7 - (i - 1))
        exp2 += digit2 * 2 ** (7 - (i - 1))
    for i in range(9, 32):
        fraction_plus_one1 += 2 ** (8 - i) if bin1[i] == "1" else 0
        fraction_plus_one2 += 2 ** (8 - i) if bin2[i] == "1" else 0
    sign1 = 1 if bin1[0] == "1" else 0
    sign2 = 1 if bin2[0] == "1" else 0
    return ((-1) ** sign1) * (2 ** (exp1 - 127)) * fraction_plus_one1 >= \
           ((-1) ** sign2) * (2 ** (exp2 - 127)) * fraction_plus_one2


# Q3 - A
def approx_root(x, e):
    approx = 0  # the current approximation
    lst = [1]  # list of a_1,a_2,...,a_n
    product = 1  # a_1*a_2*...*a_k
    while x >= (approx + e) * (approx + e):  # check error condition
        n = lst[len(lst) - 1]  # set n to be a_n (invariant - a_n-1 <= a_n)
        while (approx + 1 / (product * n)) * (approx + 1 / (product * n)) > x:  # check the approximation from below
            # condition
            n += 1
        approx += 1 / (product * n)  # calculate new approximation
        lst.append(n)  # n -> a_n
        product = product * n  # update product
    return lst[1:], approx  # remove the first redundant "1" before return


# Q3 - B
def approx_e(N):
    sum_of_N_games = 0
    for i in range(N):
        sum_of_N_games += approx_game()
    return sum_of_N_games / N


def approx_game():
    sum_of_r = 0
    n = 0
    while sum_of_r <= 1:
        n += 1
        sum_of_r += random.random()
    return n


# Q4 - A
def find(lst, s):
    n = len(lst)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2  # middle rounded down
        if s == lst[mid]:  # item found
            return mid
        if mid > 0 and lst[mid - 1] == s:  # item found
            return mid - 1
        if mid < n - 1 and lst[mid + 1] == s:  # item found
            return mid + 1
        if s < lst[mid]:  # item cannot be in top half (and not in midi's left adjacent)
            right = mid - 2
        else:  # item cannot be in bottom half  (and not in midi's right adjacent)
            left = mid + 2
    return None


# Q4 - B
def sort_from_almost(lst):
    """ sorts an almost sorted array inplace. time: O(n), memory: O(1) """
    if len(lst) != 0:
        for i in range(len(lst) - 1):  # O(n) time
            if lst[i] > lst[i + 1]:
                swap(lst, i, i + 1)  # O(1) time O(1) memory
    return lst


def swap(lst, i1, i2):
    """ swaps items in given indexes inplace. time: O(1), memory: O(1) """
    temp = lst[i2]
    lst[i2] = lst[i1]
    lst[i1] = temp


# Q4 - C
def find_local_min(lst):
    """ input: non empty list return: a local minima index """
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (right + left) // 2
        if ((mid == 0 or lst[mid - 1] >= lst[mid]) and
                (mid == len(lst) - 1 or lst[mid] <= lst[mid + 1])):
            return mid
        elif mid < len(lst) - 1 and lst[mid + 1] < lst[mid]:
            left = mid + 1
        elif mid > 0 and lst[mid - 1] < lst[mid]:
            right = mid - 1


# Q5 - A
def string_to_int(s):
    k = len(s)
    d = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
    }
    code = 0
    for i in range(k):
        code += d[s[i]] * (5 ** (k - i - 1))
    return code


# Q5 - B
def int_to_string(k, n):
    d = {
        "e": 4,
        "d": 3,
        "c": 2,
        "b": 1,
        "a": 0,
    }
    s = ""
    for i in range(k):
        for word in d:
            exp = d[word] * (5 ** (k - i - 1))
            if exp <= n:
                s += word
                if word != "a":
                    n -= exp
                break
    return s


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
    # if bin_to_fraction('01101') != 0.40625 or bin_to_fraction('1010000') != 0.625:
    #     print('error in bin_to_fraction')
    # Q2 - D
    # if bin_to_float('00111110001000000000000000000000') != 0.15625:
    #     print("error in bin_to_float")
    # # Q2 - E
    # if is_greater_equal('00111110001000000000000000000000', '00111111001000000000000000000000') == True or \
    #         is_greater_equal('00111110001000000000000000000000', '00111110001000000000000000000000') == False:
    #     print("error in is_greater_equal")
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
    # Q4 - A
    # almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    # if find(almost_sorted_lst, 5) != 3:
    #     print("error in find")
    # if find(almost_sorted_lst, 50) is not None:
    #     print("error in find")
    # # Q4 - B
    # if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst) or \
    #         not (sort_from_almost(almost_sorted_lst) is almost_sorted_lst):
    #     print("error in sort_from_almost")

    # Q4 - C
    # lst = [5, 6, 7, 5, 1, 1, 99, 100]
    # pos = find_local_min(lst)
    # if pos not in (0, 4, 5):
    #     print("error in find_local_min")

    # Q5
    lst_num = [random.choice(range(5 ** 4)) for _ in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")
    for i in range(5 ** 3):
        if string_to_int(int_to_string(3, i)) != i:
            print("Problem with ", i)
    alphabet = ["a", "b", "c", "d", "e"]
    lst = [x + y + z for x in alphabet for y in alphabet for z in alphabet]
    for item in lst:
        if int_to_string(3, string_to_int(item)) != item:
            print("Problem with ", item)

    # lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    # if sort_strings1(lst1, 4) \
    #         != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
    #     print("error in sort_strings1")
    #
    # if sort_strings2(lst1, 4) \
    #         != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
    #     print("error in sort_strings2")


test()
