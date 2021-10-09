"""
5- Leia um vetor de 10 posições. Calcule e imprima quantos valores
pares ele possui.
"""

vetor, total_pares, total_zeros = [], 0, 0

for i in range(10):
    vetor.append(int(input(f'Insira vetor[{i}]: ')))
    if vetor[i] % 2 == 0 and vetor[i] != 0:
        total_pares += 1
    elif vetor[i] == 0:
        total_zeros += 1

print(f'Total de números pares digitados: {total_pares}')
print(f'Total de números zeros digitados: {total_zeros}')
