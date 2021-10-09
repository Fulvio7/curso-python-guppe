"""
6- Leia duas matrizes 4x4. Escreva uma terceira matriz com os maiores
valores de cada posição das matrizes lidas.
"""

mat_a = [[], [], [], []]
mat_b = [[], [], [], []]
mat_c = [[], [], [], []]

print('Preencha Matriz A:')
for i in range(4):
    for j in range(4):
        mat_a[i].append(int(input(f'A[{i},{j}] = ')))

print('Preencha Matriz B:')
for i in range(4):
    for j in range(4):
        mat_b[i].append(int(input(f'B[{i},{j}] = ')))

        if mat_a[i][j] > mat_b[i][j]:
            mat_c[i].append(mat_a[i][j])
        else:
            mat_c[i].append(mat_b[i][j])

print(f'\nMatriz C com os maiores elementos de cada posição:')
for i in range(4):
    for j in range(4):
        print(mat_c[i][j], end=' ')
    print('')





















