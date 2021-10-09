"""
4- Faça uma função para verificar se um número é um quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que poode ser
expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...
"""
from math import sqrt


def testa_quadrado_perfeito(num):
    if int(sqrt(num)) == sqrt(num):
        return f'{num} é quadrado perfeito.'
    return f'{num} não é quadrado perfeito.'


numero = -1

while numero < 0:
    numero = int(input('Digite um número inteiro não negativo: '))

print(testa_quadrado_perfeito(numero))







