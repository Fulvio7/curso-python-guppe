"""
23- Leia dois vetores de 5 posições de números reais. Imprima os dois
vetores e o produto escalar entre eles:
x0*y0 + x1*y1 + x2*y2 + ... + xn*yn
"""

x, y, produto_escalar = [], [], 0

print('Preencha o vetor X')
for i in range(5):
    x.append(int(input(f'X[{i}]: ')))

print('Preencha o vetor Y')
for i in range(5):
    y.append(int(input(f'Y[{i}]: ')))

    produto_escalar += x[i] * y[i]

print(f'Produto escalar entre X e Y: {produto_escalar}')


