"""
46- Faça um programa que gera um número aleatório de 1 a 1000.
O usuário deve tentar acertar qual foi o número gerado. A cada
tentativa o usuário deve ser informado se o chute é maior ou menor
que o gerado. O programa acaba quando o usuário acerta. Ao final deve
ser impresso o número total de tentativas.
"""
from random import randint

tentativas, alvo, chute = 1, randint(1, 10000), 0

print('*** Jogo do Tiro ao Alvo ***')

while True:
    tentativas += 1
    chute = int(input('Chute um número: '))
    if chute == alvo:
        print('AEEEEEEE! Você acertou!')
        print(f'Número Alvo: {alvo}')
        print(f'Total de Tentativas: {tentativas}')
        break
    elif chute < alvo:
        print('Mais')
    elif chute > alvo:
        print('Menos')




