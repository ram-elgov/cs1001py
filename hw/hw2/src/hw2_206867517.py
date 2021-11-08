# Skeleton file for HW2 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw2_ID.py).
import time
import math
import random  # loads python's random module in order to use random.random() in question 2


##############
# QUESTION 1 #
##############

# 1a
def print_rectangle(length, width):
    result = ""
    for row in range(length):
        for column in range(width):
            if row == 0 or row == length - 1 or column == 0 or column == width - 1:
                result = result + "*"
            else:
                result = result + " "
        if row != length - 1:
            result = result + "\n"
    return result


# 1b
def x_o_winner(board):
    count = 0
    for row in range(3):
        count = 0
        for col in range(3):
            if board[row][col] != "e" and board[row][col] == board[row][0]:
                count += 1
        if count == 3:
            return board[row][0]

    for col in range(3):
        count = 0
        for row in range(3):
            if board[row][col] != "e" and board[row][col] == board[0][col]:
                count += 1
        if count == 3:
            return board[0][col]
        count = 0
    for d1 in range(3):
        if board[0][0] != "e" and board[d1][d1] == board[0][0]:
            count += 1
    if count == 3:
        return board[0][0]
    count = 0
    for d2 in range(3):
        if board[0][2] == "e":
            break
        if board[d2][3 - d2 - 1] == board[0][2]:
            count += 1
    if count == 3:
        return board[0][2]

    return "no winner"


# 1c
def valid_braces(s):
    open_braces_set = {"(", "[", "{"}
    close_braces_set = {")", "]", "}"}
    open_braces_bank = {
        "(": 0,
        "[": 0,
        "{": 0
    }
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    last_seen_open_brace = []
    for char in s:
        if -1 in open_braces_bank.values():
            return False
        if char in open_braces_set:
            last_seen_open_brace.append(char)
            open_braces_bank[char] += 1
        if char in close_braces_set:
            if len(last_seen_open_brace) == 0 or \
                    close_to_open[char] != last_seen_open_brace[len(last_seen_open_brace) - 1]:
                return False
            else:
                open_braces_bank[close_to_open[char]] -= 1
                last_seen_open_brace.pop()
    if sum(open_braces_bank.values()) != 0:
        return False
    return True


##############
# QUESTION 2 #
##############


# 2a
def coin():
    return random.random() > 0.5


