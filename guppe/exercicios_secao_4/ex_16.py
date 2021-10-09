"""
16- Leia um comprimento em polegadas e apresente-o convertido para
centímetros. A fórmula de conversão é:
C[cm] = 2.54 * P[pol]
"""

pol = float(input('Digite um comprimento em polegadas '))

cm = pol * 2.54

print('Convertendo para centímetros temsos: ')
print(f'{pol} pol = {cm} cm ')
