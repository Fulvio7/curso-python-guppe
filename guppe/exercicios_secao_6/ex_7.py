"""
7- Faça um programa que leia 10 números inteiros e que rejeite
negativos, e imprima a sua média.
"""
num = -1
soma = 0
cont = 1
while cont <= 10:
    while num < 0:
        num = int(input(f'Digite o n{cont}: '))
    soma += num
    num = -1
    cont += 1

media = soma / 10

print(f'Média = {media}')


"""resposta = -1
while resposta < 0:
    resposta = int(input('Digite o valor'))
"""