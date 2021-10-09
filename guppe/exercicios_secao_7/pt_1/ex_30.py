"""
30- Faça um programa que leia um vetor de 10 elementos. Crie um vetor
que seja a intersecção entre os vetores anteriores, ou seja, que
contém apenas os números que estão em ambos os vetores.
Não deve conter números repetivos.
"""

v1, v2 = [], []

print('Preencha v1')
for i in range(10):
    v1.append(int(input(f'v1[{i}] = ')))

print('\nPreencha v2')
for i in range(10):
    v2.append(int(input(f'v2[{i}] = ')))

v1 = set(v1)
v2 = set(v2)
intersec = v1.intersection(v2)

print(f'\nIntersecção entre v1 e v2: \n{intersec}')
