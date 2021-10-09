"""
11- Leia um número inteiro positivo N e imprima todos os números
naturais até N em ordem crescente.
"""
n = -1
while n <= 0:
    n = int(input('Digite o valor de N: '))

for i in range(1, n + 1):
    print(i)

