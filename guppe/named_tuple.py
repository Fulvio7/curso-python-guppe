"""
Module Collections - Named Tuple

# Recaptulando
tupla = 1, 2, 3
print(tupla[1])

Named Tuple: são tuplas diferenciadas, onde, especificamos um nome
para a mesma e também seus parâmetros.

"""
# Importando
from collections import namedtuple

# Precisamos definir o seu nome e seus parâmetros
# Forma 1 - Declaração Named Tuple
#                      Nome       Parâmetros
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple
#                      Nome       Parâmetros separados por vírgula
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração Named Tuple
#                      Nome       Parâmetros em lista
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando
ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados
# Forma 1
print(ray[0])  # idade
print(ray[1])  # nome
print(ray[2])  # raça

# Forma 2
print(ray.idade)
print(ray.nome)
print(ray.raça)


