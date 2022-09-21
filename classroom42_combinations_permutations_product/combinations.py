"""
Combinations, Permutations e Product — Itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Ambos não repetem valores únicos
Produto — Ordem importa e repete valores únicos
"""

from itertools import combinations

print('Combinação — Ordem dos elementos não importa')

peoples = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

"""
combinations(param1, param2)
param1 - lista/conjunto/wherever
param2 - quantidade de combinações
"""
for people_group in combinations(peoples, 2):
    print(people_group)
