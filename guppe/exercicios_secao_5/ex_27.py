"""
27- Leia a idade de um nadador e classifique-o:
IDADE   CATEGORIA
5 à 7   Infantil A
8 à 10  Infantil B
11 à 13 Juvenil A
14 à 17 Juvenil B
> 18    Sênior
"""

idade = int(input('Digite a idade do nadador: '))

if idade < 5:
    print('Não tem categoria.')
elif 5 <= idade <= 7:
    print('Infantil A')
elif 8 <= idade <= 10:
    print('Infantil B')
elif 11 <= idade <= 13:
    print('Juvenil A')
elif 14 <= idade <= 17:
    print('Juvenil B')
else:
    print('Sênior')



