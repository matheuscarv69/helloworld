"""

Lançando exceções

raise -> repassa a exceção para frente

"""


def divide(num1, num2):

    try:
        return num1 / num2

    except ZeroDivisionError as division_error:
        print('An Error hurled: ', division_error)

        raise  # A exceção esta sendo passada adiante


try:
    print(divide(2, 0))

except ZeroDivisionError as error:
    print('Error: ', error)