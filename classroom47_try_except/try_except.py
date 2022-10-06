"""
try e except são usados para tratar exceções no código

ex.:

print(a) -> gera um erro no console

Curiosidades do Try:

Ele aceita 'else', onde o mesmo sempre será executado caso o try
não lance nenhum erro

finally -> sempre é executado
"""

print('A simple form for processing an exception, but isn`t recommended')
try:

    print(a)

except:
    print('An Error')

print()

print('Processing a specified exception - NameError')

try:

    print(b)  # throw NameErrorException

except NameError as error:
    print('Error: ', error)

except Exception as generic_error:
    print('Unexpected error: ', generic_error)


print()

print('Processing else after try block')

try:
    a = [1,2,3]

    print(a)

except Exception as error:
    print('Error: ', error)

else:
    print('Else is executed: a:', a)

finally:
    print('Forever executed')


