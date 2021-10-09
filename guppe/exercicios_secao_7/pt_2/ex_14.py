"""
14- Faça um programa para gerar automaticamente números entre 0 e 99 de
uma cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de
5 números, gere estes dados de modo a não ter números repetidos dentro
da cartela. O programa deve exibir na tela a cartela gerada.
"""
from random import randint

cartela, num = [[], [], [], [], []], int()

for i in range(5):
    for j in range(5):
        while True:
            num = randint(0, 99)
            if num not in cartela:
                cartela[i].append(num)
                break

        print(cartela[i][j], end=' ')
    print()








