"""
Combinations, Permutations e Product — Itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Ambos não repetem valores únicos
Produto — Ordem importa e repete valores únicos
"""

from itertools import permutations

print('Permutação — Ordem dos elementos importa')

peoples = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

"""
permutations(param1, param2)
param1 - lista/conjunto/wherever
param2 - quantidade de combinações
"""
for people_group in permutations(peoples, 2):
    print(people_group)
