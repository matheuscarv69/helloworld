"""

- Multable types -> Lists and Dictionaries
- Immutables types -> Tuples, strings, numbers, Booleans, NoneType

"""

"""
Para resolver o problema, basta adicionar-mos um valor padrão Imutável
na declaração do argumento some_client_list da função.

E depois realizar uma verificação para que, quando não for informado
nenhuma lista para o some_client_list na chamada da função
create_a_list_of_clients, esse parâmetro receba o valor Imutável None,
e dessa forma seja instanciada um nova lista dentro da função.  
"""


def create_a_list_of_clients(iterable_clients, some_client_list=None):
    if some_client_list is None:
        some_client_list = []

    some_client_list.extend(iterable_clients)

    return some_client_list


"""
Espera-se que sejam criadas duas listas diferentes com os respectivos
nomes de clientes
"""

client_list_1 = create_a_list_of_clients(['João', 'Maria', 'Eduardo'])
client_list_2 = create_a_list_of_clients(['Marcos', 'Jonas', 'Zico'])

"""
Agora as duas listas criadas são diferentes por conta da atribuição de um
valor padrão imutável (None) para o argumento some_client_list e da verificação
que está sendo feita toda vez que a função create_a_list_of_clients.
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
