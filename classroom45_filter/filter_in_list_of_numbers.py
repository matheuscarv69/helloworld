"""
A função filter serve para filtrar coisas de acordo
com uma lambda

numeros_pares = filter(lambda num: num % 2 == 0, list_of_numbers)

"""

from classroom44_map.datas import list_of_numbers


print('Using filter function for to find all pair numbers')
pair_numbers = filter(lambda num: num % 2 == 0, list_of_numbers)

print(list(pair_numbers))

print()
print('Using list comprehension for to find all pair numbers')

pair_numbers_list_comprehension = [num for num in list_of_numbers if num % 2 == 0]

print(pair_numbers_list_comprehension)