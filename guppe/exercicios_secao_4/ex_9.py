"""
9- Leia uma temperatura em graus Celsius e apresente-a convertida
em Kelvin. A fórmula de conversão é:
K = C + 273.15
"""

celsius = float(input('Digite uma temperatura em grau Celsius '))

kelvin = celsius + 273.15

print('Convertendo para Kelvin temos: ')
print(f'{celsius} ºC = {kelvin} K ')
