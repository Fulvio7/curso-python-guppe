"""
36- Leia um vetor com 10 números reais, ordene os elementos deste vetor
e no final imprima os números do vetor ordenado.
"""
# Utilizando sort
# v = [9, 6, 7, 4, 8, 5, 2, 1, 3, 0]
# v.sort()
# print(v)

# Utilizando método bubllesort
v = []

print('Preencha o vetor')
for i in range(10):
    v.append(int(input(f'v[{i}] = ')))

for i in range(10):
    for j in range(i, 10):
        if v[j] < v[i]:
            v[i], v[j] = v[j], v[i]

print(v)


