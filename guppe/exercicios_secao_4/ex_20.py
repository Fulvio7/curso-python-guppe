"""
20- Leia uma massa em quilogramas e apresente-a convertida em libras.
A fómula de conversão é:
L[lb] = K[kg] / 0.45
"""

kg = float(input('Digite uma massa em quilogramas: '))

lb = kg / 0.45

print('Convertendo para libras temos: ')
print(f'{kg} kg = {lb} lb ')

