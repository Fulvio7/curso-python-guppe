"""
32- Leia um número inteiro e imprima a soma do sucessor de seu triplo
com o antecessor de seu dobro.
"""

num = int(input('Digite um número inteiro '))

total = ((num * 3) + 1) + ((num * 2) - 1)

print(f'Jogando {num} nesta equação maluca temos: ')
print(f'(({num} * 3) + 1) + (({num} * 2) - 1) = {total} ')


