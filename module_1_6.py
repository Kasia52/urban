my_dict = {'haaland': 9, 'nedved': 21, 'king': 3 }
print(my_dict.get('haaland'))
print(my_dict.get('messi','Ошибка'))
print(my_dict)
a = my_dict.pop('nedved')
print(my_dict)
print(a)
##
my_set = {'a', 'b', 'c', 'd', 'e', 'e', 'f', 'a'}
list_ = ['a', 'b', 'c', 'c', 'f']
list_ = set(list_)
print(list_)
print(list_.add('z'))
print(list_)
print(list_.discard('a'))
print(list_)


