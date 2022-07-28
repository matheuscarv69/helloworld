"""

For / Else

"""

list_var = ['acorda', 'pedrinho', 'que ', 'hoje', 'tem', 'campeonato']

# Forma antes de usar o For / Else

print('Before use For/Else\n')
for name in list_var:
    if name.lower().startswith('h'):
        print(f'This word "{name}" start with "h"')
    else:
        print(f'This word "{name}" not start with "h"')

# Usando For / Else
print('\nAfter use For/Else\n')
for name in list_var:
    if name.lower().startswith('h'):
        print(f'This word: "{name}" start with "h"')
        break
else:
    # Esse bloco so eh executado quando nao existe nenhuma palavra na lista com h
    print('In list_var not exist a word not start with "h"')
