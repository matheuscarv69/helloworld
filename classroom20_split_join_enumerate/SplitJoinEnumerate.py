"""

Split, Join, Enumerate

Split - Divide uma string
Join - Juntar lista e string
Enumerate - Enumerar elementos em uma lista / objetos iteraveis

"""

print('Split Example')

string = 'Acorda Pedrinho que hoje tem campeonato.'

list_string_split = string.split(' ')

for index, word in enumerate(list_string_split):
    if '.' in word:
        list_string_split[index] = word.removesuffix(".")

print(f'Total elements in list_string_split: {len(list_string_split)}')
print(list_string_split)
print()

# Join junta uma lista em um string
print("Join Example")

new_string = ' '.join(list_string_split)
print(f'Elements of list: {list_string_split}')
print(f'Phrase of new_string: {new_string}')
print()

# Enumerate enumera um colecao
print('Enumerate example')
print()

list_of_lists = [
    ['sam', 'winchester'],
    ['dean', 'winchester'],
    ['castiel', 'angel']
]

# Aqui foi feito o desempacotamento, isso eh similar ao destruct do JS
print('Enumerate Raiz - Desempacotamento / Destruct')
for index, value in list_of_lists:
    print(index, value, sep=' - ')

print()

"""
Aqui foi usada a funcao enumerate, nesse caso ela basicamente atribui um índice 
aos elementos da lista principal, que também sao listas.
Dessa forma eh possível acessar outros valores da variável value, pois ela se trata
de uma lista também.
"""

print('Enumerate Nutela - Usando funcao enumerate')
for index, value in enumerate(list_of_lists):
    print(index, value, sep=' | ')

print()

"""

Desempacotamento, pode ser usado para atribuir valores de uma lista para variáveis
parecido com o destruct

"""

print('Unpack')

names = ['Ada Lovelace', 'James Gosling', 'Guido Rossum']
print(names)

print()

people1, people2, people3 = names

print(f'people1 - {people1}')
print(f'people2 - {people2}')
print(f'people3 - {people3}')


