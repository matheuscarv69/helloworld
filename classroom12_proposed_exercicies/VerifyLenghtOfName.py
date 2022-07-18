"""

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou.
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

"""

name = input('What your name? ')

print(len(name))

if 4 >= len(name) > 0:  # len(name) <= 4 and len(name) > 0
    print('Your name is very short')
elif 6 >= len(name) >= 5:  # len(name) <= 6 and len(name) >= 5
    print('Your name is normal')
else:
    print('Your name is very long')
