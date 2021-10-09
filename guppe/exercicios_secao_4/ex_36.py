"""
36- Leia a altura[H] e o raio[R] de um cilindro circular, calcule seu
volume e imprima-o. A equação do volume do cilindro circular é:
V = pi * (R**2) * H
"""

import math

raio = float(input('Digite o valor do raio '))
altura = float(input('Digite o valor da altura '))

volume = math.pi * (raio ** 2) * altura

print(f'O volume do cilindro é {volume}')


