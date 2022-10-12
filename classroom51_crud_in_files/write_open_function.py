"""
doc - https://docs.python.org/3/library/functions.html#open

Existem algumas formas de se manipular arquivos em python
a forma a seguir é uma das mais simples

- open() - função built-in do python, é utilizada para criar arquivos,
como 1st param ela recebe o nome do arquivo e como 2nd param recebe
o modo que se quer trabalhar com o respectivo arquivo.

default mode - r

Veja os modos na documentação.

w+ -> modo de escrita (writer), + -> diz que queremos ler o arquivo também

- seek() - essa função é utilizada para mudar a posição do cursor dentro
de um arquivo.
Ex.: Acaba-se de criar um arquivo e deseja-se ler o conteúdo desse arquivo
se printar o arquivo sem usar o seek, nada será impresso no console, pois o
cursor estará na última posição do arquivo, a solução seria:

file.seek(0,0) - 1st é o offset e 2nd é o whence é a relatividade da posição
normalmente usa-se 0, com isso o cursor voltará para o início do arquivo

Toda vez que for preciso ler o arquivo do inicio usa-se essa função seek

"""

file = open('test_file.txt', 'w+')

file.write('Line 1\n')
file.write('Line 2\n')
file.write('Line 3\n')

file.seek(0, 0)

print('Reading lines: ')
print(file.read())

print('----------------------------')

file.seek(0, 0)

print('Reading individual line: ', file.readline(), end='')
print('Reading individual line: ', file.readline(), end='')
print('Reading individual line: ', file.readline(), end='')

print('----------------------------')

file.seek(0, 0)

print('Getting a List of lines at file')
list_of_lines = file.readlines()

print(list_of_lines)

file.close()  # never forget to close the file
