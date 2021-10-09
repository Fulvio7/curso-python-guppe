"""
21- Leia do usuário dois vetores, A e B, e com 10 números inteiros cada.
Crie um novo vetor C calculando: C = A - B. Ao final, imprima C.
"""

a, b, c = [], [], []

print('Preencha o vetor A:')
for i in range(10):
    a.append(int(input(f'A[{i}]: ')))

print('Preencha o vetor B:')
for i in range(10):
    b.append(int(input(f'B[{i}]: ')))

    c.append(a[i] - b[i])

print(f'Vetor C = A - B \n{c}')


