"""

Lambda Expression - funcoes anonimas

"""

print('Traditional Function')


def calc(x, y):
    return x * y


z = calc(x=2, y=5)
print(f'calc function: 2 * 5 = {z}')

print()

print('Lambda Function')

a = lambda b, c: b * c

print(f'lamda function: 2 * 2 = {a(b=2, c=2)}')
