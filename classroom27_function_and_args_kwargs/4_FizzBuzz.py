"""

4 — Fizz Buzz — Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisivel por 5, retorne buzz. Se o parâmetro da função
for divisivel por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.

"""

from random import randint

print('FizzBuzz Function\n')

# 10% of 150 = 15

'''

divisivel por 3 = Fizz
divisivel por 5 = Buzz
divisivel por 5 e 3 = FizzBuzz
Nao divisivel por nenhum = value

'''


def fizz_buzz(value):
    if value % 5 == 0 and value % 3 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    else:
        return value


print('Sequential - 0/100')
for num in range(100):
    print(f'{num} - {fizz_buzz(num)}')

print()
print('-------------------------------')
print('random')

for num in range(100):
    random_value = randint(0, 100)
    result = fizz_buzz(random_value)

    if not type(result) == int:
        print(f'{random_value} - {result}')
