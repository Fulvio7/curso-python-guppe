"""
22- Leia duas matrizes (A e B) 3x3 e calcule C = A * B
"""

alpha, beta, gamma = [[], [], []], [[], [], []], [[], [], []]

print('Preencha a matriz A')
for i in range(3):
    for j in range(3):
        alpha[i].append(int(input(f'A[{i},{j}] = ')))

print('Preencha a matriz B')
for i in range(3):
    for j in range(3):
        beta[i].append(int(input(f'B[{i},{j}] = ')))

print('\nC = A x B')
for i in range(3):
    for j in range(3):
        num = 0
        for k in range(3):
            num += alpha[i][k] * beta[k][j]

        gamma[i].append(num)
        print(gamma[i][j], end=' ')
    print()









