"""
18- Leia um volume em metros cúbicos e apresente-o convertido em litros.
A fórmula de conversão é:
L[l] = 1000 * M[m³]
"""

m_cub = float(input('Digite um volume em metros cúbicos '))

litros = m_cub * 1_000

print('Convertendo para litros temos: ')
print(f'{m_cub} m³ = {litros} l ')

