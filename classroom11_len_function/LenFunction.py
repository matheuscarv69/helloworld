"""

len

Counting Character

"""

name = input('Enter your name: ')
print(f'Your name is {name} and they have {len(name)} characters')

password = input('Enter your password: ')

if len(password) < 8:
    print('Invalid password, they are than 8 characters')
