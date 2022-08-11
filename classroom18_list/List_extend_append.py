"""
Listas em Python

Fatiamento - Slicing

append, insert, pop, del, clear, extend, +
min, max,
range

"""
#         0    1    2    3    4
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
#    -    5    4    3    2    1

print(list1)
print(list2)
print(f'Concatenando listas usando + : {list1 + list2}')

print()
print()

print(list1)
print(list2)

list1.extend(list2)

# extend - adiciona uma multiplos valores no final de uma lista de forma que todos os elementos estejam juntos. ex: list2 foi adicionada na list1
# resultado: [1, 2, 3, 4, 5]

print(f'Usando a funcao extend: {list1}')

print()
print()

list1 = ['a', 'b', 'c']

print(list1)
print(list2)

list2.append(list1)
# append - adiciona lista/valores no final de outra lista, em caso de uma lista sendo passada
# para o append, na lista principal ela aparecera como um item com elementos dentro
# resultado: [1, 2, 3, [4, 5]]

print(f'Usando a funcao append: {list2}')

print()
print()

l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']

print(f'l1 index[1] - {l1[1]}')

l1.insert(1, 'estive aqui')
# insere elementos em uma determinada posicao da lista

print(f'l1 apos insert index[1] - {l1[1]}')

print(f'Adicionando itens em qualquer posicao na lista com o insert: {l1}')

l1.pop(1)
# remove um elemento de uma determinada posicao na lista
# se nao passar nenhum indice, o ultimo item eh removido

print(f'Removendo um item em uma determinada posicao da lista com o pop: {l1}')

print()
print()

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l3)

del (l3[0:4])
# eh preciso informar o range para delecao dos itens na lista, no exemplo comeca em 0 e vai ateh o 4 item
# expected: 5,6,7,8,9,10

print(f'Excluindo um intervalo de itens dentro de uma lista com o del: {l3}')
