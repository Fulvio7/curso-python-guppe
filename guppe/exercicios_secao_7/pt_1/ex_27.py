"""
27- Leia um vetor de 10 posições e armazene números inteiros.
Imprima os valores primos e suas respectivas posições no vetor.
"""

vetor, primos, posicoes = [], [], []

print('Digite 10 números inteiros')
for i in range(10):
    vetor.append(int(input('--> ')))
    if (vetor[i] % 2 != 0) and (vetor[i] != 1):
        cont = 0
        for j in range(1, vetor[i]):
            if vetor[i] % j == 0:
                cont += 1
            if cont > 2:
                break
        if cont < 2:
            primos.append(vetor[i])
            posicoes.append(i)

print('Números primos no vetor')
for i in range(len(primos)):
    print(f'vetor[{posicoes[i]}] = {primos[i]}')