# 2b
def roll_dice(d):
    rand = d * random.random()
    return int(rand // 1) + 1


# 2c
def roulette(bet_size, parity):
    result = roll_dice(37) - 1
    if result == 0:
        return 0
    if parity_value(result) == parity:
        return 2 * bet_size
    else:
        return 0


def parity_value(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# 2d
def roulette_repeat(bet_size, n):
    accumulated_profit = 0
    for i in range(n):
        accumulated_profit += (roulette(bet_size, "even") - bet_size) if coin() \
            else (roulette(bet_size, "odd") - bet_size)
    return accumulated_profit


# on the average the player looses his money so it is not lucrative


# 2e
def shuffle_list(lst):
    shuffled_list = lst[:]
    indexes = []

    def random_index(x):
        return roll_dice(x) - 1

    i = 0
    while len(indexes) < len(lst) and i < len(lst):
        index = random_index(len(lst))
        if index not in indexes:
            indexes.append(index)
            shuffled_list[i] = lst[index]
            i += 1
    if indexes == [i for i in range(len(lst))]:  # to prevent getting the same list after a shuffle
        return shuffle_list(lst)
    else:
        return shuffled_list


# 2f
def count_steps(d):
    displacement = 0
    count = 0
    while abs(displacement) != d:
        displacement += 1 if coin() else -1
        count += 1
    return count


def avg_count_steps(d):
    total = 0
    for i in range(100000):
        total += count_steps(d)
    return total / 100000


# 2g
def count_steps_2dim(d):
    x = 0
    y = 0
    count = 0
    while (x**2 + y**2) < d**2:
        count += 1
        step = roll_dice(4)
        if step == 1:
            x += 1
        elif step == 2:
            x -= 1
        elif step == 3:
            y += 1
        else:
            y -= 1

    return count


##############
# QUESTION 3 #
##############


# 3a
def inc(binary):
    carry = True
    binary_list = list(binary)
    for i in range(len(binary_list) - 1, -1, -1):
        if binary_list[i] == "1":
            binary_list[i] = "0"
        else:
            binary_list[i] = "1"
            carry = False
            return "".join(binary_list)
    if carry:
        return "".join(["0" if i > 0 else "1" for i in range(len(binary_list) + 1)])


# 3b
def add(bin1, bin2):
    cary = 0
    result = ""
    max_length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_length)
    bin2 = bin2.zfill(max_length)
    for i in range(max_length - 1, -1, -1):
        if (bin1[i] == "0" and bin2[i] == "1") or (bin1[i] == "1" and bin2[i] == "0"):
            if not cary:
                result += "1"
            else:
                result += "0"
        elif int(bin1[i]) & int(bin2[i]):
            result += "0" if not cary else "1"
            cary = 1
        else:
            if cary:
                result += "1"
                cary = 0
            else:
                result += "0"
    if cary:
        result += "1"
    return "".join(list(result)[::-1])


# 3c
def pow_two(binary, power):
    result = list(binary)[::-1]
    result = "".join(result)
    result = result.zfill(len(binary) + power)
    return "".join(list(result)[::-1])


# 3d
# def div_two(binary, power)
#     result = int(binary)
#     for i in range(power):
#         result //= 10
#         if not result:
#             break
#     return str(result)


# 3e
def leq(bin1, bin2):
    if len(bin1) > len(bin2):
        return False
    if len(bin1) < len(bin2):
        return True
    else:
        for i in range(len(bin1)):
            if bin1[i] != bin2[i]:
                return False
    return True


# 3f
# def to_decimal(binary)
#     decimal_value = 0
#     for i in range(len(binary)):
#         decimal_value += 2**((len(binary) - 1) - i) * int(binary[i])
#     return decimal_value


##############
# QUESTION 5 #
##############


# 5a
def divisors(n):
    return [i + 1 for i in range(n - 1) if n % (i + 1) == 0]


def is_perfect_number(number):
    return sum(divisors(number)) == number


# 5b
def perfect_numbers(n):
    count = 0
    current = 1
    result = []
    while True:
        if count == n:
            break
        if is_perfect_number(current):
            result.append(current)
            count = count + 1
        current = current + 1
    return result


# 5c

def abundant_density(n):
    count = 0
    for i in range(1, n + 1, 1):
        if is_abundant(i):
            count += 1
    return count / n


def is_abundant(number):
    return sum(divisors(number)) > number


# 5e
def semi_perfect_3(n):
    x = divisors(n)
    l = len(x)
    for i in range(l - 2):
        for j in range(i + 1, l - 1, 1):
            for k in range(j + 1, l, 1):
                if x[i] + x[j] + x[k] == n:
                    return [x[i], x[j], x[k]]
    return None


##########
# Tester #
##########

def test():
    # test 1a
    # if print_rectangle(4, 5) != "*****\n*   *\n*   *\n*****" or \
    #         print_rectangle(3, 3) != "***\n* *\n***" or \
    #         print_rectangle(3,2) != "**\n**\n**" or \
    #         print_rectangle(2,3) != "***\n***" or \
    #         print_rectangle(5,3) != "***\n* *\n* *\n* *\n***" or \
    #         print_rectangle(5, 4) != '****\n*  *\n*  *\n*  *\n****' or \
    #         print_rectangle(1,1) != '*' or \
    #         print_rectangle(1,2) != '**' or \
    #         print_rectangle(2,2) != "**\n**":
    #     print("#1a - error in print_rectangle")
    # test 1b
    # if x_o_winner(["eee", "xxx", "eoo"]) != "x" or \
    #         x_o_winner(["xee", "oxo", "eex"]) != "x" or \
    #         x_o_winner(["eex", "oxe", "xoe"]) != "x" or \
    #         x_o_winner(["oee", "oxx", "oeo"]) != "o" or \
    #         x_o_winner(["eee", "eee", "eeo"]) != "no winner" or \
    #         x_o_winner(["xox",
    #                     "oox",
    #                     "xxe"]) != "no winner" or \
    #         x_o_winner(["xox",
    #                     "oxx",
    #                     "xex"]) != "x" or \
    #         x_o_winner(["xoo",
    #                     "oxo",
    #                     "xxx"]) != "x" or \
    #         x_o_winner(["xoo",
    #                     "xox",
    #                     "oex"]) != "o":
    #     print("#1b - error in x_o_winner")
    # test 1c
    # if valid_braces("(ab{cd}ef)") is not True or \
    #         valid_braces("{this(is]wrong") is not False or \
    #         valid_braces("{1:(a,b),2:[c,d)}") is not False or \
    #         valid_braces(".,(:::::::t{t)dd}rr her") is not False or \
    #         valid_braces("hgfsdfgh)h") is not False or \
    #         valid_braces(".{.") is not False or \
    #         valid_braces("sd( .,  (        }::      )") is not False or \
    #         valid_braces("(({.}{}.{,}[][]s(aaa)(a)a{,.[a{}.]}))") is not True or \
    #         valid_braces("([{([{}])}])") is not True or \
    #         valid_braces("{}}") is not False:
    #     print("#1c - error in valid_braces")
    # tests Q2
    # for i in range(10):
    #     if coin() not in {True, False}:
    #         print("#2a - error in coin")
    #         break
    # trues = 0
    # falses =0
    # for i in range(10000000):
    #     if(coin()):
    #         trues += 1
    #     else:
    #         falses +=1
    # print(falses / 10000000, " ", trues / 10000000)

    # for i in range(1000000):
    #     if roll_dice(6) not in {1, 2, 3, 4, 5, 6} or \
    #             roll_dice(100) not in {i for i in range(1, 101)} or \
    #             roll_dice(2) not in {1,2}:
    #         print("2b - error in roll_dice")
    #         break

    # for i in range(10000):
    #     if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
    #         print("2c - error in roulette")
    #         break
    #
    # print(roulette_repeat(100, 10000000) / 10000000)
    # counting = 0
    # for i in range(100000):
    #     if shuffle_list([1, 2, 3, 4]) == [1, 2, 3, 4] or \
    #             shuffle_list(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"] or \
    #             shuffle_list([(1, 2), (3, 4), ("a", "b")]) == [(1, 2), (3, 4), ("a", "b")]:
    #         counting += 1
    #         print("2e - error in shuffle_list")
    # if not 24 < avg_count_steps(5) < 26:  # very low probability that a good implementation will be out of this range
    #     print("2f - error in avg_count_steps")
    # if count_steps_2dim(5) < 5 or \
    #         count_steps_2dim(10) < 10 or \
    #         count_steps_2dim(100) < 100:  # can't reach d in less than d steps
    #     print("2g - error in count_steps_2dim")

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc("1111111") != "10000000" or \
            inc("1110111") != "1111000":
        print("3a - error in inc")
    #
    # if add("0", "1") != "1" or \
    #         add("1", "1") != "10" or \
    #         add("110", "11") != "1001" or \
    #         add("111", "111") != "1110" or \
    #         add("10101010", "11001100") != "101110110" or \
    #         add("0", "10010010010") != "10010010010" or \
    #         add("11111","11111111111") != "100000011110":
    #     print("3b - error in add")
    #
    # if pow_two("10", 2) != "1000" or \
    #         pow_two("111", 3) != "111000" or \
    #         pow_two("101", 1) != "1010":
    #     print("3c - error in pow_two")
    #
    # if div_two("10", 1) != "1" or \
    #         div_two("101", 1) != "10" or \
    #         div_two("1010", 2) != "10" or \
    #         div_two("101010", 3) != "101" or \
    #         div_two("1",10) != "0":
    #     print("3c - error in div_two")
    #
    # if not leq("1010", "1010") or \
    #         leq("1010", "0") or \
    #         leq("1011", "1010") or \
    #         not leq("0", "1010"):
    #     print("3d - error in leq")
    # if to_decimal("100101001110101010101010") != 9759402 or \
    #         to_decimal("0") != 0 or \
    #         to_decimal("1") != 1 or \
    #         to_decimal("10") != 2:
    #     print(print("3f - error in to_decimal"))
    # if divisors(6) != [1, 2, 3] or divisors(7) != [1] or divisors(1) != [] or divisors(24) != [1, 2, 3, 4, 6, 8, 12]:
    #     print("5a - error in divisors")
    #
    # if perfect_numbers(1) != [6] or perfect_numbers(2) != [6, 28] or perfect_numbers(3) != [6, 28,
    #                                                                                         496] or perfect_numbers(
    #         4) != [6, 28, 496, 8128]:
    #     print("5b - error in perfect_numbers")
    #
    # if abundant_density(20) != 0.15 or abundant_density(120) != (28/120):
    #     print("5c - error in adundant_density")
    #
    # if semi_perfect_3(18) != [3, 6, 9] or semi_perfect_3(20) is not None:
    #     print("5e - error in semi_perfect_3")


test()
