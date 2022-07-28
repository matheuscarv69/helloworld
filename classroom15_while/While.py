"""
while em Python

Utilizado para realizar ações enquanto
uma condição for verdadeira.
Requisitos: Entender condições e operadores

"""

x = 0

while x <= 10:
    print(x)
    x += 1

print('Finish first while')

print()

x = 0
while x <= 10:

    if x == 3:
        x = x + 1
        continue  # nao executa as linhas posteriores, o codigo eh executado novamente do while

    print(x)
    x = x + 1

print('Finish second while')

print()

x = 0
while x <= 10:

    if x == 3:
        x += 1
        break  # encerra o while

    print(x)
    x += 1

print('Finish')

print()

i = 0
j = 0

while i <= 2:
    j = 0

    while j <= 2:
        print(f'{i},{j}')
        j += 1

    i += 1