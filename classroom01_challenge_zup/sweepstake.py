"""
No primeiro passo, precisamos construir um endpoint que receberá o e-mail da
pessoa e retornará um objeto de resposta com os números sorteados para a aposta.
Você deverá garantir que estas informações estejam gravadas em um banco de dados
e devidamente associadas à pessoa.

Também devemos construir um segundo endpoint para listar todas as apostas de um
solicitante, passando seu e-mail como parâmetro, o sistema deverá retornar em
ordem de criação todas as suas apostas.

"""
from random import randint


def start_sweepstake():
    print('------- Welcome the sweepstake -------', end='\n')
    print('------- Enter your datas -------', end='\n\n')

    id = 0

    start = True

    dict_users = dict()

    while start:
        id += 1
        user_registered = user_registry(id)

        dict_users.update(user_registered)

        continue_or_stop = input('Do you finish? y/n: ')
        print()

        if continue_or_stop.lower() == 'y':
            start = False

    return dict_users


def user_registry(user_id):
    name = input('Enter your name: ')
    email = input('Enter your email: ')

    sweepstake_number = generate_sweepstake()

    print(f'\nMrs {name}, your sweepstake number is: {sweepstake_number}', end='\n\n')

    user_domain = {
        user_id: {
            'name': name,
            'email': email,
            'sweepstake_number': sweepstake_number
        }
    }

    return user_domain


def generate_sweepstake():
    set_random_numbers = set()

    while len(set_random_numbers) < 6:
        random_number = randint(0, 60)
        set_random_numbers.add(random_number)

    return set_random_numbers


def show_report(user_dict):
    print('------- Report -------')
    print()

    for user_id, user_value in user_dict.items():
        print(f'ID: {user_id}')

        for user_key, user_data in user_value.items():
            print(f'\t"{user_key}" - "{user_data}"')

        print()


users = start_sweepstake()

show_report(users)
