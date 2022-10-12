"""

2 — Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.

"""

print('Sum Function\n')


def sum_function(x, y, z):
    return x + y + z


print(sum_function(x=1, y=2, z=3))
print()

x = int(input('Enter X value: '))
y = int(input('Enter Y value: '))
z = int(input('Enter Z value: '))

print(f'Your sum is: {sum_function(x, y, z)}')
