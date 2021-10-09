"""
23- Escreva uma função que gera um triângulo lateral de altura 2*n-1 e
n de largura. Exemplo:
n = 3
*
**
***
**
*
"""


def asteriscos(tamanho):
    for i in range(1, tamanho):
        print(i*'*')
    for i in range(tamanho, 0, -1):
        print(i*'*')


n = 0

print('Triângulo de Asteriscos *')

while n <= 0:
    n = int(input('Digite o tamanho do triângulo: '))

asteriscos(n)
