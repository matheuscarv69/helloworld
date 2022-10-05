"""
A função filter serve para filtrar coisas de acordo
com uma lambda

"""

from classroom44_map.datas import peoples

print('Find all peoples with age is greater than 18')


def filter_age_greater_18(people):
    if people['age'] >= 18:
        return True

    return False

all_peoples_greater_18 = filter(filter_age_greater_18, peoples)

for person in all_peoples_greater_18:
    print(person)
