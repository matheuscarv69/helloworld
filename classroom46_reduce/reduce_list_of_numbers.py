"""
Reduce é utilizado para realizar ACUMULAÇÕES utilizando lambdas

ex:

Somar uma lista de numeros:

É possível fazer isso usando um acumulador e um laço de repetição

reduce(lambda acumulador, item_da_colecao: operacaoes, lista/dict, valor inicial do acumulador)

"""

from classroom44_map.datas import list_of_numbers
from functools import reduce

print('Sum all values in list of number usind For loop')

total = 0

for number in list_of_numbers:
    total += number

print()
print(list_of_numbers)

print()
print(f'Sum of all list of number is : {total}')


print()
print('Sum all values in list using Reduce')

total_value = reduce(lambda accumulator, num: accumulator + num, list_of_numbers, 0)

print(f'Sum of all list is : {total_value} using reduce')



