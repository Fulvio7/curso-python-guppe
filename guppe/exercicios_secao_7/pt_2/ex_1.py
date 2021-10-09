"""
1- Leia uma matriz 4x4, conte e escreva quantos valores maiores que
10 ela possui.
"""

matriz = [[], [], [], []]

print('Preencha a matriz: ')
for linha in range(4):
    for coluna in range(4):
        matriz[linha].append(int(input(f'M[{linha},{coluna}] = ')))

maiores_que_10 = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            maiores_que_10 += 1

print(f'A matriz M possui {maiores_que_10} números maiores que 10.')


