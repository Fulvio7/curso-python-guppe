"""
17- Faça uma função que receba dois números inteiros positivos por
parâmetro e retorne a soma dos N números inteiros existentes entre eles.
"""


def soma_entre(inicio, fim):
    soma = 0
    for i in range(inicio + 1, fim):
        soma += i
    return soma


n_inicio, n_fim = 0, 0

while n_inicio <= 0:
    n_inicio = int(input('Digite o número de partida: '))

while n_fim <= 0:
    n_fim = int(input('Digite o número de parada: '))


print(soma_entre(n_inicio, n_fim))
