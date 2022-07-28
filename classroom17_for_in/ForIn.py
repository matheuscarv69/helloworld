"""

For in em Python

Iterando strings com for
Funcao range (start=0, stop, step1)

"""

text = 'python'

print('Default For')
# Usando for para percorrer o texto
for letter in text:
    print(letter)

print()
print('For with enumerate')
# Usando enumerate para pegar o indice de cada loop
for index, letter in enumerate(text):
    print(f'index: {index} - {letter}')

print()
print('For with range')
# Usando a funcao range(start=0, stop, step=1)
for number in range(10):
    print(f'number: {number}')

print()
print('For using range(start, stop, step)')
# Usando a funcao range(start=0, stop, step=1)
for number_2 in range(0, 10, 2):
    print(f'number: {number_2}')