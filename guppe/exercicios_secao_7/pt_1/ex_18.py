"""
18- Leia um vetor de 10 números inteiros. Leia o valor de x.
Em outro vetor armazene os elementos do primeiro vetor que são múltiplos
de x e imprima o segundo vetor.
"""

numeros, multiplos = [], []

for i in range(10):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))

x = int(input('Digite o valor de x: '))

for num in numeros:
    if num % x == 0:
        multiplos.append(num)

print(f'Números digitados que são múltiplos de {x}: \n{set(multiplos)}')



