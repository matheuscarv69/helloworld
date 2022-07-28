"""

CPF = 168.995.350-09

1 * 10 = 10                      |      0  1 * 11 = 10
6 * 9 = 54                       |      1  6 * 10 = 54
8 * 8 = 64                       |      2  8 *  9 = 64
9 * 7 = 63                       |      3  9 *  8 = 63
9 * 6 = 54                       |      4  9 *  7 = 54
5 * 5 = 25                       |      5  5 *  6 = 25
3 * 4 = 12                       |      6  3 *  5 = 12
5 * 3 = 15                       |      7  5 *  4 = 15
0 * 2 = 0                        |      8  0 *  3 = 0
      + 297                      |      9  0 *  2 = 0
                                 |                + 343
11 - (297 % 11) = 11             |        11 - (343 % 11) = 9
11 > 9 = 0                       |
Digito 1 = 0                     |      Digito 2 = 9
"""

# ind  0123456789
cpf = '16899535009'
new_cpf = cpf[0:9]

total = 0
reverse_count = 10

for index in range(19):

    if index > 8:
        # 9 - 9 = 0 -> isso faz com que o ponteiro do index suba novamente
        # para fazer o segundo calculo
        index -= 9  # = 0

    # print(new_cpf[index], index, reverse_count, sep=' - ')
    total += int(new_cpf[index]) * reverse_count

    reverse_count -= 1
    if reverse_count < 2:
        # reverse_count = 1 -> faz com que o "ponteiro" do reverse_count suba tambem para 11
        # para comecar o segundo calculo
        reverse_count = 11

        # ternario para verificar se o modulo do total eh maior que 9
        d = '0' if (11 - (total % 11)) > 9 else '9'
        total = 0
        new_cpf += d

print(new_cpf)
