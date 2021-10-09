"""
39- Leia um número inteiro positivo n e em seguida imprima n linhas do
chamado Triângulo de Pascal. Exemplo para n = 6:
linha
0-> 1
1-> 1 1
2-> 1 2 1
3-> 1 3 3 1
4-> 1 4 6 4 1
5-> 1 5 10 10 5 1
6-> 1 6 15 20 15 6 1
"""

n, linha, linha_anterior = 0, [], []

while n <= 0:
    n = int(input(f'Digite o número de linhas: '))

for i in range(n):
    linha.clear()
    if (i == 0) or (i == n+1):
        linha.append(1)
        print(linha)
    else:
        for j in range(i+1):
            if (j == 0) or (j == i+1):
                linha.append(1)
            else:
                linha.append((linha_anterior[j] + linha_anterior[j-1]))

    linha_anterior = linha.copy()
    linha_anterior.append(1)
    print(linha_anterior)








