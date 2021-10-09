"""
22- Leia dois vetores de 10 posições. Preencha um terceiro vetor, onde:
as posições pares recebem os valores do primeiro e nas ímpares recebem
os valores do segundo.
"""

a, b, c = [], [], []

print('Preencha o vetor A')
for i in range(10):
    a.append(int(input(f'A[{i}]: ')))


print('Preencha o vetor B')
for i in range(10):
    b.append(int(input(f'B[{i}]: ')))


print('Vetor C')
for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])

print(c)


