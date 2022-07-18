"""

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

num = input('Enter with a number: ')

try:
    num = int(num)

    is_pair = num % 2 == 0

    if is_pair:
        print(f'This number: {num} is Pair')
    else:
        print(f'This number: {num} is Odd')
except:
    print(f'Error - this number: {num} is not integer')
