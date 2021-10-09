"""
5- Leia uma matriz 5x5. Leia também um valor X. O programa deverá fazer
uma busca desse valor na matriz e, ao final, escrever a localização
(linha e coluna) ou uma mensagem de 'não encontrado'.
"""

matriz = [[], [], [], [], []]
pos_de_x = []

print('Preencha a matriz:')
for i in range(4):
    for j in range(4):
        matriz[i].append((int(input(f'M[{i},{j}] = '))))

valor_x = int(input('\nDigite o valor X: '))

for i in range(4):
    for j in range(4):
        if matriz[i][j] == valor_x:
            pos_de_x.append(str(f'M[{i},{j}]'))

if len(pos_de_x) > 0:
    print(f'\nPosições onde encontramos X = {valor_x}: ')
    for i in pos_de_x:
        print(i)
else:
    print(f'X = {valor_x} não encontrado.')



