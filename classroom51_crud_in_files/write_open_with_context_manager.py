"""

Usando o gerenciador de context - with

Não precisamos fechar o arquivo

"""

with open('test_file.txt', 'w+') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

    file.seek(0)

    print(file.read())
