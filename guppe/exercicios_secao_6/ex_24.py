"""
24- Leia um número inteiro e calcule a soma de todos os divisores
desse número, com excessão dele próprio.
"""

number, soma = -1, 0

while number <= 0:
    number = int(input('Digite um número positivo: '))

for i in range(1, number):
    if number % i == 0:
        soma += i

print(f'Soma dos divisores: {soma}')
