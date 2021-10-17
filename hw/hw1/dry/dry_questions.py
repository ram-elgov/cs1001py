import time

""" Question 1 - solution """
#
# my_string = "xyzw"
# my_list = ['x','y','z','w']
#
# # string but not list functions
#
# print(str.capitalize(my_string))  # first method
# print(my_string.capitalize())     # second method
#
# print(str.replace(my_string, "xy","<(^__^)>"))  # first method
# print(my_string.replace("xy","<(^__^)>"))       # second method
#
# print(str.istitle(my_string))  # first method
# print(my_string.istitle())     # second method
#
# print("\n")
#
# # list but not string functions
#
# print(list.pop(my_list),)    # first method
# my_list = ['x','y','z','w']  # pop() is inplace
# print(my_list.pop())         # second method
#
# list.clear(my_list)            # first method
# print(my_list)
# my_list = ['x','y','z','w']    # clear() is inplace
# my_list.clear()                # second method\
# print(my_list)
# my_list = ['x','y','z','w']    # clear() is inplace
#
#
# list.insert(my_list, 3, "<(^__^)>")    # first method
# print(my_list)
# my_list = ['x','y','z','w']            # insert() is inplace
# my_list.insert(3, "<(^__^)>")          # second method
# print(my_list)
#


""" Question 2 - solution """
# def control_digit(israeli_id):
#     """
#     compute the check digit in an Israeli ID number,
#     given as a string of 8 digits.
#     :param israeli_id: Israeli ID number
#     :return: check digit
#     """
#     assert isinstance(israeli_id, str)
#     assert len(israeli_id) == 8
#
#     total = 0
#     for i in range(8):
#         idi = israeli_id[i]
#         val = int(israeli_id[i])  # converts chart to int
#         if i % 2 == 0:            # even index (0,2,4,6)
#             total += val
#         else:                     # odd index (1,3,5,7)
#             if val < 5:
#                 total += 2 * val
#             else:
#                 total += ((2 * val) % 10) + 1  # sum of digits in 2*val. 'tens' digits must be 1
#     total = total % 10                         # 'ones' (rightmost) digit
#     check_digit = (10 - total) % 10            # the complement modulo 10 of total
#
#     return str(check_digit)
#
#
# control_digit("20686751")

""" Question 3 - solution """


def zeros(num):  # 1st solution
    m = num
    cnt = 0
    while m > 0:
        if m % 10 == 0:
            cnt = cnt + 1
        m = m // 10
    return cnt


def zeros2(num):  # 2nd solution
    cnt = 0
    snum = str(num)  # num as a string
    for digit in snum:
        if digit == "0":
            cnt = cnt + 1
    return cnt


def zeros3(num):  # 3rd solution
    cnt = str.count(str(num), "0")
    return cnt


num = 2 ** 1400
t0 = time.perf_counter()
zeros3(num)
t1 = time.perf_counter()
print("Running time: ", t1 - t0, "sec")

