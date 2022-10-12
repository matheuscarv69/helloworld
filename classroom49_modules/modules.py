"""
Módulos padrão do Python

Módulos são arquivos .py ( que contém código python) e servem para expandir
as funcionalidades padrão da linguagem.

"""

from sys import platform  # importando do módulo 'sys' a função 'platform'
import random  # importando o módulo random completo
from random import randint  # importando somente a função 'randint'

print(f'Current O.S: {platform}')
print(f'Generate random number - random.randint: {random.randint(0,10)}')
print(f'Generate random number - randint: {randint(10,20)}')

