"""

Usando o gerenciador de context - with

Não precisamos fechar o arquivo

-x-
Modos:

a - append - Ele adiciona coisas no arquivo, sem apagar as informações
já existentes.

"""

with open('text_file.txt', 'a+') as file:
    file.write('\n')
    file.write('Line 4\n')
    file.write('Line 5\n')
    file.write('Line 6\n')

    file.seek(0)

    print(file.read())
    