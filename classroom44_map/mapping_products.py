"""
Map possui o comportamento parecido com list comprehesion

map(function, iterable/list...) - retorna um iterable
"""

from datas import products

print('Show all products')
print(type(products))

for product in products:
    print(f'\t{product}')

print()
print('Getting price of product using Map function')
# pegando o preço de dentro de um produto usando map
products_prices = map(lambda product_data: product_data['price'], products)

print(list(products_prices))

print()
"""
Para alterar os precos dentro do dicionario e ainda assim manter a estrutura inicial
devemos criar uma funcao nova e fazer a logica de alteracao de valores dentro dela.

Depois utiliza-la no map, da seguinte forma:
"""


def update_price_of_product(product_data):
    product_data['price'] = round(product_data['price'] * 1.05, 2)
    return product_data


updated_products = map(update_price_of_product, products)

print('Show Products with updated prices')
for product in updated_products:
    print(product)
