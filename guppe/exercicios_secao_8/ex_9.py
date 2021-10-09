"""
9- Faça uma função que receba a altura e o raio de um cilindro circular
e retorne o volume do cilindro. Equação:
V = pi * raio² * altura
"""
from math import pi


def volume_cilindro(altura, raio):
    volume = pi * altura * raio**2
    return volume


print('Calcula o Volume de um Cilindro')
alt = float(input('Digite a altura do cilindro: '))
rai = float(input('Digite o raio do cilindro: '))

print(f'Volume = {volume_cilindro(alt, rai)}')







