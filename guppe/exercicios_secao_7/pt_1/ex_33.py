"""
33- Leia um vetor de 15 posições e o compacte, ou seja, elimine as
posições com valor igual a zero. Mova os elementos para trás a cada
eliminação.
"""

vetor = []

print('Preencha o vetor')
for i in range(15):
    vetor.append(int(input(f'v[{i}] = ')))

for i in range(14, -1, -1):
    if vetor[i] == 0:
        vetor.pop(i)

print(vetor)





