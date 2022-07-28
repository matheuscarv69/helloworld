"""

Unpack

"""

print('Unpack Example')
names = ['Ada Lovelace', 'James Gosling', 'Guido Rossum']
print(names)

print()

people1, people2, people3 = names

print(f'people1 - {people1}')
print(f'people2 - {people2}')
print(f'people3 - {people3}')
print()

print('Other Unpack Example')

list_values = ['Luiz', 'João', 'Pedrinho', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

"""

Dessa forma fazemos o desempacotamento dos valores que estão dentro da lista,
pegamos os três primeiros nomes, seus valores estão atribuídos às variáveis
n1, n2 e n3.
Como a lista tem mais valores além desses citados, precisamos atribuir esses outros valores
à outras variáveis, por isso usamos o *other_list, com isso o restante dos elementos da lista
irão ser alocados nessa variável other_list


"""
n1, n2, n3, *other_list = list_values

print(f'n1 - {n1}')
print(f'n2 - {n2}')
print(f'n3 - {n3}')
print(f'other_list - {other_list}')
print()

print('Unpack list with variables, other list and getting last element of principal list')
n4, n5, n6, *other_other_list, last_element = list_values

print(f'n4 - {n4}')
print(f'n5 - {n5}')
print(f'n6 - {n6}')
print(f'other_other_list - {other_other_list}')
print(f'last_element - {last_element}')
print()

"""

O desempacotamento para outra lista também funciona no inverso
confuso, mas olha o exemplo

"""

print('Other example of unpack')
"""
Nesse caso estamos pegando o últimos valores da lista e atribuindo para n7, n8, n9

Dica de python:
Caso durante um desempacotamento você crie um lista que não utilizará,
pode atribuir esse nome para ela *_ 
isso indica para outros devs que você não utilizará ela

"""
*other_other_other_list, n7, n8, n9 = list_values

print(f'other_other_other_list - {other_other_other_list}')
print(f'n7 - {n7}')
print(f'n8 - {n8}')
print(f'n9 - {n9}')
print()
