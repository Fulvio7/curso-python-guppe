"""
1- Receba dois números e mostre qual deles é maior.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é o maior.')
elif n1 < n2:
    print(f'{n2} é o maior.')
else:
    print('Os dois números são iguais.')

