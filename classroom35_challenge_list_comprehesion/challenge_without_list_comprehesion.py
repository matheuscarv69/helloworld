"""
string = '0123456789012345678901234567890123456789012345678901234567890123456789'
list_separated_nums = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
last_modification = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'

"""

# string = '0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0123456789'
string = '0123456789012345678901234567890123456789012345678901234567890123456789'

list_separated_nums = []
group_of_nums = ''

for char_num in string:

    if char_num == '0' and group_of_nums.endswith('9'):
        list_separated_nums.append(group_of_nums)
        group_of_nums = ''

    group_of_nums += char_num

print(list_separated_nums)

text_aux = ''

for counter, value in enumerate(list_separated_nums):

    if counter != len(list_separated_nums) - 1:
        text_aux += value + '.'
    else:
        text_aux += value

print(text_aux)
