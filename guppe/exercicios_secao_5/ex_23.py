"""
23- Leia um ano e determine se ele é bissexto. O ano bissexto é aquele
divisível por 400 ou se for divisível por 4 e não por 100.
"""

ano = int(input('Digite um ano qualquer: '))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')


