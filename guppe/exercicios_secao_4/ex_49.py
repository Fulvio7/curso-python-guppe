"""
49- Leia um horário de início (h, min, s) e o tempo de duração (s)
de uma experiência biológica. Imprima o horário final (h, min, s)
da experiência.
# não foram tratados os casos em que as horas passam de 24.
"""
import math

print('Preencha o horário inicial: ')
horas_inicio = int(input('Hora de Início: '))
minutos_inicio = int(input('Minutos de Início: '))
segundos_inicio = int(input('Segundos de Início: '))

print('Preencha o tempo de duração: ')
segundos_duracao = int(input('Tempo total em segundos: '))

# encontrando o horario final em segundos
horario_final = (horas_inicio * 3600) \
                + (minutos_inicio * 60) \
                + segundos_inicio \
                + segundos_duracao

# convertendo os segundos do horário inicial em horário final
horas = math.floor(horario_final / 3600)
minutos = math.floor((horario_final % 3600) / 60)
segundos = (horario_final % 3600) % 60

print('Convertendo em horas, minutos e segundos temos:')
print(f'{horas} h')
print(f'{minutos} min')
print(f'{segundos} s')





