"""
12- Leia um número inteiro positivo N e imprima todos os números
naturais até N em ordem decrescente.
"""
n = -1
while n <= 0:
    n = int(input('Digite o valor de N: '))

for i in range(n, 0, -1):
    print(i)
