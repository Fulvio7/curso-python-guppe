"""
17- Leia um número inteiro positivo N e imprima a soma dos números
naturais até N em ordem crescente.
"""
n = -1
while n <= 0:
    n = int(input('Digite o valor de N: '))

soma = 0
for i in range(1, n + 1):
    soma += i

print(f'Soma = {soma}')
