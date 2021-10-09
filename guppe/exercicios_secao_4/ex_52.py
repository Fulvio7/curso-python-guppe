"""
52- Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve
ser repartido proporcionalmente ao valor que cada um deu para a
realização da aposta. Faça um programa que leia quanto cada um investiu,
o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base
no valor investido.
"""
print('===== LOTERIA DAORA =====')
premio_total = float(input('Digite o valor do prêmio: R$ '))

print('Digite o valor investido por cada apostador:')
aposta_jogador_1 = float(input('Jogador 1: R$ '))
aposta_jogador_2 = float(input('Jogador 2: R$ '))
aposta_jogador_3 = float(input('Jogador 3: R$ '))

total_apostado = aposta_jogador_1 + aposta_jogador_2 + aposta_jogador_3

premio_jogador_1 = (aposta_jogador_1 / total_apostado) * premio_total
premio_jogador_2 = (aposta_jogador_2 / total_apostado) * premio_total
premio_jogador_3 = (aposta_jogador_3 / total_apostado) * premio_total

print('Caso vocês ganhem, o resultado é o seguinte: ')
print(f'Prêmio jogador 1: R$ {premio_jogador_1:.2f}')
print(f'Prêmio jogador 2: R$ {premio_jogador_2:.2f}')
print(f'Prêmio jogador 3: R$ {premio_jogador_3:.2f}')


