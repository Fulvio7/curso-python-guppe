"""
29- Escreva um programa para calcular ao valor da série abaixo,
para 5 termos.
S = 0 + 1/2! + 2/4! + 3/6! + 4/8! + 5/10!
"""
soma, fatorial = 0, 1

for i in range(10000):
    fatorial = 1
    for j in range(1, (2*i)+1):
        fatorial *= j
    soma += (i / fatorial)

# soma = (1/2) + (2/24) + (3/720) + (4/40320)
# 0.5875992063492064
print(soma)
