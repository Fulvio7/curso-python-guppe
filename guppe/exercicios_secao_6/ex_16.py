"""
16- Leia um número inteiro positovo ímpar N e imprima todos os
números ímpares de 0 até N em ordem decrescente.
"""

n = -1
while (n % 2 == 0) or (n <= 0):
    n = int(input('Digite o valor de N: '))

for i in range(n, 0, -2):
    print(i)
