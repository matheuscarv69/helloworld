"""

Vamos ler o arquivo que contém o json e depois convertê-lo em
dictionary

"""

import json

with open(file='peoples.json', mode='r') as file:
    peoples_json = file.read()

    dictionary_peoples = json.loads(peoples_json)

for key, value in dictionary_peoples.items():

    print(f'{key}')
    for key2, value2 in value.items():
        print(f'\t{key2} : {value2}')

    print()
