"""
26- Leia um número e encontre o primeiro múltiplo de 11, 13 ou 17
após o número lido.
"""

num = int(input('Digite um número inteiro: '))

while True:
    num += 1
    if (num % 11 == 0) or (num % 13 == 0) or (num % 17 == 0):
        print(num)
        break
