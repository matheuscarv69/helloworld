"""

Decorators:

Trata-se de um design pattern que permite alterar o comportamento de uma
função, classe ou método, dinamicamente.

"""


def decorador_uppercase(function):
    def execute(*args):
        print('Executing print function in decorator')

        name = args[0].upper()

        function(name)

    return execute


@decorador_uppercase
def presentation(name):
    print(f'Hi, my name is {name}')


presentation('Dumb')
