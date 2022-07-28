"""
Listas em Python

Fatiamento - Slicing

append, insert, pop, del, clear, extend, +
min, max,
range

"""
#        0    1    2    3    4
list = ['a', 'b', 'c', 'd', 'e']
#    -   5    4    3    2    1

print('For, enumerate in list')
for index, num in enumerate(list):
    print(f'{index} - {num}')

print(f'printing in list: {list}')

print()
print('Slicing in list')
print(f'list - 3 primeiros {list[0:3]}')
print(f'list - pulando de 2 em 2 {list[0: len(list): 2]}')
print(f'list - iniciando na 2 posicao até o final {list[2:]}')
# :: significa que omitimos o inicio e o fim da list, logo serah impresso tudo
print(f'list - invertendo a ordem do print dos valores {list[::-1]}')

