"""
32- Faça um programa que simula o lançamento de dois dados, d1 e d2,
n vezes, e tem como saída o número de cada dado e a relação entre
eles (<,>,=) de cada lançamento.
"""
from random import randint

n = int(input('Digite número de jogadas: '))
print('d1   d2')
for i in range(n):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    if d1 > d2:
        print(f' {d1} > {d2}')
    elif d1 < d2:
        print(f' {d1} < {d2}')
    else:
        print(f' {d1} = {d2}')

