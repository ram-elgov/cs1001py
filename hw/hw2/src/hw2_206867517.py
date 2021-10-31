# Skeleton file for HW2 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw2_ID.py).

import random  # loads python's random module in order to use random.random() in question 2

##############
# QUESTION 1 #
##############


# 1a
def print_rectangle(length, width):
    pass  # replace with your code


# 1b
def x_o_winner(board):
    pass  # replace with your code


# 1c
def valid_braces(s):
    pass  # replace with your code


##############
# QUESTION 2 #
##############


# 2a
def coin():
    pass  # replace with your code


# 2b
def roll_dice(d):
    pass  # replace with your code


# 2c
def roulette(bet_size, parity):
    pass  # replace with your code


# 2d
def roulette_repeat(bet_size, n):
    pass  # replace with your code


# 2e
def shuffle_list(lst):
    pass  # replace with your code


# 2f
def count_steps(d):
    pass  # replace with your code


def avg_count_steps(d):
    pass  # replace with your code


#2g
def count_steps_2dim(d):
    pass  # replace with your code


##############
# QUESTION 3 #
##############


# 3a
def inc(binary):
    pass  # replace with your code


# 3b
def add(bin1, bin2):
    pass  # replace with your code


# 3c
def pow_two(binary, power):
    pass  # replace with your code


# 3d
def div_two(binary, power):
    pass  # replace with your code


# 3e
def leq(bin1, bin2):
    pass  # replace with your code


# 3f
def to_decimal(binary):
    pass  # replace with your code


##############
# QUESTION 5 #
##############


# 5a
def divisors(n):
    pass  # replace with your code


# 5b
def perfect_numbers(n):
    pass  # replace with your code


# 5c
def abundant_density(n):
    pass  # replace with your code


# 5e
def semi_perfect_3(n):
    pass  # replace with your code


##########
# Tester #
##########

def test():
    if print_rectangle(4, 5) != "*****\n*   *\n*   *\n*****" or \
       print_rectangle(3, 3) != "***\n* *\n***" or \
       print_rectangle(5, 4) != '****\n*  *\n*  *\n*  *\n****':
        print("#1a - error in print_rectangle")

    if x_o_winner(["eee", "xxx", "eoo"]) != "x" or \
       x_o_winner(["xee", "oxo", "eex"]) != "x" or \
       x_o_winner(["eex", "oxe", "xoe"]) != "x" or \
       x_o_winner(["oee", "oxx", "oeo"]) != "o" or \
       x_o_winner(["eee", "eee", "eeo"]) != "no winner":
        print("#1b - error in x_o_winner")

    if valid_braces("(ab{cd}ef)") is not True or \
       valid_braces("{this(is]wrong") is not False or \
       valid_braces("{1:(a,b),2:[c,d)}") is not False:
        print("#1c - error in valid_braces")

    for i in range(10):
        if coin() not in {True, False}:
            print("#2a - error in coin")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("2b - error in roll_dice")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
            print("2c - error in roulette")
            break

    if shuffle_list([1, 2, 3, 4]) == [1, 2, 3, 4] or \
       shuffle_list(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"] or \
       shuffle_list([(1, 2), (3, 4), ("a", "b")]) == [(1, 2), (3, 4), ("a", "b")]:
        print("2e - error in shuffle_list")

    if not 24 < avg_count_steps(5) < 26:  # very low probability that a good implementation will be out of this range
        print("2f - error in avg_count_steps")

    if count_steps_2dim(5) < 5:  # can't reach d in less than d steps
        print("2g - error in count_steps_2dim")

    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("3a - error in inc")

    if add("0", "1") != "1" or \
       add("1", "1") != "10" or \
       add("110", "11") != "1001" or \
       add("111", "111") != "1110":
        print("3b - error in add")

    if pow_two("10", 2) != "1000" or \
       pow_two("111", 3) != "111000" or \
       pow_two("101", 1) != "1010":
        print("3c - error in pow_two")

    if div_two("10", 1) != "1" or \
       div_two("101", 1) != "10" or \
       div_two("1010", 2) != "10" or \
       div_two("101010", 3) != "101":
        print("3c - error in div_two")

    if not leq("1010", "1010") or \
           leq("1010", "0") or \
           leq("1011", "1010"):
        print("3d - error in leq")

    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("5a - error in divisors")

    if perfect_numbers(2) != [6, 28]:
        print("5b - error in perfect_numbers")

    if abundant_density(20) != 0.15:
        print("5c - error in adundant_density")

    if semi_perfect_3(18) != [3, 6, 9] or semi_perfect_3(20) is not None:
        print("5e - error in semi_perfect_3")