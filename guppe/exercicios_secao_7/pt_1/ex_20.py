"""
20- Preencha um vetor de 10 posições com números inteiros entre 0 e 50.
Preencha um segundo vetor apenas com os números ímpares presentes no
primeiro. Imprima os dois vetores, com 2 elementos por linha
"""

numeros, impares = [], []

for i in range(10):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))

    if (numeros[i] % 2 == 1) and (numeros[i] not in impares):
        impares.append(numeros[i])

print(f'\nVetor:')
for i in range(len(numeros)):
    if i % 2 == 0:
        print(numeros[i], end=' ')
    else:
        print(numeros[i])

print(f'\nNúmeros ímpares distintos: ')
for i in range(len(impares)):
    if i % 2 == 0:
        print(impares[i], end=' ')
    else:
        print(impares[i])




