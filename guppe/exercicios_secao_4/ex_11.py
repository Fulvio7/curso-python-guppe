"""
11- Leia uma velocidade em m/s em apresente-a convertida em km/h.
A fórmula de conversão é:
K[km/h] = M[m/s] * 3.6
"""

m_por_s = float(input('Digite uma velocidade em m/s '))

km_por_h = m_por_s * 3.6

print('Convertendo para kh/h temos: ')
print(f'{m_por_s} m/s = {km_por_h} km/h ')
