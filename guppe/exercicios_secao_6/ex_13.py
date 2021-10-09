"""
13- Leia um número inteiro positivo par N e imprima todos os números
pares de 0 até N em ordem crescente.
"""

n = -1
while (n % 2 != 0) or (n <= 0):
    n = int(input('Digite o valor de N: '))

for i in range(0, n + 1, 2):
    print(i)
