immutable_var = (1, 2, 'vadim')
print(immutable_var)
# immutable_var[1] = 33
# print(immutable_var)
# # Т.к. это неизменяемый объект, заранее зарезервированный в памяти, поэтому по памяти он менее объемный чем список и является константным значением.
mutable_list = ([3, 4, 'artem'], 'artem')
print(mutable_list)
mutable_list[0][2] = ')0'
print(mutable_list)








