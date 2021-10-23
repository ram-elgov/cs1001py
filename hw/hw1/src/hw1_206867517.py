# hw1 solution
# id: 206867517

# Question 4a
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars_counter = [0 for i in range(26)]
    if len(text) == 0:  # in case of an empty string
        return 0
    for i in range(len(text)):
        if text[i] in chars:
            chars_counter[chars.find(text[i])] = 1
    return sum(chars_counter)


# Question 4b
def replace_char(text, old, new):
    if len(text) == 0:  # in case of an empty string
        if old == '':
            return text + new
    text_clone = ""
    for i in range(len(text)):
        if text[i] == old:
            text_clone += new
        else:
            text_clone += text[i]
    return text_clone


# Question 4c
def longest_word(text):
    if len(text) == 0:  # in case of an empty string
        return 0
    words = text.split()
    longest_word_value = 0
    for word in words:
        if len(word) > longest_word_value:
            longest_word_value = len(word)
    return longest_word_value


# Question 4d
def to_upper(text):
    if len(text) == 0:  # in case of an empty string
        return ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_clone = ""

    for i in range(len(text)):
        if text[i] in lower:
            for j in range(len(lower)):
                if text[i] == lower[j]:
                    text_clone += upper[j]
                    break
        else:
            text_clone += text[i]
    return text_clone


# Question 5
def calc(expression):
    if len(expression) == 0:
        return ""
    expression_list = str.split(expression[1:len(expression) - 1], "'")
    if len(expression_list) == 1:
        return expression_list[0]
    i = 3
    l_op = calc_operation(expression_list[0], expression_list[1], expression_list[2])
    while i < len(expression_list) - 1:
        operator = expression_list[i]
        r_op = expression_list[i + 1]
        l_op = calc_operation(l_op, operator, r_op)
        i += 2
    return l_op


def calc_operation(left_operand, operation, right_operand):
    return left_operand + right_operand if operation == '+' else left_operand * int(right_operand)


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
    if num_different_letters("012345678910*/-+") != 0:
        print("error in num_different_letters - 4")
    if num_different_letters("abcdefghijklmnopqrstuvwxyz0123456789") != 26:
        print("error in num_different_letters - 5")

    if replace_char("abcdabcde", "a", "x") != "xbcdxbcde":
        print("error in replace_char - 1")
    if replace_char("abcd123", "1", "x") != "abcdx23":
        print("error in replace_char - 2")
    if replace_char("", " ", "$") != "":
        print("error in replace_char - 3")
    if replace_char("", "", "$") != "$":
        print("error in replace_char - 4")
    if replace_char("xxxxx", "x", "$") != "$$$$$":
        print("error in replace_char - 5")
    if replace_char("xxxx", "x", "") != "":
        print("error in replace_char - 6")

    # comparing to built-in str.replace()
    if replace_char("abcdabcde", "a", "x") != str.replace("abcdabcde", "a", "x"):
        print("error in replace_char - 1")
    if replace_char("abcd123", "1", "x") != str.replace("abcd123", "1", "x"):
        print("error in replace_char - 2")
    if replace_char("", " ", "$") != str.replace("", " ", "$"):
        print("error in replace_char - 3")
    if replace_char("", "", "$") != str.replace("", "", "$"):
        print("error in replace_char - 4")
    if replace_char("xxxxx", 'x', '$') != str.replace("xxxxx", "x", "$"):
        print("error in replace_char - 5")

    if longest_word("a bb ccc 4444 e") != 4:
        print("error in longest_word - 1")
    if longest_word("a bb ccc 4444 eeeee fffff") != 5:
        print("error in longest_word - 2")
    if longest_word("") != 0:
        print("error in longest_word - 3")
    if longest_word("asfkj 00 12345678$ 1 00") != 9:
        print("error in longest_word - 4")
    if longest_word("        ") != 0:
        print("error in longest_word - 5")
    if longest_word("dssdf  ' sfsf' ff   f") != 5:
        print("error in longest_word - 6")
    if longest_word("abcd xyz") != 4:
        print("error in longest_word - 7")
    if longest_word("a 12b 34cd 5678efg zzz") != 7:
        print("error in longest_word - 8")

    if to_upper("abc") != "ABC":
        print("error in to_upper - 1")
    if to_upper("123") != "123":
        print("error in to_upper - 2")
    if to_upper("1bc") != "1BC":
        print("error in to_upper - 3")
    if to_upper("") != "":
        print("error in to_upper - 4")
    if to_upper("a a") != "A A":
        print("error in to_upper - 5")
    if to_upper("12 3") != "12 3":
        print("error in to_upper - 6")
    if to_upper("ABC") != "ABC":
        print("error in to_upper - 7")
    if to_upper("1 a") != "1 A":
        print("error in to_upper - 8")

    # testing Q5
    if calc("'123321'*'2'") != eval("'123321'*2"):  # "123321123321"
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != eval("'Hi there '*3+'you2'"):  # "Hi there Hi there Hi there you2"
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != eval("'hi+fi'*2*2"):  # "hi+fihi+fihi+fihi+fi"
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != eval("('a'* 2 +'b') * 2"):  # "aabaab"
        print("error in calc - 4")
    if calc("") != "":
        print("error in calc - 5")
    if calc("''") != eval("''"):  # """
        print("error in calc - 6")
    if calc("'2'*'2'*'2'") != eval("'2'*2*2"):  # "2222"
        print("error in calc - 7")
    if calc("'+*'+'*+'*'2'") != eval("('+*'+'*+')*2"):  # +**++**+"
        print("error in calc - 8")


test()
