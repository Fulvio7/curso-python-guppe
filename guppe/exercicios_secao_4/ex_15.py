"""
15- Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é:
G = R * 180 / pi
"""

import math

rad = float(input('Digite um ângulo em radianos '))

graus = rad * 180 / math.pi

print('Convertendo para graus temos: ')
print(f'{rad} rad = {graus}º ')
