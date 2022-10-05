"""
Map possui o comportamento parecido com list comprehesion

map(function, iterable/list...) - retorna um iterable
"""

from datas import list_of_numbers

print('Using list comprehesion')
new_list_of_numbers_with_list_comprehesion = [num * 2 for num in list_of_numbers]

print(f'default list - {list_of_numbers}')
print(f'modified list - {new_list_of_numbers_with_list_comprehesion}')

print()

print('Using Map function')
new_map_object_of_list_of_numbers_with_map = map(lambda num: num * 3, list_of_numbers)
new_list_of_numbers_with_map = list(new_map_object_of_list_of_numbers_with_map)
print(f'new list by map function = {new_list_of_numbers_with_map}')
