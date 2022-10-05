"""
Reduce é utilizado para realizar ACUMULAÇÕES utilizando lambdas

ex:

Somar uma lista de números:

É possível fazer isso usando um acumulador e um laço de repetição

reduce(lambda acumulador, item_da_colecao: operacoes, lista/dict, valor inicial do acumulador)

"""

from classroom44_map.datas import products
from functools import reduce

print('Sum total price of all products')

total_products_price = reduce(lambda accumulator, product: accumulator + product['price'], products, 0.0)

print(f'Total Product Price {total_products_price}')

print()

print('Average of Total Products Price')
average_price = round(total_products_price / len(products), 2)
print(f'Average: {average_price}')
