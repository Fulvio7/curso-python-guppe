"""
17- Leia um comprimento em centímetros e apresente-o convertido
para polegadas. A fórmula de conversão é:
P[pol] = C[cm] / 2.54
"""

cm = float(input('Digite um comprimento em centímetros '))

pol = cm / 2.54

print('Convertendo para polegadas temos: ')
print(f'{cm} cm = {pol} pol')
