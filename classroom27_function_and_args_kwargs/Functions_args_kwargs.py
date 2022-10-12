"""

Functions - def

"""


def hello(name, year):
    return f'Hello {name}, are you {year} years old?'


msg = hello(name='Matheus Carvalho', year=22)

print(msg)


def print_function():
    print('Vou printar')


def dumb():
    return print_function


test_function_per_reference = dumb()

print(test_function_per_reference)
print('test_function_per_reference: ', id(test_function_per_reference), ' |', 'print_function: ', id(print_function))

print('test_function_per_reference execution: ', test_function_per_reference)
print('print_function: ', end='')
print_function()

print()
print('Returning many values in function')


def returning_many_values():
    name = 'Matheus'
    surname = 'Carvalho'
    age = 22
    return name, surname, age


tupla = returning_many_values()
name, surname, age = returning_many_values()
print(tupla)
print(f'name = {name}')
print(f'surname = {surname}')
print(f'age = {age}')

print()
print('Packing args')


# packing args - isso eh usado quando nao sabemos quantos
# argumentos esperar
# *args eh uma tupla, elas sao imutaveis
def packing_args(*args):
    # args[0] = 20 - isso lanca erro
    # para alterar valores em uma tupla eh preciso fazer o casting dela para list
    # lista = list(args) - uma lista eh mutavel
    print(args)
    # print(args[0])
    # print(args[7])
    # print(args[:5])


packing_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print()
print('Passando mais de um parametro')
# usando o *args eh possivel mandar varios parametros na chamada da funcao
packing_args('matheus', 22, 'carvalho', 'developer', [1, 2, 3, 4])

print()
# nada mais eh que args so que nomeados
print('**Kwargs')


def packing_key_args(**kwargs):
    print(kwargs)
    print(kwargs['name'])  # lanca erro caso a variavel nomeada nao exista
    print(kwargs['surname'])
    # outra forma de acessar um valor nomeado no kwargs
    name_var = kwargs.get('name')  # nao lanca erro caso a variavel nomeada nao exista
    print(name_var)

    none_exist = kwargs.get('age')  # nao lanca erro caso a variavel nomeada nao exista
    if none_exist is not None:
        print(none_exist)


packing_key_args(name='matheus', surname='carvalho', age=22)



