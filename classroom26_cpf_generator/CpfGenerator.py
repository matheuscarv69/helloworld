from random import randint

num = str(randint(100000000, 999999999))

new_cpf = num

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
        d = '0' if 11 - (total % 11) > 9 else 11 - (total % 11)

        total = 0
        new_cpf += str(d)

print(new_cpf)
