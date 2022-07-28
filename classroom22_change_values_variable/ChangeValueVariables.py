"""
x = 10
y = matheus

expected

x = matheus
y = 10

"""

# Em python a troca de valores entre variaveis eh bem simples

x = 10
y = 'matheus'

print(f'x - {x}')
print(f'y - {y}')

print()
print('Mudando os valores - x, y = y, x')
print()

x, y = y, x

print(f'x - {x}')
print(f'y - {y}')

print()
print('Outro exemplo com mais variaveis')
print()
"""
Da pra fazer o mesmo cmo mais variaveis
"""

x = 20
y = 'Carvalho'
z = [1, 2, 3, 4, 5]

print(f'x - {x}')
print(f'y - {y}')
print(f'z - {z}')

print()
print('Mudando os valores - x, y, z = z, y, x')
print()

x, y, z = z, y, x

print(f'x - {x}')
print(f'y - {y}')
print(f'z - {z}')
