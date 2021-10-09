"""
48- Leia um valor inteiro em segundos e o converta para hora, minutos e
segundos.
"""
import math

segundos_lidos = int(input('Digite um valor inteiro em segundos '))

horas = math.floor(segundos_lidos / 3600)

minutos = math.floor((segundos_lidos % 3600) / 60)

segundos = (segundos_lidos % 3600) % 60

print('Convertendo em horas, minutos e segundos temos:')
print(f'{horas} h')
print(f'{minutos} min')
print(f'{segundos} s')
