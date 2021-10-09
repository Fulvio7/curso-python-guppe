"""
6- Faça uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta para segundos.
"""


def converte_para_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos


hours, minutes, seconds = -1, -1, -1

while hours < 0:
    hours = int(input('Digite as horas: '))

while minutes < 0 or minutes > 59:
    minutes = int(input('Digite os minutos: '))

while seconds < 0 or seconds > 59:
    seconds = int(input('Digite os segundos: '))


print(f'Convertendo {hours}h {minutes}min {seconds}seg para segundos temos: ')
print(converte_para_segundos(hours, minutes, seconds), ' segundos.')





