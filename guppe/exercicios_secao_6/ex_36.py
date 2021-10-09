"""
36- Faça um programa que calcule a diferença entre a soma dos
quadrados dos primeiros 100 números naturais e o quadrado da soma
dos primeiros 100 números naturais. Exemplo:
1**2 + 2**2 + 3**2 + 4**2 + ... + 10**2 = 385
(1 + 2 + 3 + 4 + ... + 10)**2 = 3025
3025 - 385 = 2640
"""

soma1, soma2 = 0, 0

for i in range(101):
    soma1 += i ** 2
    soma2 += i

soma2 = (soma2 ** 2)

diferenca = soma2 - soma1

print(diferenca)
