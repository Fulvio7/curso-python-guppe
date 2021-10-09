"""
20- Faça um algoritmo que receba um número inteiro positivo n e calcule
o seu fatorial, n!
"""


def fatorial(numero):
    aux, total = 1, 1
    while aux <= numero:
        total *= aux
        aux += 1
    return total


num = 0
print('Descobra o fatorial de um número')

while num <= 0:
    num = int(input('Digite um número inteiro positivo: '))

print(fatorial(num))






