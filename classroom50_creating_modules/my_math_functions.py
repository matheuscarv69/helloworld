def sum_two_int(num1, num2):
    if not isinstance(num1, int):
        raise ValueError(f'{num1} is not an int, it is a {type(num1)}')

    if not isinstance(num2, int):
        raise ValueError(f'{num2} is not an int, it is a {type(num2)}')

    return num1 + num2


if __name__ == '__main__':
    print('Running a My Math Functions')

