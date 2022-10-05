"""
A função filter serve para filtrar coisas de acordo
com uma lambda


"""

from classroom44_map.datas import products

print('Using filter function for to find all products with price greater than 50')

products_with_price_greater_50 = filter(lambda product: product['price'] > 50, products)

for product in products_with_price_greater_50:
    print(product)


print()
print('Using filter function for to find all products with price smaller than 50 using a custom function')


def filter_products_with_price_greater_50(item):
    if item['price'] < 50:
        return True

    return False


products_with_price_greater_50_version_2 = filter(filter_products_with_price_greater_50, products)

for p in products_with_price_greater_50_version_2:
    print(p)