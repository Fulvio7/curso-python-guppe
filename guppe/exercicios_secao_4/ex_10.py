"""
10- Leia uma velocidade em km/h e apresente-a convertida para m/s.
A fómula de conversão é:
M[m/s] = K[km/h] / 3.6
"""

km_por_h = float(input('Digite uma velocidade em km/h '))

m_por_s = km_por_h / 3.6

print('Convertendo para m/s temos: ')
print(f'{km_por_h} km/h = {m_por_s} m/s ')

