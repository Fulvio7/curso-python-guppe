"""
25- Faça um programa que preencha um vetor de tamanho 100, com os 100
primeiros naturais que não são múltiplos de 7 ou que terminam com 7.
"""

vetor, i = [], 0

while True:
    i += 1

    final = (str(i))[-1]

    if (i % 7 != 0) and final != '7':
        vetor.append(i)

    if len(vetor) == 100:
        break

print(vetor)




