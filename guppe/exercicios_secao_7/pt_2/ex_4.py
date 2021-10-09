"""
4- Leia uma matriz 4x4, imprima a matriz e retorne a localização
(linha e coluna) do maior valor.
"""

matriz = [[], [], [], []]
maior = int()

print('Preencha a matriz M:')
for i in range(4):
    for j in range(4):
        matriz[i].append(int(input(f'M[{i},{j}] = ')))

        if i == 0 and j == 0:
            maior = matriz[i][j]
        else:
            if maior < matriz[i][j]:
                maior = matriz[i][j]

print('\nMatriz M:')
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=' ')
    print('')

print('Maior elemento: ', maior)


