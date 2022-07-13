"""
* Criar variáveis para nome, idade,
* altura e peso de uma pessoa
* Criar variável com o ano atual
* Obter o ano de nascimento da pessoa
* Obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos os valores na tela usando F-Strings
"""

name = 'Guido'
surname = 'Rossum'
height = 1.80
weight = 80
yearBirth = 1956

bmi = weight // height ** 2

print(f'{name} {surname} is {2022-yearBirth} years old, {height:.2f} of height and his weight is {weight} kg.')
print(f'His BMI is {bmi:.2f}.')
print(f'{name} was born in {yearBirth}.')
