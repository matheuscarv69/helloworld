"""

Vamos criar um dictionary que contém informações de pessoas
e o formateremos em um json, em seguida ele será salvo em um arquivo

"""

import json

peoples = {
    'people_1': {
        'name': 'Brian',
        'age': 34
    },
    'people_2': {
        'name': 'Roman',
        'age': 29
    }
}

peoples_json = json.dumps(peoples, indent=True)

with open(file='peoples.json', mode='w+') as file:

    file.write(peoples_json)

