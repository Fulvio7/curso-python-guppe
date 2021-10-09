"""
23- Leia uma matriz A 3x3 e calcule B = A².
"""

alfa, beta = [[], [], []], [[], [], []]

print('Preencha a matriz A')
for i in range(3):
    for j in range(3):
        alfa[i].append(int(input(f'A[{i},{j}] = ')))

print('\nB = A²')
for i in range(3):
    for j in range(3):
        num = 0
        for k in range(3):
            num += alfa[i][k] * alfa[k][j]
        beta[i].append(num)
        print(beta[i][j], end=' ')
    print()








