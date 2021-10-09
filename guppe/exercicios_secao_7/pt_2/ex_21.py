"""
21- Leia duas matrizes 2x2 com valores reais. Apresente o seguinte menu
ao usuário:
a - somar as duas matrizes
b - subtrair a primeira matriz da segunda
c - adicionar uma constante as duas matrizes
d - imprimir as matrizes
Nas duas primeiras opções uma matriz 2x2 deve ser criada, contendo
o resultado. Na terceira opção o valor da constante deve ser lido e o
resultado da adição da constante deve ser armazenado na própria constante.
"""

from decimal_x_float import Decimal

alfa, beta, gamma = [[], []], [[], []], [[], []]
opcoes, opcao, constante = ('a', 'b', 'c', 'd'), '', Decimal()

print('Preencha a matriz A')
for i in range(2):
    for j in range(2):
        alfa[i].append(Decimal(input(f'A[{i},{j}] = ')))

print('\nPreencha a matriz B')
for i in range(2):
    for j in range(2):
        beta[i].append(Decimal(input(f'B[{i},{j}] = ')))

print('\nO que deseja fazer com as matrizes A e B?'
      '\na - somar as duas matrizes'
      '\nb - subtrair a primeira matriz da segunda'
      '\nc - adicionar uma constante as duas matrizes'
      '\nd - imprimir as matrizes\n')
while opcao not in opcoes:
    opcao = input('Selecione uma opção: ').lower()

if opcao == 'a':
    print('\nA + B = ')
    for i in range(2):
        for j in range(2):
            gamma[i].append(alfa[i][j] + beta[i][j])
            print(gamma[i][j], end=' ')
        print()

elif opcao == 'b':
    print('\nA - B = ')
    for i in range(2):
        for j in range(2):
            gamma[i].append(alfa[i][j] - beta[i][j])
            print(gamma[i][j], end=' ')
        print()

elif opcao == 'c':
    constante = Decimal(input('\nDigite a constante: '))

    print(f'\nA + {constante}')
    for i in range(2):
        for j in range(2):
            alfa[i][j] += constante
            beta[i][j] += constante
            print(alfa[i][j], end=' ')
        print()

    print(f'\nB + {constante}')
    for i in range(2):
        for j in range(2):
            print(beta[i][j], end=' ')
        print()

elif opcao == 'd':
    print('\nMatriz A')
    for i in range(2):
        for j in range(2):
            print(alfa[i][j], end=' ')
        print()

    print('\nMatriz B')
    for i in range(2):
        for j in range(2):
            print(beta[i][j], end=' ')
        print()











