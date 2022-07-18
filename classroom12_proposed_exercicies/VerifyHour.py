"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

time = input('What time is it? ')

try:
    time = float(time.replace(':', '.'))

    if 23 >= time >= 0 :

        # if time >= 0 and time < 12:
        if 0 <= time < 12:
            print('Good Morning!')
        elif 12 <= time < 18:
            print('Good Aftermoon')
        else:
            print('Good Night')
    else:
        print('Time should to be between 0 - 23')

except:
    print('Error')
