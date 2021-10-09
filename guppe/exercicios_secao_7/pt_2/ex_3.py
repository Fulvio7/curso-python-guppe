"""
3- Faça um programa que preencha uma matriz 4x4 com o produto entre os
índices da posição do elemento. Ao final, imprima a matriz.
"""

matriz = [[], [], [], [], []]

for i in range(4):
    for j in range(4):
        matriz[i].append(i*j)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print('')




