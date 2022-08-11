"""

Tuplas sao semelhantes a listas, porem elas nao podem ser modificadas

Para modificar uma tupla eh preciso converte-las em listas

"""

# criando uma tupla

tupla1 = (1, 2, 3, 'matheus', ['almeida', 'carvalho'])

print(type(tupla1))
print(tupla1)
print(tupla1[3])

print()
for index, item in enumerate(tupla1):
    print(f'index[{index}] - {item}')

print()

# slicing em tuplas

values = tupla1[1:4]
print('slicing 1-4', values)

# outra forma de criar tupla e somando tuplas

tupla2 = 1, 2, 3, 'matheus'
tupla3 = 4, 5, 6, 'almeida'

tupla4 = tupla2 + tupla3
print(f'tupla4 - {tupla4}')

print()

# unpacking

n1, n2, *trash, n_ultimo = tupla4

print(n1)
print(n2)
print(n_ultimo) # expected - almeida

# casting tupla para lista para poder alterar valores

list_of_tuple = list(tupla4)

print(f'types - {type(tupla4)} - {tupla4}')

list_of_tuple.insert(7, 'position 7')
list_of_tuple.append(['ola', 'bom dia'])
list_of_tuple.extend(['hi', 'good morning'])

print(f'types - {type(list_of_tuple)} - {list_of_tuple}')

# Convertendo uma lista em tupla
new_tuple = tuple(list_of_tuple)

print(new_tuple)