"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

===================

resultado
lista_soma  = [2, 4, 6, 8]

"""

# step 1 - generate new list with pair values of list A and B

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

pair_values_list = list(zip(list_a, list_b))
print(pair_values_list)

sum_list = [value_a + value_b for (value_a, value_b) in pair_values_list]
# sum_list = [value_a + value_b for value_a, value_b in zip(list_a, list_b)] // outra forma

print(sum_list)
