"""

1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.

"""

print('Function1 recebe Function2 como parametro')


def function2():
    return 'I am the function2'


def function1(func=None):
    if func is not None:
        return func()
    else:
        print('I am function1, because none function received')


func = function1(function2)
print(func)
