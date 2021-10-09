"""
53- Escreva um programa que leia um número inteiro positivo n e em
seguida imprima n linhas o chamado Triângulo de Floyd.
Para n = 5, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

print('TRIÂNGULO DE FLOYD')
linhas = int(input('Digite o valor de n: '))
colunas, num = 1, 0
for i in range(1, linhas+1):
    for j in range(1, colunas+1):
        num += 1
        print(num, end=' ')
    print(end='\n')
    colunas += 1



