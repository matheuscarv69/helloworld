"""
Zip_longest une iteráveis independente do tamanho deles
Zip_longest retorna um gerador/generator, este por sua vez ocupa menos espaço de memória

Para utiliza-lo é preciso importa-lo do module itertools

ex.:
from itertools import zip_longest

name = ['Matheus', 'Ana', 'Geovana', 'Cleo']
surname = ['Almeida', 'Alice', 'Almeida']

name_surname = zip(name, surname)

Percebe-se que o tamanho de surname é menor que o de name,
por conta disso, a funcao zip, ira criar uma nova lista
com a quantidade de elementos igual a da menor lista, no caso
a lista de surname

# output
[('Matheus','Almeida'), ('Ana','Alice'),('Geovana','Almeida')]

----- x -----

name_surname = zip_longest(name, surname)
print(name_surname)

# output
[('Matheus','Almeida'), ('Ana','Alice'),('Geovana','Almeida'), ('Cleo', None) ]

----- x -----

Para definir um valor default a ser mostrado no lugar de None, usa-se a seguinte forma:

name_surname = zip_longest(name, surname, fillValue='Surname')
print(name_surname)

# output
[('Matheus','Almeida'), ('Ana','Alice'),('Geovana','Almeida'), ('Cleo', 'Surname') ]


"""
from itertools import zip_longest, count

index = count()

cities = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Boa Vista']
states = ['SP', 'MG', 'BA']

cities_states = zip(
    index,
    cities,
    states,
)

for index, cities, states in cities_states:
    print(index, cities, states)

