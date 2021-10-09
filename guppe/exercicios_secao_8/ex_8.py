"""
8- Faça uma função que receba os catetos a e b, e calcule a sua
hipotenusa. Equação:
hip = sqrt(a² + b²)
"""
from math import sqrt


def calcula_hipotenusa(cateto_a, cateto_b):
    hipotenusa = sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa


catA = int(input('Digite o valor do cateto A: '))
catB = int(input('Digite o valor do cateto B: '))

print(f'A hipotenusa de {catA} e {catB} é: {calcula_hipotenusa(catA,catB)}')





