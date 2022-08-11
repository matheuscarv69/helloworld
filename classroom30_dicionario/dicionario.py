"""

dicionario eh bem parecido com a estrutura Map

key, value

"""

# Criando um dicionario
print('Criacao de dicionario \n')

d1 = {'key1': 'value1'}

# adicionando outra chave no dicionario

d1['key2'] = 'value2'

print(f"Criacao tradicional - {d1} \n")

# outra forma de criar dicionario

d2 = dict(key1='value1', key2='value2')

print('Criacao com dict(key1=value1) - ', d2, end='\n')

# dicionarios aceitam qualquer tipo de dado, ate tuplas
print("Criando dicionario com varios tipos \n")
d3 = {
    'key1': 'value1',
    123: 2019,
    (6, 5, 4): 'tuple'
}

print(f'Criacao com varios tipos de dados - {d3} \n')

# Acessando valores de um dicionario
print('Acessando dados de dicionarios \n')
print('d1[key1] - ', d1['key1'])  # se a chave nao existir, lancara excecao
print('d2.get(key1) - ', d2.get('key1'))  # caso a chave nao existe, o codigo nao lanca excecao

# Formas de atualizar o valor de uma chave
print('Atualizando valores de dicionarios \n')
d1['key1'] = 'new_value1'
d2.update({'key1': 'new_value1'})

# Formas de excluir um valor de um dicionario
print('Deletando valores de dicionarios \n')
print('Usando del \n')

print('d1 - ', d1)

del d1['key1']

print('d1 - ', d1)
print()

print('Usando pop \n')

d1.update(
    {'delete-me': 'delete-me-value'}
)
print(d1)
d1.pop('delete-me')
print(d1)
print()

print('Usando popItem - Ele exclui o ultimo item do dicionario \n')
d1.update(
    {'delete-me-again': 'delete-me-again-value'}
)
print(d1)
d1.popitem()
print(d1)
print()

# Iterando em um dicionario
print('Iterando em um dicionario \n')

print('For para mostrar as chaves \n')
# d2.keys() tem o mesmo comportamento
for key in d2:
    print(key)

print()

print('For para mostrar os valores \n')
for value in d2.values():
    print(value)

print('For para mostrar as chaves e valores \n')
for item in d2.items():
    print(item)

print('Outra forma para pegar as chaves e valores usando unpacking \n')
for key, value in d2.items():
    print(f'{key} - {value}')

print('\n')

# Criando um novo dicionario a partir de outro dicionario
print('Criando um novo dicionario a partir de outro dicionario \n')

# Para fazer isso precisamos usar a funcao .copy() do dicionario, ela cria uma copia rasa do dicionario
# pois da forma tradicional var = d1, estaremos dizendo ao python que var tera
# uma referencia de d1, sendo assim, se algo mudar em var, no d1 tambem mudara

new_dicionario = d1.copy()

print(d1)

new_dicionario['key3'] = 'value3'

print(new_dicionario)
print('\n')

"""
Copia Rasa com o .copy

Essa funcao cria uma copia de um dicionario, onde a partir dessa copia
eh possivel alterar valores absolutos (exceto listas, arrays, dicionarios) que
estiverem dentro do dicionario principal sem que o afete.

Mas caso dentro do dicionario principal tenha lista, array, dicionario ou outra 
estrutura de dados, caso na copia ela seja modificada, isso refletira no dicionario principal

Para contornar esse comportamento, usa-se o modulo copy do python, especificamente
usando a funcao deepCopy - copia profunda
"""
# exemplo

dicionario = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': ['Evolution', 'WRX', 'Type R']
}

print('Antes de fazer alteracao no novo dicionario')
print(dicionario, '\n')

print('Criando novo dicionario com o .copy() e alterando um valor da lista \n')

novo_dicionario = dicionario.copy()
# alterando valor da lista dentro do dicionario
novo_dicionario['key3'][0] = 'RS200'
print('Imprimindo novo dicionario')
print(novo_dicionario, '\n')

print('Imprimindo o dicionario e o novo dicionario \n')
print(dicionario)
print(novo_dicionario)
