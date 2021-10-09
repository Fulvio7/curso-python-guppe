"""
7- Leia 10 números inteiros e armazene-os em um vetor. Imprima o maior
elemento e a sua posição.
"""

vetor, maior, posicao_maior = [], int(), []

for i in range(10):
    vetor.append(int(input(f'Digite o vetor[{i}]: ')))

    if i == 0:
        maior = vetor[i]
        posicao_maior.append(i)
    else:
        if maior < vetor[i]:
            maior = vetor[i]
            posicao_maior.clear()
            posicao_maior.append(i)
        elif maior == vetor[i]:
            posicao_maior.append(i)

print(f'Maior número digitado: {maior}')
print(f'Posições em que o maior está: {posicao_maior}')




