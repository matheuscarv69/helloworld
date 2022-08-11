
clientes = {
    'cliente1': {
      'nome': 'Matheus',
      'sobrenome': 'Carvalho'
    },
    'cliente2': {
        'nome': 'James',
        'sobrenome': 'Gosling'
    },
    'cliente3': {
        'nome': 'Guido',
        'sobrenome': 'Rossum'
    },
}

for cliente_key, cliente_value in clientes.items():
    print(f'{cliente_key}')

    # Segundo for para iterar dentro do dicionario mais interno
    for dados_key, dados_value in cliente_value.items():
        print(f'\t{dados_key} - {dados_value}')

