"""
19- Faça um programa para verificar se um determinado número inteiro é
divísivel por 3 ou por 5, mas não simultaneamente pelos dois.
"""

num = int(input('Digite um número inteiro: '))

if num % 3 == 0 and num % 5 == 0:
    print('Fim de programa.')
elif num % 3 == 0:
    print(f'{num} é divisível por 3.')
elif num % 5 == 0:
    print(f'{num} é divisível por 5.')
else:
    print('Fim de programa.')

