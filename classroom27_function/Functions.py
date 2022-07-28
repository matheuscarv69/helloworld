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