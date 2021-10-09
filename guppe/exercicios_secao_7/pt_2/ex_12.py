"""
12- Leia uma matriz 3x3 elementos. Calcule e imprima a sua transposta.
"""

matriz, transposta = [[], [], []], [[], [], []]

print('Preencha a matriz')
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'M[{i},{j}] = ')))

for j in range(3):
    for i in range(3):
        transposta[j].append(matriz[i][j])

print('\nMatriz')
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print('')

print('\nMatriz Transposta')
for i in range(3):
    for j in range(3):
        print(transposta[i][j], end=' ')
    print('')

