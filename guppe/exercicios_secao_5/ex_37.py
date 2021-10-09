"""
37- Leia o horário de entrada (h e min) e o horário de saída (h e min)
de um estacionamento. Calcule o valor a ser cobrado considerando a
tabela abaixo. Considere apenas horas cheias.
1ª e 2ª hora -> R$ 1,00 cada hora
3ª e 4ª hora -> R$ 1,40 cada hora
>= 5 horas -> R$ 2,00 cada hora
"""
import math

print('=== ESTACIONAMENTO FELIZ ===')
hora_entrada = int(input('Horas de entrada == '))
min_entrada = int(input(f'Minutos de entrada == {hora_entrada}:'))
hora_saida = int(input('Horas de saída == '))
min_saida = int(input(f'Minutos de saída == {hora_saida}:'))

# transformando os horários em total de minutos
tempo_entrada = (hora_entrada * 60) + min_entrada
tempo_saida = (hora_saida * 60) + min_saida
tempo_total = int

if tempo_entrada < tempo_saida:
    tempo_total = tempo_saida - tempo_entrada
else:
    # se passar de 24h temos de acrescentar 1440 minutos à saída
    tempo_total = (tempo_saida + 1440) - tempo_entrada

preco_final = float

if tempo_total <= 60:
    preco_final = 1  # 1 * 1,00

elif 60 < tempo_total <= 120:
    preco_final = 2  # 2 * 1,00

elif 120 < tempo_total <= 180:
    preco_final = 4.2  # 3 * 1,4

elif 180 < tempo_total <= 240:
    preco_final = 5.6  # 4 * 1,4

else:
    preco_final = 2 * math.ceil(tempo_total / 60)

print(f'Preço final: R$ {preco_final}')
