"""

Operador Ternário

"""

logged_user = True

print('if else')
# if else normal
if logged_user:
    msg = 'Logged'
else:
    msg = 'Unlogged'

print(msg)

# operador ternário
print()
print('ternary operator ')
msg = 'logged' if logged_user else 'unlogged'
print(msg)
