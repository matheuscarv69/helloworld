"""

CPF = 168.995.350-09

1 * 10 = 10                      |        1 * 11 = 10
6 * 9 = 54                       |        6 * 10 = 54
8 * 8 = 64                       |        8 *  9 = 64
9 * 7 = 63                       |        9 *  8 = 63
9 * 6 = 54                       |        9 *  7 = 54
5 * 5 = 25                       |        5 *  6 = 25
3 * 4 = 12                       |        3 *  5 = 12
5 * 3 = 15                       |        5 *  4 = 15
0 * 2 = 0                        |        0 *  3 = 0
      + 297                      |        0 *  2 = 0
                                 |               + 343
11 - (297 % 11) = 11             |       11 - (343 % 11) = 9
11 > 9 = 0                       |
Digito 1 = 0                     |      Digito 2 = 9
"""

cpf = '16899535009'

*initial_number, digit_x, digit_y = cpf

# function - calculo 1
result_calculate_1 = 0

for index, regressive_counter in enumerate(range(10, 1, -1)):
    result_calculate_1 += int(initial_number[index]) * regressive_counter

# formula 1
digit_1 = str(0) if 11 - (result_calculate_1 % 11) >= 9 else 'Invalid CPF'

# function - calculo 2
result_calculate_2 = 0

for index, regressive_counter in enumerate(range(11, 1, -1)):

    if index == 8:
        result_calculate_2 += int(initial_number[index]) * regressive_counter
        break

    result_calculate_2 += int(initial_number[index]) * regressive_counter

# formula 2
digit_2 = str(11 - (result_calculate_2 % 11))

cpf_string = ''

counter = 0
for index in range(0, 9, 1):
    cpf_string += initial_number[index]

    counter += 1
    if counter == 3:
        cpf_string += '.'
        counter = 0

cpf_string = cpf_string.removesuffix('.')

cpf_string += '-' + digit_1 + digit_2

print(cpf_string)
