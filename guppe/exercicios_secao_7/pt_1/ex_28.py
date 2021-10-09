"""
28- Leia 10 números inteiros e armazene-os em um vetor v. Copie os
números ímpares para v1 e os pares para v2. Ao final, imprima o número
de elementos em v1 e em v2.
"""
v, v1, v2 = [], [], []

print('Digite 10 números inteiros: ')
for i in range(10):
    v.append(int(input(f'{i+1}º = ')))

    if v[i] % 2 != 0:
        v1.append(v[i])
    else:
        v2.append(v[i])

print(f'\nVetor original v: {v}')
print(f'\nVetor ímpares v1: {v1}')
print(f'Tamanho {len(v1)}')
print(f'\nVetor pares v2: {v2}')
print(f'Tamanho {len(v2)}')

