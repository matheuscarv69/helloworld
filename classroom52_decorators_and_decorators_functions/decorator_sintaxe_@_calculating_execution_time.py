"""

Decorators:

Trata-se de um design pattern que permite alterar o comportamento de uma
função, classe ou método, dinamicamente.

"""

from time import time


def decorador_uppercase(function):
    def execute(*args):
        print('Executing print function in decorator')

        start_time = time()  # getting currently time before execution function.

        name = args[0].upper()
        function(name)

        end_time = time()  # getting currently time after execution function.
        execution_time = (end_time - start_time) * 1000

        print(f'The function "{function.__name__}" has executed in {execution_time:.4f} ms')

    return execute


@decorador_uppercase
def presentation(name):
    print(f'Hi, my name is {name}')


presentation('Dumb')
