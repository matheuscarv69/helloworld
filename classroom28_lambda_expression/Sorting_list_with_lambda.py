"""

Lambda Expression - funcoes anonimas

Sorting a list of lists with lambda


"""

product_list = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(product_list[1])

print()
print('Using function sort by list with lambda for sorting a list of lists')

print('Ascending Sort')
product_list.sort(key=lambda item: item[1])
print(product_list)
print()

print('Descending Sort')
product_list.sort(key=lambda item: item[1], reverse=True)
print(product_list)
print()

print('\nOther method: Sorting with sorted() function\n')

print('Ascending Sort - sorted function')
product_list_ascending_sorted = sorted(product_list, key=lambda item: item[1])
print(product_list_ascending_sorted)
print()

print('Descending Sort - sorted function')
product_list_descending_sorted = sorted(product_list, key=lambda item: item[1], reverse=True)
print(product_list_descending_sorted)
