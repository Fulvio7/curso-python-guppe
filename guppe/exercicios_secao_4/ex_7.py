"""
7- Leia uma temperatura em graus Fahrenheit e apresente-a convertida
em graus Celsius. A fórmula de conversão é:
C = 5 * (F-32) / 9
"""
fahrenheit = float(input('Digite uma temperatura em Fahrenheit '))

celsius = 5 * (fahrenheit - 32) / 9

print('Convertendo para Celsius temos: ')
print(f'{fahrenheit} ºF = {celsius} ºC ')
