"""
38- Leia 10 valores numéricos do usuário e ordene-os de forma crescente,
guardando-os em um vetor. Posicione o valor assim que o usuário
inserí-lo. Ao final imprima o resultado.
# Obs: Poderia utilizar sort a cada iteração, mas acho que este não
# é o intuito deste exercício.
"""

vetor = []
print('Preencha o vetor')
for i in range(10):
    vetor.append(int(input(f'vetor[{i}] = ')))

    if i != 0:
        for j in range(i):
            if vetor[j] > vetor[i]:
                vetor[j], vetor[i] = vetor[i], vetor[j]

print(vetor)






