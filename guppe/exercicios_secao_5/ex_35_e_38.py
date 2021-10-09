"""
35- Leia uma data e determine se ela é válida. Lembre-se dos anos
bissextos.
"""

dias_no_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

data_existe = bool

if ano < 0 or mes > 12 or mes < 0 or dia < 0 or dia > 31:
    data_existe = False
else:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        dias_no_mes[2] = 29

    if dia > dias_no_mes[mes]:
        data_existe = False
    else:
        data_existe = True


if data_existe:
    print('A data existe.')
else:
    print('A data não existe.')


