"""
3- Leia 10 números reais e armazene-os em um vetor. Calcule o quadrado
de cada elemento e armazene em outro vetor. Ao final imprima ambos.
"""

vetor, vetor_ao_quadrado = [], []

for i in range(10):
    vetor.append(float(input(f'Digite o valor de vetor[{i}]: ')))
    vetor_ao_quadrado.append(vetor[i]**2)

print(f'\nVetor original:\n{vetor}')
print(f'\nVetor ao quadrado:\n{vetor_ao_quadrado}')
