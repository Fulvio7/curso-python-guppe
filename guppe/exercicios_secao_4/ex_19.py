"""
19- Leia um volume em litros e apresente-o convertido para metros cúbicos.
A fórmula de conversão é:
M[m³] = L[l] / 1000
"""

litros = float(input('Digite um volume em litros '))

m_cub = litros / 1_000

print('Convertendo para metros cúbicos temos: ')
print(f'{litros} l = {m_cub} m³ ')


