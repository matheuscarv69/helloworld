"""
Formatando valores com modificadores

:S- Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""

num_1 = 10
num_2 = 3213

division = num_1 / num_2

print(division)

print(f'f string {division:.2f}')
print('.format {:.2f}'.format(division))

print()

print(':(CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)')
"""
> - Esquerda
< - Direita
^ - Centro
"""
print(f'0 a esquerda até completar 10 caracteres - {num_1:0>10}')

print(f'0 a esquerda até completar 10 caracteres - {num_2:0>10}')

print(f'0 a esquerda até completar 10 caracteres com 2 casas decimais - {num_2:0>10.2f}')

print(f'0 a direita até completar 10 caracteres - {num_2:0<10}')

print(f'0 no centro até completar 10 caracteres - {num_2:0^10}')

