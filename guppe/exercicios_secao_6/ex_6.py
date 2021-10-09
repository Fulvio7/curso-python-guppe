"""
6- Leia 10 inteiros e imprima a sua média.
"""
soma = int()

print('=== MÉDIA DE 10 NÚMEROS INTEIROS ===')
for i in range(1, 11):
    num = int(input(f'Digite n{i}: '))
    soma += num

media = soma / 10

print(f'Média = {media}')
