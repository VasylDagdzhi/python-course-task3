import builtins

print("\r\n Part 1.\n")

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(f"ID of int_a is: {id(int_a)} and value is: {int_a}")
print(f"ID of str_b is: {id(str_b)} and value is: {str_b}")
print(f"ID of set_c is: {id(set_c)} and value is: {set_c}")
print(f"ID of lst_d is: {id(lst_d)} and value is: {lst_d}")
print(f"ID of dict_e is: {id(dict_e)} and value is: {dict_e}")

print("\r\n Part 2.")

lst_d.append(4)
lst_d.append(5)
print(f"\r\nID of lst_d now is: {id(lst_d)} and values inside were changed to: {lst_d}")

print("\r\n Part 3.\n")

print(f"Type of int_a is: {type(int_a)}")
print(f"Type of str_b is: {type(str_b)}")
print(f"Type of set_c is: {type(set_c)}")
print(f"Type of lst_d is: {type(lst_d)}")
print(f"Type of dict_e is: {type(dict_e)}")

print(isinstance(int_a, str))

print("\r\n Part 4.\n")

# we get the list of all types available in Python and place them in a list
builtin_types = [getattr(builtins, i) for i in dir(builtins) if isinstance(getattr(builtins, i), type)]
# since all the variable types are also objects we remove the type 'object' from the list to leave only exact types
builtin_types.remove(builtins.object)
# next we check with isinstance each of our variables in a cycle to determine which type they are
for i in builtin_types:
    if isinstance(int_a, i):
        print(f"int_a is a type of: {i} \r")
    if isinstance(str_b, i):
        print(f"str_b is a type of: {i} \r")
    if isinstance(set_c, i):
        print(f"set_c is a type of: {i} \r")
    if isinstance(lst_d, i):
        print(f"lst_d is a type of: {i} \r")
    if isinstance(dict_e, i):
        print(f"dict_e is a type of: {i} \r")

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

print("\r\n Part 5.\n")

apples = int_a
peaches = int(int_a / 5)
print("Anna has {} apples and {} peaches.".format(apples, peaches))

print("\r\n Part 6.\n")

print("Anna has {1} apples and {0} peaches.".format(peaches, apples))

print("\r\n Part 7.\n")

print("Anna has {apples} apples and {peaches} peaches.".format(apples=apples, peaches=peaches))

print("\r\n Part 8.\n")

print("Anna has {apples:5} apples and {peaches:3} peaches.".format(apples=apples, peaches=peaches))

print("\r\n Part 9.\n")

print(f"Anna has {apples} apples and {peaches} peaches.")

print("\r\n Part 10.\n")

print("Anna has %(apples)s apples and %(peaches)s peaches." % {"apples": apples, "peaches": peaches})

print("\r\n Part 11.\n")

dict_11 = {'apples': apples, 'peaches': peaches}
print("Anna has %(apples)s apples and %(peaches)s peaches." % {"apples": dict_11['apples'],
                                                               "peaches": dict_11['peaches']})

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#
# 12. Convert (1) to list comprehension
# 13. Convert (2) to regular for with if-else

print("\r\n Part 12.\n")
lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp)

print("\r\n Part 13.\n")
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

# 14. Convert (3) to dict comprehension.
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
print("\r\n Part 14.\n")
dict_13 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_13)

# 15*. Convert (4) to dict comprehension.
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

print("\r\n Part 15.\n")
dict_14 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_14)

# 16. Convert (5) to regular for with if.
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

print("\r\n Part 16.\n")
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
print(d)

# 17*. Convert (6) to regular for with if-else.
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print("\r\n Part 17.\n")
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
    else:
        d[num] = num
print(d)

# Lambda:

# 18. Convert (7) to lambda function
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
print("\r\n Part 18.\n")
foo = lambda x, y: x if x < y else y
print(foo(2, 3))

# 19*. Convert (8) to regular function
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
print("\r\n Part 19.\n")


def foo(x, y, z):
    if y < x & x > z:
        return z
    else:
        return y


print(foo(2, 3, 8))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print("\r\n Part 20.\n")
lst_to_sort.sort()
print(lst_to_sort)

# 21. Sort lst_to_sort from max to min
print("\r\n Part 21.\n")
lst_to_sort.sort(reverse=True)
print(lst_to_sort)

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("\r\n Part 22.\n")

lst_x2 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_x2)

# 23*. Raise each list number to the corresponding number on another list:
print("\r\n Part 23.\n")
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_raised = list(map(lambda x, y: x ** y, list_A, list_B))
print(lst_raised)

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("\r\n Part 24.\n")
lst_filtered = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_filtered)

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print("\r\n Part 25.\n")
b = list(range(-10, 10))
b_negative = list(filter(lambda x: x < 0, b))
print(b_negative)

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print("\r\n Part 26.\n")


