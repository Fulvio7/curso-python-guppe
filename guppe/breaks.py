"""
Break

Utilizado para sair de loops de maneira planejada.

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saí do loop')

"""

# Exemplo 2
while True:
    comando = input('Digite "sair" para sair:')
    if comando == 'sair':
        break

