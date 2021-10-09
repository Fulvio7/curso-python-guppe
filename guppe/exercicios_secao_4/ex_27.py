"""
27- Leia uma área em hectares e apresente-a convertida em metros quadrados.
A fórmula de conversão é:
M[m] = H[ha] * 10000
"""

hectares = float(input('Digite uma área em hectares '))

metros = hectares * 10_000

print('Convertendo para metros temos: ')
print(f'{hectares} ha = {metros} m²')

