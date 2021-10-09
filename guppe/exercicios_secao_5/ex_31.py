"""
31- Receba a altura e o peso de uma pessoa. Classifique-a através
da tabela abaixo e mostre o resultado.
ALTURA              PESO
                <= 60   > 60 e <= 90    > 90
< 1,20          A       D               G
de 1,20 à 1,70  B       E               H
> 1,70          C       F               I
"""

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

print('Sua classificação é: ')

if altura < 1.2:
    if peso <= 60:
        print('A')
    elif peso > 90:
        print('G')
    else:
        print('D')

elif altura > 1.7:
    if peso <= 60:
        print('C')
    elif peso > 90:
        print('I')
    else:
        print('F')
else:
    if peso <= 60:
        print('B')
    elif peso > 90:
        print('H')
    else:
        print('E')

