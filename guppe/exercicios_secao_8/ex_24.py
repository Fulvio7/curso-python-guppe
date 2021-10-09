"""
24- Escreva uma função que gere um triângulo de altura e lados n e base
2*n-1. Por exemplo:
n = 4
   *
  ***
 *****
*******
"""


def piramide(tamanho):
    for i in range(1, tamanho+1):
        print(((tamanho-i)*' ')+(2*i-1)*'*')


n = 0

print('Pirâmide de Asteriscos *')

while n <= 0:
    n = int(input('Digite o tamanho da pirâmide: '))

piramide(n)
