"""
26- Faça um algorítmo que receba um número inteiro positivo n e calcule
o somatório de 1 até n.
"""


def somatorio(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma


numero = 0
print('Somatório de 1 até N ')

while numero <= 0:
    numero = int(input('Digite o valor (inteiro positivo) de N: '))

print(somatorio(numero))
