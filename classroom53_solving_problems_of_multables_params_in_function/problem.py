"""

- Multable types -> Lists and Dictionaries
- Immutables types -> Tuples, strings, numbers, Booleans, NoneType

"""


def create_a_list_of_clients(iterable_clients, some_client_list=[]):
    some_client_list.extend(iterable_clients)

    return some_client_list


"""
Espera-se que sejam criadas duas listas diferentes com os respectivos
nomes de clientes
"""

client_list_1 = create_a_list_of_clients(['João', 'Maria', 'Eduardo'])
client_list_2 = create_a_list_of_clients(['Marcos', 'Jonas', 'Zico'])

"""
Porém o resultado é o contrário, as duas listas criadas são iguais e
ambas se juntaram.
"""
print(client_list_1)
print(client_list_2)

"""
Isso acontece por conta que o argumento some_clients_list é uma lista []
logo ela é mutável, dessa forma, ela está mantendo os valores passados inicialmente
na primeira chamada da função e adicionando novos valores quando a função é
chamada novamente.

No arquivo classroom53_solving_problems_of_multables_params_in_function.undo_redo.py
estará a solução.
"""