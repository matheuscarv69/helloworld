import my_math_functions

total = my_math_functions.sum_two_int(10, 20)

print(f'The total is: {total}')

try:
    total_2 = my_math_functions.sum_two_int(2.45, 15)

    print(f'The total_2 is: {total_2}')

except ValueError as conversion_error:
    print(f'An error ocurred: {conversion_error}')
