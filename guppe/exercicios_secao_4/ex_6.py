"""
6- Leia uma temperatura em graus Celsius e apresente-a convertida em
Fahrenheit. A fórmula de conversão é:
F = C * (9/5) + 32
"""
celsius = float(input('Digite uma temperatura em graus Celcius '))

fahrenheit = celsius * (9/5) + 32

print('Convertendo para Fahrenheit temos: ')
print(f'{celsius} ºC = {fahrenheit} ºF ')
