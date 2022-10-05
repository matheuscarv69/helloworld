"""
Map possui o comportamento parecido com list comprehesion

map(function, iterable/list...) - retorna um iterable
"""

from datas import peoples

print('Show all people')
print(type(peoples))

for people in peoples:
    print(f'\t{people}')

print()
print('Creating list with name of peoples using Map function')

list_name_of_peoples = map(lambda people: people['name'], peoples)

print(list_name_of_peoples)

for name in list_name_of_peoples:
    print(f'\t{name}')

print()

"""
 É possivel adicionar novas chaves em um dicionario e ainda manter a estrutura
 inicial dele, seguindo a mesma lógica do exemplo de mapping com produtos
"""


print('Adding new key in dict, using map function ')


def adding_new_key_of_age_plus_ten_years(people):
    people['new_age_plus_ten_years'] = people['age'] + 10

    return people


new_peoples_list_with_new_key = map(adding_new_key_of_age_plus_ten_years, peoples)

for people_with_new_age_key in new_peoples_list_with_new_key:
    print(f'\t{people_with_new_age_key}')