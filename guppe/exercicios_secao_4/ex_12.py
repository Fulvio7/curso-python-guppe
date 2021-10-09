"""
12- Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é:
K[km] = 1.61 * M[mi]
"""

mi = float(input('Digite uma distância em milhas '))

km = mi * 1.61

print('Convertendo para km temos: ')
print(f'{mi} mi = {km} km')


