"""
2- Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0
os demais elementos. Escreva a matriz ao final.
"""

matriz = [[], [], [], [], []]

for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=' ')
    print('')








