"""
10- Leia 10 números e armazene-os em um vetor. Imprima o maior e o
menor número inserido.
"""

vetor, maior, menor = [], int(), int()

for i in range(10):
    vetor.append(int(input(f'Insira vetor[{i}]: ')))

    if i == 0:
        maior, menor = vetor[i], vetor[i]
    else:
        if maior < vetor[i]:
            maior = vetor[i]
        if menor > vetor[i]:
            menor = vetor[i]

print(f'Maior número inserido: {maior}')
print(f'Menor número inserido: {menor}')
