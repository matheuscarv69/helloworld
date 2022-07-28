"""

1 — Crie uma função que exibe uma saudação com os (parâmetros) saudação e nome.

"""

print('Hello Function\n')


def hello(saudation, name):
    print(f'Welcome Mr/Mrs {name}, {saudation}')

hello(saudation='Good Morning', name='M. Carvalho')
hello(saudation='Good Aftermoon', name='J. Gosling')