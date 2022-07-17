"""

Conditions

and (true + true) = true
or (true + false) = false
not (not true) = false

in
not in

"""

print('Testing logical operator In, Not In:')
name = input('Enter your name: ')

if 'a' in name:
    print(f'The letter "A" exist in your name: {name}')
elif 'z' not in name:
    print(f'But the letter "Z" not exist in your name: {name}')

print('\nTesting logical operators And, Or, Not')

number1 = int(input('Enter a number1: '))

if number1 == 2 and number1 > 0:
    print(f'{number1} == 2 -> {number1 == 2}')
elif number1 > 2 or number1 < 2:
    print(f'{number1} > 2 -> {number1 > 2}, {number1} < 2 -> {number1 < 2}')

print()

number2 = int(input('Enter a number2: '))

if not number2 > number1:
    print(f'number2: {number2} is not greater than number1: {number1}')
    #  number2 > number1 == true, not number2 > number1 = false
    print(f'number2: {number2} "not number2 > number1" number1: {number1} = {not number2 > number1}')
else:
    print(f'number2: {number2}  > number1: {number1} = {number2 > number1}'
          f'not number2: {number2} > number1: {number1} = {not number2 > number1}')
