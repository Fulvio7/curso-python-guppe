"""
26- Leia uma área em metros quadrados e apresente-a convertida em hectares.
A fórmula de conversão é:
H[ha] = M[m] * 0.0001
"""

metros = float(input('Digite uma área em metros quadrados'))

hectares = metros * 0.0001

print('Convertendo para hectares temos: ')
print(f'{metros} m² = {hectares} ha ')

