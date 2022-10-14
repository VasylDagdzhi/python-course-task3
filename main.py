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
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

