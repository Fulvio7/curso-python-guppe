"""
18- Leia uma matriz 3x3 de números inteiros. Em seguida, gere um array
unidimensional pela soma dos números de cada coluna da matriz. Ao
final imprima este array.
"""

matriz = [[], [], []]
vetor = []

print('Preencha a matriz: ')
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'M[{i},{j}] = ')))
    vetor.append(sum(matriz[i]))

print(vetor)





