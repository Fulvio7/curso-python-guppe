"""
Estruturas lógicas
and, or, not e is
e, ou, não e é

Operadores unários:
- not

Operadores binários:
- and, or, is
"""

ativo = True
logado = True

# not, inverte o valor
if not ativo:
    print('Você precisa ativar a sua conta.')
else:
    print('Bem-vindo usuário!')

# and, ambos precisam ser True
if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar a sua conta.')

# or, um deles precisa ser True
if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar a sua conta.')

# is, retorna se uma coisa é aquilo
# verifica se ativo é falso e retorna o resultado disso
print(ativo is False)






