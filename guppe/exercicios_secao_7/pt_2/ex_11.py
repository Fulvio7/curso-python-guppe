"""
11- Leia uma matriz 3x3 elementos. Calcule a soma dos elementos que
estão na diagonal secundária.
"""

matriz, soma = [[], [], []], 0

print('Preencha a matriz')
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'M[{i},{j}] = ')))

        if i + j == 2:
            soma += matriz[i][j]

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print('')

print(f'Soma dos elementos na diagonal secundária: {soma}')
