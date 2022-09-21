"""
Zip une iteráveis até o tamanho do iterável que possui o menor valor
Zip retorna um gerador/generator, este por sua vez ocupa menos espaço de memória

ex.:
name = ['Matheus', 'Ana', 'Geovana', 'Cleo']
surname = ['Almeida', 'Alice', 'Almeida']

Percebe-se que o tamanho de surname é menor que o de name,
por conta disso, a funcao zip, ira criar uma nova lista
com a quantidade de elementos igual a da menor lista, no caso
a lista de surname

name_surname = zip(name, surname)
print(name_surname)

# output
[('Matheus','Almeida'), ('Ana','Alice'),('Geovana','Almeida')

"""

cities = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Boa Vista']

states = ['SP', 'MG', 'BA']

cities_states = zip(cities, states)

print(cities_states)  # mostrara que trata-se de um zip salvo na memória

# repare que Boa Vista ficou de fora, por conta que o tamanho de states é menor que o de cities
print(list(cities_states))

'''
Para resolver essa característica do zip usaremos o zip_longest
do module itertools
'''



