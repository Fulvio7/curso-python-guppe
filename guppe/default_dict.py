"""
Module Collections - Default Dict

# Recaptulando
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # KeyError

Default Dict - informamos um valor default, podendo utilizar um
lambda. Este valor será utilizado sempre que não houver um valor
definido.
Caso a chave não exista, não dá KeyError, mas atribui o default.

Lambdas são funções sem nome que podem ou não receber parâmetros
de entrada e retorna valores.
"""
# Importando
from collections import defaultdict
dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])

