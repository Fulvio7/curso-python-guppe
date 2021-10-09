"""
15- Leia um número inteiro positovo ímpar N e imprima todos os
números ímpares de 0 até N em ordem crescente.
"""

n = -1
while (n % 2 == 0) or (n <= 0):
    n = int(input('Digite o valor de N: '))

for i in range(1, n + 1, 2):
    print(i)
