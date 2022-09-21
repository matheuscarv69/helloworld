# union |
# une os dois classroom32_sets

print('Union | ')
set_1 = {1, 2, 3, 4}
set_2 = {5, 6, 7, 'union'}
set_3_union = set_1 | set_2  # ou set_3 = set_1.union(set_2)

print('set 1: ', set_1, end='\n')
print('set 2: ', set_2, end='\n')
print('union - set 3: ', set_3_union, end='\n\n')

print('Intersection &')
# intersection & - todos os elementos presentes nos dois classroom32_sets
set_4 = {1, 2, 3, 4}
set_5 = {5, 2, 7, 'union', 1}
set_6_intersection = set_4 & set_5  # set_4.intersection(set_5)

print('set 4: ', set_4, end='\n')
print('set 5: ', set_5, end='\n')
print('intersection - set 6: ', set_6_intersection, end='\n\n')

print('difference -')
# diference -  - pega apenas os elementos que estao presentes
# no set da esquerda e nao no da direita
# a ordem importa
set_7 = {1, 2, 3, 4, 'difference'}
set_8 = {1, 2, 3, 4}
set_9_difference = set_7 - set_8  # set_7.difference(set_8)

print('set 7: ', set_7, end='\n')
print('set 8: ', set_8, end='\n')
print('difference - set 9: ', set_9_difference, end='\n\n')


print('symmetric_ difference ^')
# symmetric_diference ^  - pega apenas os elementos que estao presentes
# nos dois classroom32_sets, mas nao em ambos

set_10 = {1, 2, 3, 4, 'matheus'}
set_11 = {1, 2, 3, 4, 'carvalho'}
set_12_symmetric_difference = set_10 ^ set_11  # set_10.symmetric_difference(set_11)

# aqui o symmetric_difference vai pegar 'matheus''carvalho'
# pois sao elementos que estao nos dois classroom32_sets, mas nao em ambos
# matheus em set_10
# carvalho em set_11

print('set 10: ', set_10, end='\n')
print('set 11: ', set_11, end='\n')
print('symmetric_difference - set 12: ', set_12_symmetric_difference, end='\n\n')

