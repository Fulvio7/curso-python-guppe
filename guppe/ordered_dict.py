"""
Module Collections - Ordered Dict

Em um dicionário comum a ordem de inserção não é garantido.

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

No OrderedDict garantimos a ordem de inserção dos elementos
no dicionário.

# Importando
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
from collections import OrderedDict

# Diferenças entre dict e OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> dicionário comum não tem ordenação

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> ordereddict leva a ordem em consideração

