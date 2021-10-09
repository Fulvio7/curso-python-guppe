"""
5- Faça uma função e um programa de teste para o cálculo do volume de
uma esfera. Sendo que o raio é passado por parâmetro.
Fórmula do volume da esfera:
V = 4/3 * pi * R³
"""
import math


def volume_esfera(raio):
    volume = 4/3 * math.pi * raio**3
    return volume


print('Cálculo do Volume de uma Esfera')
raio_digitado = float(input('Digite o tamanho do raio: '))

print(volume_esfera(raio_digitado))




