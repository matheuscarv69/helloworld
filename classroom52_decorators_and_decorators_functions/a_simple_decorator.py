"""

Decorators:

Trata-se de um design pattern que permite alterar o comportamento de uma
função, classe ou método, dinamicamente.

"""


def decorador(funcao_a_ser_decorada):
    def execute():
        print('Print adicionado dinamicamente na execução da função decorada')
        funcao_a_ser_decorada()

    return execute


def apresentacao():
    print('Hi, my name is Axel')


apresentacao = decorador(apresentacao)

apresentacao()
