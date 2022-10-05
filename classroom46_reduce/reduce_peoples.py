"""
Reduce é utilizado para realizar ACUMULAÇÕES utilizando lambdas

ex:

Somar uma lista de números:

É possível fazer isso usando um acumulador e um laço de repetição

reduce(lambda acumulador, item_da_colecao: operacoes, lista/dict, valor inicial do acumulador)

"""

from classroom44_map.datas import peoples
from functools import reduce

print("Sum all peoples' age")

sum_all_age = reduce(lambda accumulator, people: accumulator + people['age'], peoples, 0)

print(f'The sum of all peoples age is: {sum_all_age} years')

average_age = sum_all_age / len(peoples)

print(f'Average Age is : {average_age}')
