"""
17- Leia um vetor de 10 posições e atribua o valor 0 para todos os
números negativos inseridos.
"""

numeros = []

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))

    if num < 0:
        numeros.append(0)
    else:
        numeros.append(num)

print(numeros)
