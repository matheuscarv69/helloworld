"""

Lançando exceções

"""


def test_raise_custom_message_exception(num1, num2):

    if num2 == 0:
        raise ValueError("num2 can't be equal 0 - zero")

    return num1 / num2

try:
    print(test_raise_custom_message_exception(2, 0))

except ValueError as error:
    print('An error hurled: ', error)