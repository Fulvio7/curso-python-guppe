"""
51- Um funcionário recebe aumento anual. Em 1995 foi contratado por
R$ 2000,00. Em 1996 recebeu aumento de 1,5%. A partir de 1997, os
aumentos sempre correspondem ao dobro do ano anterior. Faça um
programa que determine o salário atual do funcionário.
"""
from datetime import datetime

ano, salario = 1995, float()

while ano <= datetime.now().year:
    if ano == 1995:
        salario = 2000
    elif ano == 1996:
        salario *= 1.015
    else:
        salario *= 2
    print(f'{ano} R$ {salario:.2f}')
    ano += 1


