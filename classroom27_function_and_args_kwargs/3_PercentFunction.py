"""

3 — Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.

"""

print('Percent Function\n')


# 10% of 150 = 15
# 15 + 150 = 165


def percent_function(value, percent):
    percent_value = value * (percent / 100)
    return value + percent_value


print(percent_function(value=150, percent=10))
print()

value = int(input('What your value? - '))
desired_percent = float(input('What your desired percent? - '))

print(f'You have {percent_function(value=value, percent=desired_percent)}')
