"""
25- Leia uma área em acres e apresente-a convertida em metros quadrados.
A fórmula de conversão é:
M[m] = A[ac] / 0.000247
"""

acres = float(input('Digite uma área em acres '))

metros = acres / 0.000_247

print('Convertendo para metros quadrados temos: ')
print(f'{acres} ac = {metros} m ')

