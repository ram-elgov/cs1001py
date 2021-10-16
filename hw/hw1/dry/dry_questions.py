""" Question 1 - solution """
"""
my_string = "xyzw"
my_list = ['x','y','z','w']

# string but not list functions

print(str.capitalize(my_string))  # first method
print(my_string.capitalize())     # second method

print(str.replace(my_string, "xy","<(^__^)>"))  # first method
print(my_string.replace("xy","<(^__^)>"))       # second method

print(str.istitle(my_string))  # first method
print(my_string.istitle())     # second method

print("\n")

# list but not string functions

print(list.pop(my_list),)    # first method
my_list = ['x','y','z','w']  # pop() is inplace
print(my_list.pop())         # second method

list.clear(my_list)            # first method
print(my_list)
my_list = ['x','y','z','w']    # clear() is inplace
my_list.clear()                # second method\
print(my_list)
my_list = ['x','y','z','w']    # clear() is inplace


list.insert(my_list, 3, "<(^__^)>")    # first method
print(my_list)
my_list = ['x','y','z','w']            # insert() is inplace
my_list.insert(3, "<(^__^)>")          # second method
print(my_list)

"""

