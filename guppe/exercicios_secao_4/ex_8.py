"""
8- Leia uma temperatura em Kelvin e apresente-a convertida em
graus Celsius. A fórmula para conversão é:
C = K - 273.15
"""

kelvin = float(input('Digite uma temperatura em Kelvin '))

celsius = kelvin - 273.15

print('Convertendo para Celsius temos: ')
print(f'{kelvin} K = {celsius} ºC ')

