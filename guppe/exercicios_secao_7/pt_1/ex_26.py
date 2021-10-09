"""
26- Faça um programa que calcule o desvio padrão de um vetor v contendo
n = 10 números, onde m é a média do vetor.
Desvio Padrão = Raiz( (1/(n-1)) * E((v[i] - m)²) )
"""
from math import sqrt

v = [1.5, 1.75, 2, 2.5, 2.5, 2.5, 2.75, 3.25, 3.75, 4.75]

soma = 0
for num in range(10):
    soma += v[num]
media = soma / 10

somatorio = 0
for num in range(10):
    somatorio += (v[num] - media)**2

desvio_padrao = sqrt((1/9) * somatorio)
print(desvio_padrao)


# from statistics import stdev
# print(stdev([1.5, 1.75, 2, 2.5, 2.5, 2.5, 2.75, 3.25, 3.75, 4.75]))
# 0.9750356118852503  # -> referência stdev
# 0.9750356118852502  # -> resultado obtido



