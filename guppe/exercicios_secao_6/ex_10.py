"""
10- Faça um programa que calcule e mostre a soma dos
50 primeiros números pares.
"""

soma = 0

for i in range(0, 101, 2):
    soma += i

print(f'A soma dos 50 primeiros números pares é: {soma}')

