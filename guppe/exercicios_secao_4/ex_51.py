"""
51- Escreva um programa que leia as coordenadas x e y de pontos no
R² e calcule sua distância da origem (0,0).
"""
from math import sqrt

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

dist = sqrt((x ** 2) + (y ** 2))

print(f'A distância até a origem (0,0) é: {dist:.4f}')
