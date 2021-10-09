"""
20- Leia uma matriz 3x6 de valores reais.
a - Imprima a soma de todos os elementos das colunas ímpares;
b - Imprima a média aritmética dos elementos da segunda e da quarta
colunas;
c - Substitua os valores da sexta coluna pela soma dos valores das
colunas 1 e 2;
d - Imprima a matriz modificada.
"""

matriz = [[], [], []]
soma_impares, soma_2_e_4 = 0, 0

print('Preencha a matriz: ')
for i in range(3):
    for j in range(6):
        matriz[i].append(int(input(f'M[{i},{j}] = ')))

        if j % 2 == 1:
            soma_impares += matriz[i][j]

        if j == 2 or j == 4:
            soma_2_e_4 += matriz[i][j]

        if j == 5:
            matriz[i][5] = matriz[i][1] + matriz[i][2]

print('\nResultados:')
print(f'Soma de todos os elementos das colunas ímpares: {soma_impares}')
print(f'Média dos elementos das colunas 2 e 4: {soma_2_e_4/6}')
print('Matriz modificada: ')
for i in range(3):
    for j in range(6):
        print(matriz[i][j], end=' ')
    print()














