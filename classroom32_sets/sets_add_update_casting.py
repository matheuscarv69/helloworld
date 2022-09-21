"""
add, update, clear, discard
union |
intersection & - todos os elementos presentes nos dois classroom32_sets
difference -  - elementos apenas no set da esquerda
symmetric_difference ^ - elementos que estao nos dois classroom32_sets, mas nao em ambos

curiosidade do set
- ele suporta apenas valores imutaveis:
 - numeros
 - strings
 - tuplas

classroom32_sets nao possuem indice, logo nao eh possivel acessar uma
posicao especifica, porem eh possivel iterar sobre um set
"""

# maneiras de criar classroom32_sets

# 1a forma - parecido com a criacao de dicionarios
# mas a diferenca eh que classroom32_sets nao possuem keys

set_1 = {1, 2, 3, 4, 5}

print(set_1)
print(type(set_1))

print('\niterando sobre um set')
for value in set_1:
    print(value)

# nao eh possivel criar um set vazio com {}, para isso
# usa-se a funcao set()

# set_invalido = {} - isso ira criar um dicionario

print('\n criando set com funcao set() ')
set_2 = set()
print(set_2, end='\n')
# add - adiciona valores em um set

print('\n adicionando valores com add()')
set_2.add(1)
set_2.add(2)
set_2.add(3)

print(set_2, end='\n')

# discard - remove o elemento informado do set
print('\n removendo o elemento informado com a funcao discard()')
set_2.discard(1)
print(set_2, end='\n')

# update - ele adiciona um elemento no set
# e adiciona por meio de iteraveis no set: ex:
# set_2.update('matheus') - cada letra da palavra informada
# ficara em uma posicao do set e fora de ordem

# eh possivel passar varios objetos no update, listas, tuplas
# que a funcao ira coloca-los direto no set, excluindo
# valores repetidos, isso eh uma caracteristica do set
print('\n adicionando elementos com o update')

set_2.update('matheus')
set_2.update(['isso eh uma lista', 1, 2, 3], {'isso eh um set', 3, 2, 1})

print(set_2, end='\n\n')

# Exemplo de casting de lista para set, para excluir duplicidades
print('Casting de lista para set - excluindo duplicidades')
lista_1 = [1, 2, 3, 4, 4, 4, 4, 4, 4, 'matheus', 12, 2, 1, 2, 3, 4, 'carvalho', 'matheus']

set_3_casting = set(lista_1)

print('Lista: ', set_3_casting, end='\n\n')
print('Set Casting: ', set_3_casting, end='\n\n')

