"""
24- Leia uma área em metros quadrados e apresente-a convertida em acres.
A fórmula de conversão é:
A[ac] = M[m] * 0.000247
"""

metros = float(input('Digite uma área em metros quadrados '))

acres = metros * 0.000_247

print('Convertendo para acres temos: ')
print(f'{metros} m = {acres} ac')
