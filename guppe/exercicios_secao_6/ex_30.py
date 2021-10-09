"""
30- Leia o valor de n e calcule as seguintes equações:
1 + 2 + 3 + 4 + 5 + ... + somatório n
1 + 3 + 5 + 7 + 9 + ... + somatório (2*n - 1)
1 - 2 + 3 - 4 + 5 - ... + somatório (2*n - 1) + somatório(-2*n)
"""

n = int(input('Digite o valor de n: '))

soma1, soma2, soma3 = 0, 0, 0

for i in range(1, n+1):
    soma1 += i
    soma2 += (2 * i) - 1
    soma3 += (-2 * i)

soma3 += soma2
print(f'Soma1: {soma1}')
print(f'Soma2: {soma2}')
print(f'Soma3: {soma3}')


