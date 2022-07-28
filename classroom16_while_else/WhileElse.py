"""
while / else

contadores
acumuladores

"""

contador = 1
acumulador = 1

while contador <= 10:
    print(f'contador: {contador} | acumulador: {acumulador}')
    acumulador += contador
    contador += 1
else:
    print('Amigo estou aqui')