"""
22- Crie uma função que receba como parâmetro um valor inteiro e gere como
saída n linhas com pontos de exclamação, conforme o exemplo abaixo:
n = 5
!
!!
!!!
!!!!
!!!!!
"""


def exclamacoes(tamanho):
    for i in range(1, tamanho+1):
        print(i*'!')


n = 0

print('Triângulo de Exclamações!')

while n <= 0:
    n = int(input('Digite o número de linhas: '))

exclamacoes(n)
