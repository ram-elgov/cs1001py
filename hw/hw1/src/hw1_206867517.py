# Skeleton file for HW1 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw1_ID.py).


# Question 4a
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars_counter = [0 for i in range(26)]
    if len(text) == 0:  # treating the case of an empty string
        return 0

    for i in range(len(text)):
        if text[i] in chars:
            chars_counter[chars.find(text[i])] = 1
    return sum(chars_counter)

# Question 4b
def replace_char(text, old, new):
    pass  # replace with your implementation


# Question 4c
def longest_word(text):
    pass  # replace with your implementation


# Question 4d
def to_upper(text):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pass  # replace with your implementation


# Question 5
def calc(expression):
    pass  # replace with your implementation


########
# Tester
########

def test():
    # testing Q4
    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")
    if num_different_letters("aaa98765432100000000") != 1:
        print("error in num_different_letters - 2")
    if num_different_letters("") != 0:
        print("error in num_different_letters - 3")

    # if replace_char("abcdabcde", "a", "x") != "xbcdxbcde":
    #     print("error in replace_char - 1")
    # if replace_char("abcd123", "1", "x") != "abcdx23":
    #     print("error in replace_char - 2")
    #
    # if longest_word("a bb ccc 4444 e") != 4:
    #     print("error in longest_word - 1")
    # if longest_word("a bb ccc 4444 eeeee fffff") != 5:
    #     print("error in longest_word - 2")
    #
    # if to_upper("abc") != "ABC":
    #     print("error in to_upper - 1")
    # if to_upper("123") != "123":
    #     print("error in to_upper - 2")
    #
    # # testing Q5
    # if calc("'123321'*'2'") != "123321123321":
    #     print("error in calc - 1")
    # if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
    #     print("error in calc - 2")
    # if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
    #     print("error in calc - 3")
    # if calc("'a'*'2'+'b'*'2'") != "aabaab":
    #     print("error in calc - 4")


test()