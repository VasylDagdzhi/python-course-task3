print("\r\n Part 1.\n")

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(f"ID of int_a is{id(int_a)} and value is {int_a}")
print(f"ID of str_b is{id(str_b)} and value is {str_b}")
print(f"ID of set_c is{id(set_c)} and value is {set_c}")
print(f"ID of lst_d is{id(lst_d)} and value is {lst_d}")
print(f"ID of dict_e is{id(dict_e)} and value is {dict_e}")

print("\r\n Part 2.")
lst_d.append(4)
lst_d.append(5)
print(f"\r\nID of lst_d now is{id(lst_d)} and values inside have changed to {lst_d}")