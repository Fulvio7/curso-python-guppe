"""
14- Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é:
R = G * pi / 180
"""
import math

graus = float(input('Digite um ângulo em graus '))

rad = graus * math.pi / 180

print('Convertendo para radianos temos: ')
print(f'{graus}º = {rad} rad ')
