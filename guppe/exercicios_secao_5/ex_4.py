"""
4- Faça um programa que leia um número, caso ele seja positivo,
calcule e mostre: sua raiz quadrada e também elevado ao quadrado.
"""
from math import sqrt
number = float(input('Digite um número positivo: '))

if number > 0:
    number_sqrt = sqrt(number)
    number_raised = number ** 2
    print(f'A raiz quadrada de {number} é {number_sqrt:.2f}')
    print(f'{number} ao quadrado é {number_raised}')
elif number < 0:
    print('Você digitou um número negativo.')
else:
    print('Você digitou 0.')

