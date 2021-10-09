"""
27- Em Matemática, o número harmônico designado H(n) define-se
como sendo a soma da série harmônica:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Leia um valor inteiro positivo n e calcule seu H(n).
"""
h_n = float()

print('Encontrando o número harmônico H(n):')
print('H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n\n')
n = int(input('Digite o valor de n: '))

for i in range(1, n+1):
    h_n += (1 / i)

print(f'H(n) = {h_n}')
