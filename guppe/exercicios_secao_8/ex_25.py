"""
25- Faça uma função que receba um número inteiro N como parâmetro,
calcule e retorne o resultado da seguinte série:
S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3)
"""


def serie(n):
    soma = 0
    for i in range(1, n+1):
        soma += ((i**2)+1) / (i+3)
    return soma


numero = 0
print('Somatório da série (N² + 1)/(N + 3) ')

while numero <= 0:
    numero = int(input('Digite o valor (inteiro positivo) de N: '))

print(serie(numero))
