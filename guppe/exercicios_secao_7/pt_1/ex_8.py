"""
8- Leia 6 números inteiros e armazene-os em um vetor. Imprima o vetor
na ordem inversa.
"""

vetor = []

for i in range(6):
    vetor.append(int(input(f'Insira vetor[{i}]: ')))

print(vetor[::-1])

