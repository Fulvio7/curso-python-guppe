"""
50- Implemente um programa que encontre o ano de nascimento de
uma pessoa, partindo de sua idade e ano atual.
"""

from datetime import date

ano_atual = date.today().year

idade = int(input('Digite a sua idade '))
ja_nirvou = input('Você já aniversariou este ano? [s ou n] ').lower()

ano_nasc = ano_atual - idade

if ja_nirvou == 's':
    print(f'Você nasceu em {ano_nasc}.')
elif ja_nirvou == 'n':
    print(f'Você nasceu em {ano_nasc - 1}.')
else:
    print('Erro: Resposta inválida.')


