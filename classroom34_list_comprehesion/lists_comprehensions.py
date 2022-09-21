"""
O uso de lists comprehesion torna mais facil o
processo de iteracao de elementos em uma lista
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# o nome variavel é um alias para se referir a um elemento
# dentro da lista l1
# O nome variavel deve ser usado antes e depois do for
# pois o utilizamos para referenciar o elemento da lista l1
exemplo1 = [variavel for variavel in l1]

# o list comprehesion que utilizamos acima, nada mais faz
# do que pegar um elemento dentro da l1 e atribuir a exemplo1,
# dessa forma as duas lista são identicas
print(exemplo1)

print()
print()

# aqui usamos o list comprehesion para iterar sobre cada elemento de
# l1, após isso, fazemos a multiplicacao de cada elemento por 2
exemplo2 = [variavel * 2 for variavel in l1]

print(exemplo2)

print()
print()

# Tornando um pouco mais complicado
'''
Vamos criar uma tupla a partir da l1, onde nessa tupla teremos o
primeiro item sendo um elemento da l1 e o segundo elemento a posicao dele na l1.

ex:
l1 = [1, 2, 3, 4, 5]

lista_tupla = [(1,0), (2,1), (3,2), (4,3), (5,4)]

'''

# dica, no range definimos ate que posicao a contagem sera feita,
# no caso estamos botando para a contagem da posicao ir ate o tamanho da l1
# que tem 9 posicoes, mas se quisermos podemos colocar qualquer valor dentro
# do range(3), assim range(3) ira fazer a contagem de 0, 1, 2
exemplo3_lista_tupla = [
    (variavel_l1, posicao) for variavel_l1 in l1
    for posicao in range(len(l1))
]

for value in exemplo3_lista_tupla:
    print(value)

print()
print()

'''
Outro exemplo do uso de list comprehesions é o seguinte:
Com ele podemos por exemplo, mudar variaveis de posicao dentro de uma tupla
ou lista
'''
# aqui é uma tupla de tuplas
# vamos mudar os valores par ao lugar das chaves
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)

tupla_exemplo4 = [(valor, chave) for chave, valor in tupla]

print(tupla_exemplo4)

print()
print()

'''
Tambem é possivel usar if's dentro do list comprehesion

No exemplo, vamos criar uma lista que vai de 0 a 20
e vamos criar outra lista usando o comprehesion para que essa
lista tenha somente numeros pares divisiveis por 2
'''
lista_0_20 = list(range(20))

lista_num_pares = [num for num in lista_0_20 if num % 2 == 0]

print(lista_num_pares)

'''
Ainda da pra ser mais especifico

vamos criar outra lista usando o comprehesion para que essa
lista tenha somente numeros pares divisiveis por 2 e por 8 somente
'''

lista_num_pares_divisiveis_por_8 = [num for num in lista_0_20 if num % 2 == 0 if num % 8 == 0]

print(lista_num_pares_divisiveis_por_8)

print()
print()

'''
Tambem é possivel usar if's else dentro do list comprehesion

Porem a sintaxe muda um pouco, onde o if muda de lugar, indo para o inicio
da comprehesion

'''

lista_num_divisiveis_por_3 = [num if num % 3 == 0 else 'Não é divisivel' for num in lista_0_20]

print(lista_num_divisiveis_por_3)
