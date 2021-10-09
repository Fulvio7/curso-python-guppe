"""
6- Receba dois números, mostre na tela o maior deles, e também a
diferença entre ambos.
7- Mostre se os números forem iguais.
"""

n1 = float(input('Digite o valor de n1: '))
n2 = float(input('Digite o valor de n2: '))

diferenca = float

if n1 > n2:
    diferenca = n1 - n2
    print(f'{n1} é o maior.')
    print(f'A diferença entre eles é de {diferenca}.')
elif n1 < n2:
    diferenca = n2 - n1
    print(f'{n2} é o maior.')
    print(f'A diferença entre eles é de {diferenca}.')
else:
    print(f'{n1} e {n2} são iguais.')
    print(f'A diferença entre eles é zero.')

