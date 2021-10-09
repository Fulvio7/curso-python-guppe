"""
2- Leia 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""

lista = []

print('Insira 6 números inteiros')
for i in range(6):
    lista.append(int(input('Digite o valor inteiro: ')))

print('Números digitados')
for i in range(6):
    print(lista[i])
