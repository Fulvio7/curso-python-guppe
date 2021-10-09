"""
7- Faça uma função que receba uma temperatura em graus Celsius e
retorne-a convertida em graus Fahrenheit. Equação:
F = C * (9/5) + 32
"""


def celsius_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


print('Conversor Celsius para Fahrenheit')
cel = int(input('Digite a temperatura em graus Celsius: '))

print(f'{cel}°C = {celsius_fahrenheit(cel)}°F')



