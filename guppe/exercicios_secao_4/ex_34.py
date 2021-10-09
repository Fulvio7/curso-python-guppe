"""
34- Leia o raio de um círculo, calcule e imprima a sua área.
A área do círculo é dada pela equação:
A = pi * (R ** 2)
"""

import math

raio = float(input('Digite o valor do raio do círculo '))

area = math.pi * (raio ** 2)

print(f'A área do círculo de raio {raio} é {area:.4f}')
