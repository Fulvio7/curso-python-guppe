"""
19- Preencha um vetor de 50 posições segundo a equação abaixo, onde i
é a posição do vetor. Ao final imprima o vetor:
(i + 5 * i) % (i + 1)
"""

vetor = []
for i in range(50):
    vetor.append((i + 5 * i) % (i + 1))
print(vetor)

