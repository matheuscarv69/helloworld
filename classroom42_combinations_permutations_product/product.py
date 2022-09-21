"""
Combinations, Permutations e Product — Itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Ambos não repetem valores únicos
Produto — Ordem importa e repete valores únicos
"""

from itertools import product

print('Produto — Ordem dos elementos importa e repete valores únicos')

peoples = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

"""
product(param1, repeat = param2)
param1 - lista/conjunto/wherever
param2 - quantidade de combinações
"""
for people_group in product(peoples, repeat=2):
    print(people_group)
