"""

Lambda Expression - funcoes anonimas

Sorting a list of lists without lambda


"""

product_list = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(product_list[1])


def print_function_with_for_in_product_list():
    """This function show all items in product list: """

    print('for without use key_function:')
    for a_product in product_list:
        print(a_product)


print(print_function_with_for_in_product_list.__doc__)
print_function_with_for_in_product_list()

print()


def key_func(item):
    """This function is used to access a second [0, "1"] position in a list/array."""
    return item[1]


def print_function_with_for_and_key_function_in_product_list():
    """This function show all items in product list, but accessing second position of item
     using key_function"""

    print('for with key_function:')
    for product in product_list:
        item = key_func(product)
        print(item)


print(print_function_with_for_and_key_function_in_product_list.__doc__)
print_function_with_for_and_key_function_in_product_list()

print()
print('Using function sort by list with key_function for sorting a list of lists')

print('Ascending Sort')
product_list.sort(key=key_func)
print(product_list)
print()

print('Descending Sort')
product_list.sort(key=key_func, reverse=True)
print(product_list)