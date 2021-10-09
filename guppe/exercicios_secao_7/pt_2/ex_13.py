"""
14- Gera uma matriz 4x4 com valores de 1 a 20. Escreva um programa que
transforme a matriz gerada numa matriz triangular inferior, ou seja,
atribuindo zero a todos os elementos acima da diagonal principal.
Imprima a matriz original e a matriz transformada.
"""

matriz, num = [[], [], [], []], 1

for i in range(4):
    for j in range(4):
        matriz[i].append(num)
        print(matriz[i][j], end=' ')
        num += 1
        if i < j:
            matriz[i][j] = 0
    print()
print()
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=' ')
    print()
