"""

2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.

"""

print('Function1 varias funcoes como parametro')


def saudation(name):
    print(f'Welcome {name}')


def age_calculate(year_birth, current_year):
    print(f'Are you {current_year - year_birth} years old?')


def function2():
    print("I am the function2")


def function1(**kwargs):
    function = kwargs.get('func')
    saudation = kwargs.get('saudation')
    age = kwargs.get('age')

    saudation('Matheus')
    age(year_birth=1999, current_year=2022)

    return function


funtion_return = function1(func=function2, saudation=saudation, age=age_calculate)

funtion_return()
# function1(func=function2(), saudation=saudation(name='Matheus'), age=age_calculate(1999, 2022))

print()
print()
print('Other Way')
print()


def principal(function, *args, **kwargs):
    return function(*args, **kwargs)


def say_hello(name):
    return f'Hello {name}'


def age_calculate(name, year_birth, current_year):
    return f'{name}, are you {current_year - year_birth} years old?'


result = principal(say_hello, 'Matheus')
print(result)

result2 = principal(age_calculate, 'Matheus', year_birth = 1999, current_year=2022)
print(result2)
